"""
2.  Create a function that randomly generates an IP address for a network.
The default base network should be '10.10.10.'. For simplicity the network will always be a /24.

You should be able to pass a different base network into your function as an argument.

Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

You can use the following to randomly generate the last octet:
import random
random.randint(1, 254)

Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.

For each function call print the returned IP address to the screen.

"""

import random

# Create function that will randomly generate IP from a /24 subnet. Single parameter being base network
def random_ip(base='10.10.10.'):
    base_network = base.split('.') # Split the base network on the full stop character, resulting in list

    last_octet = str(random.randint(1,254)) # Generate a rand number for last octet and turn it into string

    base_network.pop() # Remove null string from end of list to avoid future problems
    base_network.append(last_octet) # Append the randomly generated number to list
    new_rand_ip = '.'.join(base_network) # Join list back together and reenter '.' to separate octets
    print(new_rand_ip) # Print new random IP to console

# Call the function with no arguments
random_ip()

# Call the function with positional argument
random_ip('192.168.1.')

# Call the function with named argument
random_ip(base='172.16.16.')


