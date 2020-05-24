"""
4. Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside of your function (i.e. where you have your function calls).

Inside of pdb, experiment with:
Listing your code.
Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step.
Experiment with 'up' and 'down' to move up and down the code stack.
Use p <variable> to inspect a variable.
Set a breakpoint and run your code to the breakpoint.
Use '!command' to change a variable (for example !new_mac = [])
"""
import re
import pdb

# Create function that will normalise MAC addresses. Takes one parameter, the MAC address
def normal_mac(mac_address):
    list_mac = re.split(':|\.|-', mac_address) # Split on ':' or '-' or '.'
    short_mac = [i.rjust(2,'0') for i in list_mac] # Use list comprehension & rjust method to pad 0 to single char byte
    mac = ''.join(short_mac) # Join list back together
    upper_mac = mac.upper() # Change lowercase characters to uppercase
    split_mac = re.findall('..?', upper_mac) # Split mac into 6 equal parts
    final_mac = ':'.join(split_mac) # Join list back together with ':'

    # Print MAC address to console
    print(final_mac)
# Start python debugger
pdb.set_trace()
# Call function with different test MAC address to be formatted
normal_mac('0000.aaaa.bbbb')
normal_mac('00-00-aa-aa-bb-bb')
normal_mac('a:b:c:d:e:f')


