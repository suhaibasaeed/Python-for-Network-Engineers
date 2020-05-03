"""Loop over data structure and extract all of the MAC addresses. Process all of the MAC addresses to get them into a standard format.
Print all of the new standardized MAC address to the screen. The standardized format should be as follows:
00:62:EC:29:70:FE
The hex digits should be capitalized. Additionally, there should be a colon between each octet in the MAC address."""

import textwrap

arp_table = [('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')]

# Loop through tuples in the list
for line in arp_table:
    mac_add = line[1] # Set mac address to 2nd element in the tuple
    mac_add = mac_add.upper() # change the lowercase Hex characters to uppercase
    mac_add = mac_add.split('.') # Remove the '.' which separate the characters into a list

    new_mac_add = ''.join(mac_add) # Join mac address back together into a list
    new_mac_add = textwrap.wrap(new_mac_add, 2) # Split the mac address into 6 even parts
    new_mac_add = ':'.join(new_mac_add) # join back together with a colon this time



    print(new_mac_add)
