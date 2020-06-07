"""
1a. Use Jinja2 templating to render the following:
vlan
   name

Your template should be inside of your Python program for simplicity.

The output from processing your template should be as follows. This should be printed to stdout.
vlan 400
   name red400
"""


import jinja2

# Dictonary for variables
vlan_vars = { 'vlan_no': 400,
              'vlan_name': 'red400'
}

# Jinja2 template within python file
vlan_template = '''

vlan {{vlan_no}}
    name {{vlan_name}}
'''

# Invoke template class on jinja2 object and pass in vlan template
v = jinja2.Template(vlan_template)

# Pass in variables via render method and print to screen
print(v.render(vlan_vars))