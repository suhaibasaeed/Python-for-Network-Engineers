"""
3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together.
Should be a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
"""

from pprint import pprint
# Open the file
show_arp = open("show_arp.txt")
# Put file in one line at a time and put into list
output = show_arp.readlines()
# Use list slice to get rid of command and header line
output = output[1:]
# Use pretty print to print list to console
pprint(output)

# Sort list based on IP address using sort method
output.sort()
# Create new list slice with only first 3 ARP entries
new_output = output[:3]
# Use join method to bring 3 entries together using \n as separator
new_output = '\n'.join(new_output)

# Open a new file using open function with write parameter
new_file = open("arp_entries.txt", mode="w")
# Write the string of 3 ARP entries to this new file
new_file.write(new_output)
# Flush contents into file to populate it
new_file.flush()
# Close file
new_file.close()

