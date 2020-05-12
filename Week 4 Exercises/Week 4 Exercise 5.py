"""5. Read the 'show_ipv6_intf.txt' file.

From this file, use Python regular expressions to extract the two IPv6 addresses.

The two relevant IPv6 addresses you need to extract are:
    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64

Try to use re.DOTALL flag as part of your search.
Your search pattern should not include any of the literal characters in the IPv6 address.

From this, create a list of IPv6 addresses that includes only the above two addresses.

Print this list to the screen."""

import re

ipv6_list = []

# Open file and put it into the f variable as one big string

with open("show_ipv6_intf.txt") as f:
    output = f.read()

# Use RE to extract the first IPv6 address in the file
ipv6_ip = re.search(r"IPv6 address:\s+ (\S+)", output, flags=re.DOTALL).group(1)

# Use RE to extract the 2nd IPv6 address in the file
ipv6_ip2 = re.search(r"]\s+ (\S+)", output, flags=re.DOTALL).group(1)

# Append both extracted IPV6 addresses to the list and print to console
ipv6_list.append(ipv6_ip)
ipv6_list.append(ipv6_ip2)
print(ipv6_list)