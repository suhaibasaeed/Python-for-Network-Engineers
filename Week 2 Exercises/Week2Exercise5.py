# Open file
show_bgp = open("show_ip_bgp_summ.txt")
# Read file in one go as one big string
output = show_bgp.read()
# Split the lines into a list
output = output.splitlines()
# Put first and last line into separate variables
first_line = output[0]
last_line = output[-1]
# Invoke split method on both variables to put them in another list
first_line = first_line.split()
last_line = last_line.split()
# Print Local BGP AS no and peer IP address to console
print("The local AS number is: {}".format(first_line[-1]))
print("The BGP peer IP address is: {}".format(last_line[0]))