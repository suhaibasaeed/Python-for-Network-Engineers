"""
3a. Create a YAML file that defines a list of interface names. Use the expanded form of YAML.

Use a Python script to read in this YAML list and print it to the screen.

The output of your Python script should be:
['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4', 'Ethernet5', 'Ethernet6', 'Ethernet7', 'Management1', 'Vlan1']
"""

import yaml

# Open yaml file with list in it
with open('w7e3a.yml') as f:
    output = yaml.safe_load(f) # Load into f variable

print(output)
