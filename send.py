from scapy.all import *


ip = IP(dst="192.168.0.1")  
udp = UDP(dport=12345, sport=54321)  
data = "HELLO, WORLD :)"  


packet = ip / udp / data
send(packet)

