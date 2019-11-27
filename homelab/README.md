This playbook creates 5x CSR1000v configs for my home lab. 

The playbook has several parts including:
1. Create a staging folder to store config snippets (modules)
2. Create a final 'complete' folder to final config files
3. Execute ansible roles to build config snippets, dump to staging folder per node
4. Concatenate config snippets into a single file, dump to complete folder
5. Push completed config files to nodes.

![Image of topology](https://github.com/lachlan748/ansible/blob/master/homelab/homelab.png)
