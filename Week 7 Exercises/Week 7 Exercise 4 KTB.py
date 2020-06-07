"""
4. Take the YAML file and corresponding data structure that you defined in exercise3b:
{'interfaces': {
    'Ethernet1': {'mode': 'access', 'vlan': 10},
    'Ethernet2': {'mode': 'access', 'vlan': 20},
    'Ethernet3': {'mode': 'trunk',
                  'native_vlan': 1,
                  'trunk_vlans': 'all'}
    }
}

From this YAML data input source, use Jinja templating to generate the following configuration output:

interface Ethernet1
  switchport mode access
  switchport access vlan 10
interface Ethernet2
  switchport mode access
  switchport access vlan 20
interface Ethernet3
  switchport mode trunk
  switchport trunk native vlan 1
  switchport trunk allowed vlan all

The following should all be variables in your Jinja template (the names may be different than below, but they should be variabilized and not be hard-coded in your template).
interface_name
switchport_mode
access_vlan
native_vlan
trunk_vlans

All your Jinja2 variables should be retrieved from your YAML file.
"""

import yaml
import jinja2
from pprint import pprint

# Open yaml file with dictionary in it - This will be Jinja2 variables
with open('w7e3b.yml') as f:
    template_vars = yaml.safe_load(f) # Load into f variable



# Jinja2 template within python file with loop
device_template = '''
{%- for intf_name, intf_dict in interfaces.items() %}
interface {{ intf_name }}
  {%- if intf_dict.mode == 'access' %}
  switchport mode access
  switchport access vlan {{ intf_dict.vlan }}
  {%- else %}
  switchport mode trunk
  switchport trunk native vlan {{ intf_dict.native_vlan }}
  switchport trunk allowed vlan {{ intf_dict.trunk_vlans }}
  {%- endif %}
{%- endfor %}

'''

# Invoke template class on jinja2 object and pass in device template
v = jinja2.Template(device_template)

# Pass in variables via render method and print to screen
print(v.render(template_vars))




