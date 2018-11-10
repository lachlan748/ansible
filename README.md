# ansible

This is a collection of Ansible playbooks that I've picked up along my network automation journey. 

All playbooks have been tested successfully using Ansible 2.7.1.

I've separated the playbooks into two categories:

1. Changes: when you need to automate a change across many devices in a live network. Example: add an SNMP string, edit an ACL or prefix-list, modify BGP inbound/outbound filters etc. 

2. Configuration templates: I use these for project work. When I need to create a large number of configs from scratch for a given client, I use Ansible roles with jinja2 templates. These can then be deployed via console, ZTP or whatever delivery method you prefer.

Big thanks to Michael Kashin @ networkop.co.uk. I learnt most of my automation knowledge from his blogs. 

Also thanks to the usual suspects - David Mahler, Jason Edelman, Ivan Pepelnjak and Kirk Byers.
