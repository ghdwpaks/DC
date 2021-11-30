import socket
import threading
ser_HOST = '10.241.150.211'
ser_PORT = 9999

print("ser")

conn = []
def open_connection() :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ser_HOST, ser_PORT))

        s.listen(50)
        temp_conn, addr = s.accept()
        conn.append(temp_conn)

while True :
    th2 = threading.Thread(target=open_connection)
    th2.start()
    sendData = input("보내기 > ")
    if sendData == "" or sendData == None :
        sendData = " "
    for j in range(len(conn)) :
        conn[j].send(sendData.encode('utf-8'))