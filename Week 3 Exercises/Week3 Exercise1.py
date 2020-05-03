"""
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract
all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list
where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data
structure to the screen. Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
"""
from pprint import pprint

# Create list that will hold tuples, open file and read it in as one big string
list_of_vlans = []
with open('show_vlan.txt') as f:
    show_vlan = f.read()

# Loop through file line by line via for loop and each put line in list element
for line in show_vlan.splitlines():
    # We want to skip 1st, 2nd and 4th line as its just header
    if 'VLAN' in line or '-' in line or line.startswith(' '):
        continue # don't iterate over such lines and continue with loop
    fields = line.split() # Split each line into smaller list separated by whitespace
    vlan_id = fields[0]
    vlan_name = fields[1]
    # Append the tuples containing vlan id and name to the list
    list_of_vlans.append((vlan_id, vlan_name))

# Once all tuples have been appended to the list print the list to console
pprint(list_of_vlans)


