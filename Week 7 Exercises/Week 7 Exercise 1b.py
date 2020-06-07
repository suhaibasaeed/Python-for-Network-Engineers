"""
1b. Using a conditional in a Jinja2 template, generate the following output:
crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic

The encryption of aes, and the Diffie-Hellman group should be variables in the template.

Additionally this entire ISAKMP section should only be added if the isakmp_enable variable is set to True.

Your template should be inside your Python program for simplicity.
"""

import jinja2

# Dictonary for variables
ipsec_vars = { 'encryp_type': 'aes',
              'dh_group': 5,
              'isakmp_enable': True,
}

# Jinja2 template within python file with if statement including isamkmp config it var set to True
ipsec_template = '''

{% if isakmp_enable -%}
crypto isakmp policy 10
 encr {{encryp_type}}
 authentication pre-share
 group {{dh_group}}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{% endif %}
'''

# Invoke template class on jinja2 object and pass in ipsec template
v = jinja2.Template(ipsec_template)

# Pass in variables via render method and print to screen
print(v.render(ipsec_vars))
