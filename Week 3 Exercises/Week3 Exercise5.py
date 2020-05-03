"""Construct a list of 254 IP addresses. The base IP address should be equal to '10.10.100.0' or '10.10.100.'.

You should use the 'range' builtin to accomplish this.

Your list should have all of the IP addresses from 10.10.100.1 to 10.10.100.254.

Use Python's 'enumerate' to print out all of the IP addresses and their corresponding list index. The output should look similar to the following:
0 ---> 10.10.100.1
1 ---> 10.10.100.2
2 ---> 10.10.100.3
3 ---> 10.10.100.4
4 ---> 10.10.100.5
...

Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.

Using a loop and os.system("ping -c 3 10.10.100.3") try pinging all of the IP addresses in this short list. For Windows the command will probably be os.system("ping -n 3 10.10.100.3").

Put a variable at the top to define whether you are using Windows or Linux/MacOs. This should be similar to the following:
WINDOWS = False

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux"""

import os

# Set base IP and initialise list of all IP addresses
base_ip = '10.10.10.0'
ip_list = []
arrow = ' ---> '

WINDOWS = True

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

# Loop through range from 1 - 254
for i in range(1,255):
    new_ip = base_ip.split('.') # split the base IP address on whitespace into a list
    new_ip.pop() # Remove last element in the list - which will be last octet thats changes each iteration
    last_octet = str(i) # change i to a string so we can add it to the list
    new_ip.extend([last_octet]) # add element to the list, this new element will be the changed last octet

    new_ip = '.'.join(new_ip) # Join this list back together so we get a string
    ip_list.append(new_ip) # Add this new string to the bigger list of IPs

#Loop through list of all IPs enumurating each element with its corresponding IP
for ip in enumerate(ip_list):
    index, ip_add = ip # Pass the elements of type into corresponding variable
    print("%i %s %s" % (index, arrow, ip_add)) # Print to console

# We only want 10.10.10.3 - 10.10.10.6
new_ip_list = ip_list[2:6]

print('-' * 80)
# Loop through IP addresses in the list
for host in new_ip_list:
    print("IP Address: ", host)
    return_code = os.system("{} {}".format(base_cmd, host))
    print('-' * 80)
print('-' * 80)

