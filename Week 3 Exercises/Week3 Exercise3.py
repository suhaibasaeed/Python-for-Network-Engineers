"""Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the lines until you have encountered the remote "System Name" and remote "Port id".
 Save these two items into variables and print them to the screen.  You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15').
 Break out of your loop once you have retrieved these two items."""

# Initialise variables and booleans to be be used
port_id = None
system_name = None
found_port, found_sys = (False, False)
# Open file and read it in one line at a time
with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.readlines()
# Loop through lines in the file
for line in show_lldp:
    # Look for the line that starts with port ID and split it into a list extracting the value & change bool to True
    if line.startswith('Port id'):
        fields = line.split() # Can also split on port ID and equate port_id to that
        port_id = fields[2]
        found_port = True
    # Look for line in file that starts with System Name and split it, extracting the value
    elif line.startswith('System Name'):
        fields = line.split() # Can also split on System name and equal system_name to that
        system_name = fields[2]
        found_sys = True

    # Break out of loop if found both
    if found_sys and found_port == True:
        print('Found Port ID and System Name, exiting')
        break
print()
print('Port ID: {}'.format(port_id))
print('System Name: {}'.format(system_name))


