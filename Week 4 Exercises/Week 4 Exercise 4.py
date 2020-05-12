"""
​4.  Using a named regular expression (?P<name>), extract the model from the below string:

Note that, in this example, '881' is the relevant model.
Your regular expression should not, however, include '881' in its search pattern since this number changes across devices.

Using a named regular expression, also extract the '236544K/25600K' memory string.

Once again, none of the actual digits of the memory on this device should be used in the regular expression search pattern.

Print both the model number and the memory string to the screen.

"""

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

import re

# Search for and match the model number of the device using RE and put result in dictionary key value pair called model
model_no = re.search(r"Cisco (?P<model>\S+)", show_version)
# Return dictionary using groupdict() method and put it into model variable
model = model_no.groupdict()
# Extract value only from dictionary and print to console
new_model = model['model']
print(new_model)

# Match bytes of memory on 1st line and extract it using RE, into dictionary
memory = re.search(r"with (?P<mem_count>\S+)", show_version)
# Return dictionary and put it into mem variable
mem = memory.groupdict()
# Extract value from dict and print to console
new_mem = mem['mem_count']
print(new_mem)

