"""
4. Use send_config_set() and send_config_from_file() to make configuration changes.

The configuration changes should be benign. For example, on Cisco IOS I typically change the logging buffer size.

As part of your program verify that the configuration change occurred properly.

For example, use send_command() to execute 'show run' and verify the new configuration.
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

# Send show run command to device to see current logging status and print to console
output = net_connection.send_command('show run | inc logging')
print(output)
# Send command to change logging buffer size
net_connection.send_config_set('logging buffered 4000000')
# Commit this change on IOS-XR device
net_connection.commit()

# Send show run command again to verify successful config change and print to console
output = net_connection.send_command('show run | inc logging')
print('-' * 30)
print(output)

# This time send command to device from a txt file
net_connection.send_config_from_file('config.txt')
# Commit this change on IOS-XR device
net_connection.commit()

# Send show run command again to verify successful config change
output = net_connection.send_command('show run | inc logging')
# Check if logging buffer size is as we set it via config and print confirmation to console
if '4000000' in output:
    print('Configuration change was successful')
else:
    print('Logging buffer size not correct')
print('-' * 30)