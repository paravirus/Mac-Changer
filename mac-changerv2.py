#!/usr/bin/env python

import subprocess
import optparse
from termcolor import colored
from pyfiglet import Figlet
#install dep
subprocess.call("pip3 install termcolor", shell=True)
subprocess.call("pip3 install pyfiglet", shell=True)

f = Figlet(font='standard')
print(colored( f.renderText('  ParaV!ru$'), "red"))

f = Figlet(font='standard')
print(colored( f.renderText('Wordlist Mod'), "green"))


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface that the MAC address will change for.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()


def change_mac(interface, new_mac):
    print(" [+] Changing the Mac address for" + interface + "to" + new_mac)
    subprocess.call([f"ifconfig {interface} down"])
    subprocess.call([f"ifconfig {interface} hw ether {new_mac}"])
    subprocess.call([f"ifconfig {interface} up"])


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
