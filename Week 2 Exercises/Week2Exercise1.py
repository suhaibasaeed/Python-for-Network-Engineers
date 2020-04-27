# Open the file
show_ver = open("show_ver.txt")
# Read file into string in one go
output = show_ver.read()
# Print to console
print(output)
# Print type
print(type(output))
print('\n')
# Close the file
show_ver.close()

# Open file 2nd time with context manager
with open("show_ver.txt") as show_ver:
    # Read file in one line at a time but put into list
    list_output = show_ver.readlines()
    # Print to console
    print(list_output)
    print('\n')
    # Prove output is list by printing type to console
    print(type(list_output))
