from scapy.all import *

def process_packet(packet):
    result = ""
    if packet.haslayer(TCP):
        tcp_packet = packet.getlayer(TCP)
        if tcp_packet.haslayer(Raw):
            data = packet.getlayer(TCP)[Raw].load
            try:
                data = data.decode()
                result += data
            except UnicodeDecodeError:
                pass
    return result

packets = rdpcap('test_2.pcap')

flag = ""
for packet in packets:
    flag += (process_packet(packet))
print(flag.replace("\n",""))

# KCSC{SYN_Fl0od_1S_t0O_dangerous}