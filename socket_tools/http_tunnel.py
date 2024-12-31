import socket
import threading

# HTTP 隧道伺服器
def http_tunnel_server(local_host, local_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_host, local_port))
    server.listen(5)
    print(f"[SERVER] Listening on {local_host}:{local_port}")
    
    while True:
        client, addr = server.accept()
        print(f"[SERVER] Connection from {addr}")
        threading.Thread(target=handle_client, args=(client,)).start()

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"[REQUEST] {request.decode()}")
    client_socket.send(b"HTTP/1.1 200 OK\r\n\r\nTunnel Established")
    client_socket.close()

# 啟動 HTTP 隧道伺服器
http_tunnel_server("0.0.0.0", 8888)
