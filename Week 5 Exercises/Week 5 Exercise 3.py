"""
3. Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.

It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should return the normalized MAC address

Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
"""
import re
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

# Call function with different test MAC address to be formatted
normal_mac('0000.aaaa.bbbb')
normal_mac('00-00-aa-aa-bb-bb')
normal_mac('a:b:c:d:e:f')


