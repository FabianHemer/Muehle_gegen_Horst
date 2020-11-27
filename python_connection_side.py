import socket

host = "127.0.0.1"
port = 25001
data = "0,0,0"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((host, port))
    sock.sendall(data.encode("utf-8"))
    data = sock.recv(1024).decode("utf-8")
    print(data)

finally:
    # close always socket
    sock.close()