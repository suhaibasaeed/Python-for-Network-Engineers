"""
1. Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable.
Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).
Close the file.
Open the file a second time using a Python context manager (with statement).
Read in the file contents using the .readlines() method. Print out the file contents to the screen.
Also print out the type of the variable (you should have a list at this point).
"""
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
