'''
https://inspireman.tistory.com/16
'''
import os
from tkinter import Canvas, filedialog
from tkinter import messagebox

list_file = []                                          #파일 목록 담을 리스트 생성
i = 0
while True :
    
    while True :
        files = filedialog.askopenfilenames(initialdir="/",
                        title = "파일을 선택 해 주세요",
                        #filetypes = (("*.xlsx","*xlsx"),("*.xls","*xls"),("*.csv","*csv"))
        )

        if files == '':
            messagebox.showwarning("경고", "파일을 추가 하세요")    #파일 선택 안했을 때 메세지 출력
            continue
        else :
            break

    #files 변수에 선택 파일 경로 넣기
    print("files :",files)
    print("type(files) :",type(files))
    print(files[0].split('/')[-1],"를 고르셨습니다. 또 고르시겠습니까?")
    cannotpass = True
    while True :
        userans_1_exit = input("입력(y/n) >")
        if userans_1_exit == "y" :
            cannotpass = False
            break
        elif userans_1_exit == "n" :
            cannotpass = True
            break
        else :
            print("입력을 정상적으로 해주세요")
            continue
    if cannotpass :
        break
    else :
        continue
        i += 1
        
            

print(files)    #files 리스트 값 출력