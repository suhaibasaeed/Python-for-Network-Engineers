"""
2. Use send_command() to send a show command down the SSH channel.

Retrieve the results and print the results to the screen.

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

# Send show ip interface brief command to device
output = net_connection.send_command('sh ip int br')

# Print output of this command to the console
print(output)

# Gracefully disconnect from SSH session
net_connection.disconnect()