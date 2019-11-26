This playbook creates 5x CSR1000v configs for my home lab. 

The playbook is has several parts including:
** Create a staging folder to store config snippets (modules)
** Create a final 'complete' folder to final config files
** Execute ansible roles to build config snippets, dump to staging folder per node
** Assemble/concatenate config snippets into a single file, dump to complete folder
** Push completed config files to nodes.

See homelab.pdf diagram for topology.
