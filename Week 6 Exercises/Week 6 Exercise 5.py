"""
5. Optional, use send_command() in conjunction with ntc-templates to execute a show command.
Have TextFSM automatically convert this show command output to structured data.

"""

from netmiko import Netmiko

# Dictionaries that hold the device details
cisco_device = {
    'host': 'sbx-iosxr-mgmt.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'device_type': 'cisco_xr',
    'port': 8181
}

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connection = Netmiko(**cisco_device)

# Send show ip int brief command to device and use TextFSM to return structured list
output = net_connection.send_command('show ip interface brief', use_textfsm=True)
print(output)