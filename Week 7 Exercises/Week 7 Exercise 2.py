"""
2. Using Python and Jinja2 templating generate the following OSPF configuration:
interface vlan 1
   ip ospf priority 100

router ospf 10
   passive-interface default
   no passive-interface Vlan1
   no passive-interface Vlan2
   network 10.10.10.0/24 area 0.0.0.0
   network 10.10.20.0/24 area 0.0.0.0
   network 10.10.30.0/24 area 0.0.0.0
   max-lsa 12000

The following items should be variables in your Jinja2 template:
​ospf_process_id
ospf_priority
ospf_active_interfaces (i.e. the non-passive interfaces)
ospf_area0_networks (the three networks that are specified as belonging to area0)

Your template should be in an external file.

Your template should also use a conditional to control whether this is output or not:
interface vlan 1
   ip ospf priority 100

If the 'ospf_priority variable is defined', then include that section.
If 'ospf_priority' is not defined then only include the 'router ospf 10' section.
"""

import jinja2

# List of passive interfaces and networks
pass_int_list = ['Vlan1', 'Vlan2']
network_list = ['network 10.10.10.0/24', 'network 10.10.20.0/24', 'network 10.10.30.0/24']

# Dictonary for variables
ospf_vars = {'ospf_process_id': 10,
             'ospf_priority': 100,
             'ospf_active_interfaces': pass_int_list,
             'ospf_area0_networks': network_list
             }

# Open template and read in as one big string
with open('w7e2.j2') as f:
    ospf_template = f.read()

# Invoke template class on jinja2 object and pass in ospf template
v = jinja2.Template(ospf_template)

# Pass in variables via render method and print to screen
print(v.render(ospf_vars))
