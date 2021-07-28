# individual
import json
from math import pi
import pandas as pd
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum

new_data={}
  
# Opening JSON file
f = open('D:\Amul\Github\Python-Projects\Bokeh-visualization\logs.json',)
  
# returns JSON object as a dictionary
data = json.load(f)
  
# Iterating through the json list
for i in data["hits"]["hits"]:
    for j in i["_source"]["application"].keys():
        if j in new_data.keys():
            new_data[j] += i["_source"]["application"][j]
        else:
            new_data[j] = i["_source"]["application"][j]
            
# Closing file
f.close()

def applicationUsage():
    output_file("ApplicationUsage.html")
    x = new_data

    data = pd.Series(x).reset_index(name='time').rename(columns={'index':'application'})
    data['angle'] = data['time']/data['time'].sum() * 2*pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, title="Application Usage", toolbar_location=None,
            tools="hover", tooltips="@application: @time", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='application', source=data)

    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color = None

    return show(p)

applicationUsage()