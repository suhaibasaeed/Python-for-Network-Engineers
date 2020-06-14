"""
1b. In a separate Python file named 'my_devices.py', define a dictionary 'rtr1' with the following key-value pairs:
host = rtr1.domain.com
username = cisco
password = cisco123
device_type = cisco_ios

Import my_devices into this program, and print the rtr1 dictionary to the screen using pprint.
"""

import my_devices
from pprint import pprint

# Print the rtr1 dict from my_devices file
pprint(my_devices.rtr1)
