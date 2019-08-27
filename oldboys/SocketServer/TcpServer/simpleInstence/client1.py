import socket

client = socket.socket()
client.connect(('localhost',9999))

while True:
    msg = input(">>").strip()
    if len(msg) == 0:continue
    client.send(msg.encode("utf-8"))
    data = client.recv(10240)
    print("recv:",data.decode())

client.close()