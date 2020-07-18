"""
2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list.
Use the .extend() method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list.
Print out the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
"""

# List of 5 IP addresses
ip_add = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']
# Append one more IP address to end using append method
ip_add.append('10.1.1.1')
# Append two more IP addresses to end of list using extend method
ip_add.extend(['10.1.1.2','10.1.1.3'])
# Use list concatenation to add two more IP addresses to end of list
ip_add = ip_add + ['10.1.1.4', '10.1.1.5']
# Print entire list to console
print(ip_add)
print('\n')
# Print out 1st and Last IP addresses in list
print(ip_add[0], ip_add[-1])
# Use pop method to remove 1st and last IP address in list
ip_add.pop(0)
ip_add.pop()
#Change first IP address in list to 2.2.2.2
ip_add[0] = '2.2.2.2'
# Print this new IP address added
print(ip_add[0])
