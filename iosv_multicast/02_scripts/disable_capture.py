from datetime import datetime
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException, NetMikoTimeoutException
from jinja2 import Environment, PackageLoader, FileSystemLoader
from pprint import pprint
import concurrent.futures
import getpass
import os
import re
import shutil

# Get login credentials
tacacs_username = input("Enter username: ") 
tacacs_password = getpass.getpass(prompt = "Enter password: ")

# Read the ansible hosts.yml file and extract host info using regex:
def process_hosts():
    # create a top level empty dict which we'll populate with host data
    master = {}
    with open('./hosts.yml') as f:
        # read the entire file as a string
        contents = f.read()
        # perform a regex match to grab host info
        match = re.findall(r'(\S+):\n\s+ansible_host:\s(\S+)\n\s+ansible_network_os:\s(\S+)', contents, re.DOTALL)
        # findall returns a list, process each item in the list
        for line in match:
            # create a dict per line (host)
            data = {}
            # grab name, ip, os from items in the line
            node_name = line[0]
            node_os = line[2]
            # clean node_os
            if node_os == 'eos':
                node_os = 'arista_eos'
            elif node_os == 'nxos':
                node_os = 'cisco_nxos'
            elif node_os == 'ios':
                node_os = 'cisco_ios'
            elif node_os == 'asa':
                node_os = 'cisco_asa'
            # populate data dict with details required by netmiko
            data['ip'] = line[1]
            data['device_type'] = node_os
            data['port'] = '22'
            data['username'] = tacacs_username
            data['password'] = tacacs_password
            master[node_name] = data
    return master

def run_commands(device_data):
    # Send a command to all devices using a for loop:
    try:
        netconnect = ConnectHandler(**device_data)
        netconnect.enable()
        # define an empty dictionary which will store the output for each 'show' command, per device
        data = {}
        commands = ["monitor capture point stop point0",
                    "monitor capture point stop point1",
                    "monitor capture point stop point2",
                    "monitor capture point stop point3",
                   ]
        # connect to each device and run each 'show' command
        for command in commands:
            data[command] = netconnect.send_command(command)
        # copy the populated 'data' dictionary into the master dicionary
        device_data.setdefault('outputs', data)
    except NetMikoAuthenticationException:
        print("\n" + f"{device} SSH login failed, authentication error.")
    except NetMikoTimeoutException:
        print("\n" + f"{device} SSH login failed due to timeout.")
    except Exception as exc:
        print("\n" + f"{device} Some other exception: { exc }")

def main(master):
    start_time = datetime.now()
    with concurrent.futures.ThreadPoolExecutor(15) as executor:
        futures = {}
        for device, device_data in master.items():
            print(f"Stopping capture on {device}..." + "\n")
            futures[executor.submit(run_commands, device_data)] = device

    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    data = process_hosts()
    main(data)
