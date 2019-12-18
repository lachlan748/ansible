This playbook creates 6x CSR1000v template configs for my home lab. 

The topology includes all interface config plus a flat OSPF area 0 control-plane.

No multicast or BGP is included. 

Note: the template configuration is pushed to each device via napalm-ansible. Ensure you have this package installed.

![Image of topology](https://github.com/lachlan748/ansible/blob/master/homelab/001_base_templates/homelab.png)
