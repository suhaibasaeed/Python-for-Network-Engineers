'''Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have found both of these devices, 'break' out of the for loop.'''

found_arista = False
found_dg = False

# Open file and read it in one line at a time
with open("show_arp.txt") as f:
    show_arp = f.readlines()

# Loop through lines in the file putting each in list element
for line in show_arp:
    # Ignore the top header line
    if line.startswith('P'):
        continue
    # Turn each line of file from string to list, split on whitespace
    fields = line.split()
    ip_addr = fields[1]
    mac_addr = fields[3]
    # If the IP is found print it to console with corresponding mac address and change bool to True
    if ip_addr == '10.220.88.1':
        print('Default Gateway IP/Mac:   {} / {}'.format(ip_addr, mac_addr))
        found_dg = True
    elif ip_addr == '10.220.88.30':
        print('Arista 3 IP/Mac: {} / {}'.format(ip_addr, mac_addr))
        found_arista = True

    # If both bools are true then break out of loop and print confirmation to console
    if found_dg and found_arista == True:
        print('Broke out of loop')
        break
