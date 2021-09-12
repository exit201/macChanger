#!/usr/bin/env python
import subprocess
from optparse import OptionParser


# write the function
def get_arguments():
    # parsing Help option
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to Change The MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC Address")
    (option, argument) = parser.parse_args()
    # if option.interface == '':
    #     parser.error("[+] interface Must An Argument")
    if not option.interface:
        parser.error("[+] Please Check the Detail About --help")
    if option.interface or option.new_mac == "":
        parser.error("[+] You Have to input Both (interface And New Mac)\n"
                     "[+] Please Check the Detail About --help")
    elif not option.new_mac:
        parser.error("[+] Please Check the Detail About --help")
    return option


# write the function
def change_mac(interface, new_mac):
    print("Your Interface is ", interface, " and MAC Address is ", new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])
    print("[+]Mac Change successfully")


# calling the function
option = get_arguments()
change_mac(option.interface, option.new_mac)
