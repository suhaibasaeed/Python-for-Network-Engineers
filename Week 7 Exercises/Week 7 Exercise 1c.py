"""
1c. Using Jinja2 templating and a for-loop inside the template, generate a configuration snippet:

Your template should be inside your Python program for simplicity.

It is fine for your VLAN IDs to be out of order in the generated configuration
(for example, VLAN ID 508 can come before VLAN ID 504).
"""

import jinja2

vlan_list = [501, 502, 503, 504, 505, 506, 507, 508]

# Dictonary for variables
vlans_vars = { 'vlan_no': vlan_list,
}

# Jinja2 template within python file with loop
vlans_template = '''
{%- for vlan in vlan_no %}
vlan {{vlan}}
    name blue{{vlan}}
{%- endfor %}
'''

# Invoke template class on jinja2 object and pass in vlan template
v = jinja2.Template(vlans_template)

# Pass in variables via render method and print to screen
print(v.render(vlans_vars))