"""Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

​ $ python exercise2.py
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column.
"""

ip_add = (input('Please enter an IP address: '))
octet = ip_add.split('.')

octet_1 = 'Octet1'
octet_2 = 'Octet2'
octet_3 = 'Octet3'
octet_4 = 'Octet4'

int_oct1 = int(octet[0])
bin_oct1 = bin(int_oct1)
hex_oct1 = hex(int_oct1)

int_oct2 = int(octet[1])
bin_oct2 = bin(int_oct2)
hex_oct2 = hex(int_oct2)

int_oct3 = int(octet[2])
bin_oct3 = bin(int_oct3)
hex_oct3 = hex(int_oct3)

int_oct4 = int(octet[3])
bin_oct4 = bin(int_oct4)
hex_oct4 = hex(int_oct4)




print('\n')
print(f'{octet_1:^15} {octet_2:^15} {octet_3:^15} {octet_4:^15}')
print('-' * 80)
print('{:^15}{:^15}{:^15}{:^15}'.format(*octet))
print(f'{bin_oct1:^15} {bin_oct2:^15} {bin_oct3:^15} {bin_oct4:^15}')
print(f'{hex_oct1:^15} {hex_oct2:^15} {hex_oct3:^15} {hex_oct4:^15}')
print('-' * 80)
print('\n')