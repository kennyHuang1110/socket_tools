from scapy.all import *

# 目標 IP
target_ip = "192.168.1.1"
# 偽裝來源 IP
fake_ip = "10.0.0.1"

# 構建並發送封包
packet = IP(src=fake_ip, dst=target_ip) / ICMP()
send(packet)

print(f"Sent fake packet from {fake_ip} to {target_ip}")
