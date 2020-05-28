"""
1. Using Netmiko, establish a connection to a network device and print out the device's prompt.
"""
from netmiko import Netmiko

# Create dictionary that holds device details
cisco_device = {
    'host': 'sbx-iosxr-mgmt.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'device_type': 'cisco_xr',
    'port' : 8181
}

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connection = Netmiko(**cisco_device)
# Get the devices prompt
output = net_connection.find_prompt()
# Print prompt to console
print(output)

# Gracefully disconnect from SSH session
net_connection.disconnect()