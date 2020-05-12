"""
3.  Read in the 'show_version.txt' file.
From this file, use regular expressions to extract the OS version, serial number, and configuration register values.

Your output should look as follows:
OS Version: 15.4(2)T1
Serial Number: FTX0000038X
​Config Register: 0x2102
"""

import re

# Open the file and put it in the f variable
with open("show_version.txt") as f:
    output = f.read() # read in as string

# Match on IOS version in output string using RE. Set re.M flag so each line treated separately. Print match to console
os_ver = re.search(r"^Cisco IOS Software,.*, Version (\S+),.*$", output, flags=re.M).group(1)
print("{:>20}: {:15}".format("OS Version", os_ver))

# match on serial no in output string using RE. Print to console
serial_no = re.search(r"^Processor board ID (\S+)$", output, flags=re.M).group(1)
print("{:>20}: {:15}".format("Serial Number", serial_no))

# Match on config register in output string using RE. Print to console
conf_reg = re.search(r"^Configuration register is (\S+)$", output, flags=re.M).group(1)
print("{:>20}: {:15}".format("Config Register", conf_reg))
