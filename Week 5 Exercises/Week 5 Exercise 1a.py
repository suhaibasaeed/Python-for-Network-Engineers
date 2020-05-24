"""
1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password.
The function should print out each of these three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
"""
# Define function with 3 parameters which prints them to console
def ssh_con(ip_add, username, password):
    print('ip add: {}'.format(ip_add))
    print('Username: {}'.format(username))
    print('Password: {}'.format(password))

# Call function by passing positional arguments for ip_add, username and password
ssh_con('10.1.1.1', 'admin', 'C1sc0')
print('-' * 20)

# Call function by using named arguments
ssh_con(password='Jun1per', username='root', ip_add='10.1.1.1')
print('-' * 20)

# Call function by using both positional and named arguments
ssh_con('10.1.1.2', password='hello', username='bonjour')
print('-' * 20)