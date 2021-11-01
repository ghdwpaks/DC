import socket

cli_HOST = '192.168.1.74'
cli_PORT = 9999

print("cli")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((cli_HOST, cli_PORT))
while True:
    recvData = s.recv(1024).decode('utf-8')
    print(recvData)
    sendData = "ack"
    s.send(sendData.encode('utf-8'))