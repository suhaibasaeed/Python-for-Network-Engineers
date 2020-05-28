"""
3. Find a command on your device that has additional prompting.
Use send_command_timing to send the command down the SSH channel.
Capture the output and handle the additional prompting.
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

# Send ping command to device and capture output
net_connection.send_command_timing('ping ipv4')
# Handle additional prompting by sending IP address we want to ping
output = net_connection.send_command_timing('8.8.8.8')
# Print captured output
print(output)