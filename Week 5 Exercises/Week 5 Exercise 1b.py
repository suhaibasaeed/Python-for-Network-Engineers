"""
1b. Expand on ssh_conn function from exercise1 except add fourth parameter 'device_type' with default value 'cisco_ios'.
Print all four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.
"""

# Define function with 4 parameters which prints them to console
def ssh_con2(ip_add, username, password, device_type='cisco_ios'):
    print('ip add: {}'.format(ip_add))
    print('Username: {}'.format(username))
    print('Password: {}'.format(password))
    print('Device type: {}'.format(device_type))
    print('-' * 20)

# Call function specifying the device_type
ssh_con2('192.168.1.1', 'root', 'Pa55word', 'junos')

# Call function again but don't specify device_type
ssh_con2('192.168.1.1', 'root', 'Pa55word')

# Create dictionary which will map to parameters
my_device = {
    "ip_add": "10.1.1.1",
    "device_type": "nx_os",
    "username": "admin",
    "password":"cisco"
}
# Call function using **kwargs
ssh_con2(**my_device)