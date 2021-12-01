import socket
import threading
ser_HOST = '127.0.0.1'
ser_PORT = 9999

print("ser")

conn = []
def open_connection() :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ser_HOST, ser_PORT))

        s.listen(50)
        temp_conn, addr = s.accept()
        print("\n"+str(addr)+"연결됨.",end="\n보내기 >")
        
        conn.append([temp_conn,addr])

def exit_realy(sendData) :
    
    if sendData == "exit" or sendData == "ㄷ턋" :
        while True :
            print("정말로 연결을 종료하시겠습니까?(y/n)")
            exit_confirm = input("입력 :")
            if exit_confirm == "y" or exit_confirm == "Y" :
                print("서버 제공을 중단합니다.")
                return False
            elif exit_confirm == "n" or exit_confirm == "N" :
                print("서버 제공 중단을 취소합니다.")
                return True
            else :
                print("y 또는 n 중에 하나만 입력해주세요.")
                continue 

    else :
        return True       

not_exit = True
while not_exit :
    del_count = []
    th2 = threading.Thread(target=open_connection)
    th2.start()
    sendData = input("보내기 >")
    if sendData == "" or sendData == None :
        sendData = " "
    not_exit = exit_realy(sendData)
    for j in range(len(conn)) :
        try :
            conn[j][0].send(sendData.encode('utf-8'))
        except :
            print(conn[j][1],"와의 연결이 끊겼습니다.")
            del_count.append(j)
            continue
    for j in range(len(del_count)) :
        del conn[del_count[j]-j]