#!/usr/bin/env python

import subprocess
import optparse


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
