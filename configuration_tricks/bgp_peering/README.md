This folder creates a L3 leaf and spine topology. For illustration purposes, I included:

1. eBGP between spine and leaf including peer groups
2. iBGP between each spine and leaf pair. 
3. IGP (OSPF) to exchange Loopback routes between iBGP peers
4. Leaf switches contain isolated L3 SVI's which are advertised using BGP

Run site.yml to execute.

Note: you must have the 'ipaddr' filter installed on your ansible controller. 

Also note: I have used /30 for point to point interfaces because the ipaddr module doesn't support /31 (RFC 3021). There's a work-around for that but i'll include it in a later playbook. 

See: https://docs.ansible.com/ansible/2.5/user_guide/playbooks_filters_ipaddr.html for install instructions. 
