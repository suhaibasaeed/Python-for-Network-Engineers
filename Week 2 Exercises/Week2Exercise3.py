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

