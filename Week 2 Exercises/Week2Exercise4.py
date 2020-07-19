"""
4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

Obtain the list entry associated with the FastEthernet4 interface.
You can just hard-code the index at this point since we haven't covered for-loops or regular expressions.
Use the string .split() method to obtain both the IP address and the corresponding interface associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero.
You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt).
Alternatively, you can type 'python -m pip install pycodestyle'.
"""

# Open file
sh_int = open("sh_ip_int_brief.txt")
# Put file in line by line into list
output = sh_int.readlines()
# Put list entry for Fa0/4 into variable
fa_0_4 = output[4]
# Use split method to obtain IP address and int
fa_0_4 = fa_0_4.split()
# create 2 variables that will hold interface number and IP address
intf_name = fa_0_4[0]
ip_address = fa_0_4[1]
# Create tuple called my_tuple
my_tuple = (intf_name, ip_address)
# Print tuple to console
print(my_tuple)


