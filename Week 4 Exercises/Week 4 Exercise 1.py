"""
Create a dictionary representing a network device. The dictionary should have key-value pairs representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'.
If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'.
The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.

"""
# Create dictionary which represents network device
device = {'ip_add': '192.168.1.1',
          'vendor': 'cisco',
          'username': 'admin',
          'password': 'C1sc0'}
# Print IP address to console
print(device['ip_add'])
print()
# add new key value pair to dictionary depending if the vendor is Cisco or Juniper
if device['vendor'] == 'cisco':
    device['platform'] = 'IOS'
elif device['vendor'] == 'juniper':
    device['platform'] = 'junos'
# Create 2nd dictionary
bgp_fields = {'bgp_as':'65495',
              'peer_as': '65390',
              'peer_ip': '150.1.1.1'}

# Update device dict with values from bgp_fields dict. If key not present add it to device dict.
device.update(bgp_fields)

# loop over and print out dictionary keys
for key in device:
    print(key)

# loop over and print out dictionary keys and values simultaneously
for key, value in device.items():
    print(('-' * 80))
    print("{key:>15} ---> {value:>15}".format(key=key, value=value))
    print('-' * 80)



