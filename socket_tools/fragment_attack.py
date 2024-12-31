from scapy.all import *

# 目標 IP
target_ip = "192.168.1.1"
# 構建原始資料
payload = "A" * 2000  # 大於 MTU 的資料量

# 分段封包
fragments = fragment(IP(dst=target_ip) / payload)

# 發送分段封包
for fragment in fragments:
    send(fragment)
    print(f"Sent fragment: {fragment.summary()}")
