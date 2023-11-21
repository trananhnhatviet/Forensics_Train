from scapy.all import *


out = ""

packets = rdpcap('bus.pcap')

for packet in packets:
    if packet.haslayer(TCP):
        tcp_packet = packet.getlayer(TCP)
        if tcp_packet.sport == 502:
            if tcp_packet.haslayer(Raw):
                data = (tcp_packet[Raw].load)[-2:]
                if (data == b'\xff\x00'):
                    out += "1"
                else:
                    out += "0"
print(out)