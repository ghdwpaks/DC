import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("pwnbit.kr",443))
print("내부 ip :",sock.getsockname()[0])


