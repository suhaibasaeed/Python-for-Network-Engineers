"""
6. Optional, connect to two networking devices one after the other.
Use send_command() to execute a show command on each of these devices.
Print this output to the screen.

"""

from netmiko import Netmiko

# Dictionaries that hold the device details
cisco_xr = {
    'host': 'sbx-iosxr-mgmt.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'device_type': 'cisco_xr',
    'port' : 8181
}

cisco_xe = {
    'host': 'ios-xe-mgmt-latest.cisco.com ',
    'username': 'developer',
    'password': 'C1sco12345',
    'device_type': 'cisco_xe',
    'port' : 8181
}
# Loop through the 2 dictionaries connecting to each device one by one
for device in (cisco_xr, cisco_xe):
    net_connection = Netmiko(**device)
    # Send show arp command to device and print output to console
    output = net_connection.send_command('sh ip int br')
    print(output)
    print('-' * 80)