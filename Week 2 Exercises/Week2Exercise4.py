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


