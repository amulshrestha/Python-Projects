'''
Get IP Address of any website using python
Author: Amul Shrestha
'''

#Importing necessary packages.
import socket 

#Displaying Banner
print("""
 _____ _           _    ___ ____           __
|  ___(_)_ __   __| |  |_ _|  _ \    ___  / _|   __ _ _ __  _   _
| |_  | | '_ \ / _` |   | || |_) |  / _ \| |_   / _` | '_ \| | | |
|  _| | | | | | (_| |   | ||  __/  | (_) |  _| | (_| | | | | |_| |
|_|   |_|_| |_|\__,_|  |___|_|      \___/|_|    \__,_|_| |_|\__, |
                                                           |___/
__        __   _         _ _
\ \      / /__| |__  ___(_) |_ ___
 \ \ /\ / / _ \ '_ \/ __| | __/ _ /
  \ V  V /  __/ |_) \__ \ | ||  __/
   \_/\_/ \___|_.__/|___/_|\__\___|
   
   Author: Amul Shrestha
   """)
#Asking input of the website which IP needs to find
site = input("Enter the website: ")

#Get host hostname
hostname = socket.gethostname()

#Displaying hostname
print('Your Hostname is: ' + hostname)

#Getting host IP
host_ip = socket.gethostbyname(hostname)

#Displaying host IP 
print('Your Ip Address is: ' + host_ip)

#Fetching the IP of the website
ip = socket.gethostbyname(site)

#display the IP
print('The IP Address of ' + site + ' is: '  + ip)
print("""
 _____ _                 _
|_   _| |__   __ _ _ __ | | __  _   _  ___  _   _
  | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | |
  | | | | | | (_| | | | |   <  | |_| | (_) | |_| |_
  |_| |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_(_)
                                |___/
""")