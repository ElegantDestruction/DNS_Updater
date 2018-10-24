#! /bin/python
import socket

# Function to display hostname and
# IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP_Address = s.getsockname()[0]
print(IP_Address)
s.close()

current_file = open('current_file','r')
current_IP = current_file.read()
current_IP = current_IP.strip()
current_file.close()

if (!(IP_Address == current_IP)):
    #INSERT BIT ABOUT UPDATING DNS KEY HERE
    ##########################
    ##########################



    overwrite = open('current_address.txt','w')
    overwrite.write(IP_Address)
    overwrite.close()
