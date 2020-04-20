import json
import os
from netmiko import ConnectHandler

# ip = ["192.168.1.10","10.0.0.1","10.0.0.2","10.0.0.33","10.0.0.34","10.0.0.65","10.0.0.66","10.0.0.97","10.0.0.98","10.0.0.129","10.0.0.130","10.0.0.161","10.0.0.162"]


f = open('ip_json.json', 'r')
jsonread = f.read()
json_dict = json.loads(jsonread)
ip_lists = json_dict['ip']

def ChechHostAVail():
    for i in ip_lists:
     response = os.system("ping -c 1 " + i)
     if response == 0 :
        print ("Host exist, calling function config " )
        cisco = dict(device_type="cisco_ios", host=i,username="dev", password="999999999")
        net_connect = ConnectHandler(**cisco)
        net_connect.find_prompt()
     elif response == 1:
        print ("There is no host with ip " + i)
    return


ChechHostAVail()


    # output = net_connect.send_command('sh run | include aaa')
    # print (output)
    # print ("Switch" + {element} + "done")




