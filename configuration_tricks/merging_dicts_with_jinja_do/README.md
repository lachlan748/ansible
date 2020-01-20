Use the jinja2 'do' extension to merge two or more dicts.

See updates to ansible.cfg file and roles/vlan/templates/vlan.j2.

In this example, I've created two dicts:
* shared_vlans
* my_vlans

I've joined both dicts to a single dict called 'combined_vlans' then sorted and iterated over them
to add into the vlan database.
