"""
2. Create three separate lists of IP addresses.

The first list should be the IP addresses of the Houston data center routers,
and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers,
and it should have at least eight RFC1918 IP addresses (including some addresses that overlap with Houston data center).

The third list should be the IP addresses of the Chicago data center routers,
and it should have at least eight RFC1918 IP addresses.
The Chicago IP addresses should have some overlap with both the IP addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
"""

houston_dc_routers = ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5', '10.1.1.6', '10.1.1.7', '10.1.1.8',
              '10.1.1.9', '10.1.1.10', '10.1.1.1', '10.1.1.2']

atlanta_dc_routers = ['10.2.1.1', '10.2.1.2', '10.2.1.3', '10.2.1.4', '10.2.1.5', '10.2.1.6', '10.1.1.1', '10.1.1.2']

chicago_dc_routers = ['10.3.1.1', '10.3.1.2', '10.3.1.3', '10.3.1.4', '10.3.1.5', '10.3.1.6', '10.1.1.1', '10.2.1.1']

# Convert lists to sets
houston_dc_routers = set(houston_dc_routers)

atlanta_dc_routers = set(atlanta_dc_routers)

chicago_dc_routers = set(chicago_dc_routers)

# Use intersection operation to find IP addresses duplicated between Houston and Atlanta
hous_atlan_dup = houston_dc_routers & atlanta_dc_routers
print('-' * 80)
print('Duplicate IPs between Houston & Atlanta:\n{}'.format(hous_atlan_dup))
print('-' * 80)

# Use intersection operation to find IP addresses duplicated between all 3 sites
hou_atl_chi_dup = houston_dc_routers & atlanta_dc_routers & chicago_dc_routers
print('Duplicate IPs between all 3 sites:\n{}'.format(hou_atl_chi_dup))
print('-' * 80)

# Find elements unique to Chicago by subtracting the other two sets from it
chic_unique = chicago_dc_routers - houston_dc_routers - atlanta_dc_routers
print('Elements unique to Chicago site:\n{}'.format(chic_unique))
print('-' * 80)