"""
1a. Import the 'datetime' library. Print out the module that is being imported by datetime (the __file__ attribute)

Import the Python ipaddress library. Print out the module that is being imported by ipaddress (the __file__ attribute).

If you are using Python 2.7, you will need to pip install the ipaddress library.

Import sys and use pprint to pprint sys.path
"""

import datetime
import ipaddress
import sys
from pprint import pprint

# Print out module being imported by datetime library
print(datetime.__file__)
print()
# Print out module being imported by ipaddress library
print(ipaddress.__file__)
print()

# use pprint to print sys.path to the console
pprint(sys.path)

