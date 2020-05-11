
"""This code can be used with aruba switches with SSH configured 
to find the all the connected devices,to the Core Backbone Switch.
You will need to provide a JSON file with the device ip adress you're
trying to MAP. I have used it to find devices connected to the core switch
to MAP it out in our ZABBIX Monitoring system"""

from netmiko import ConnectHandler
import sys
import os
import json
import re

with open("credentials.json", "rt") as u:
	credentials = json.loads(u.read())
		
"""Credentials to Login to the switch"""

hp_switch = {
    'device_type': '{}'.format(credentials["device_type"]),
    'host':'{}'.format(credentials["host"]),
    'username':'{}'.format(credentials["username"]),
    'password':'{}'.format(credentials["password"])
}

net_connect = ConnectHandler(**hp_switch)
net_connect.find_prompt()
#output = net_connect.send_command('sh lldp info remote-device 1-48 | include Address')

"""Reads the JSON file with IP adresses of the devices to find"""

with open("LesoleilSwitchs.json", "r") as ip:
	x=ip.read()
	ip_list = json.loads(x)

final_Ip_list = (ip_list["ip"])
#print (final_Ip_list[1])

x = open("Arp_info.txt", "a")

"""Find the Availbility of the network device, if available
add it to the DICT with True value else add it with False"""

switchAvailabilityResult = {}
for ip in final_Ip_list:				
	output = net_connect.send_command ('ping {}'.format(ip))
	print (output)

	if output=="Request timed out.":
		print ("Host unreachable")
		switchAvailabilityResult.update({ip: 'False'})
	else:
		print ("Host Reachable, moving to next step")
		switchAvailabilityResult.update({ip: 'True'})
		Arp_Output = net_connect.send_command ('sh arp | include {}'.format(ip))
		print (Arp_Output)
		x.write(Arp_Output)
		x.write("\n")
x.close()

"""Regular expression pattern to find the port numbers from the Arp_Output FIle"""

pattern = re.compile("\d+\s\s$")
port_numbers = []

with open("Arp_info.txt", "rt") as parse:
        for line in parse:
                y = pattern.search(line)
                if y==None:
                        pass
                else:
                        port_numbers.append(y.group())

"""Finally display the result"""

i=0
for ip in final_Ip_list:
	if switchAvailabilityResult[ip]=="True":
		print (("switch {} is connected to the core switch on Port " + port_numbers[i]).format(ip))
		i+=1
	else:
		print (("Could not find switch {} from the core switch  " ).format(ip))
