import copy
def get_ans_yes_or_no_or_another(ans="no") :
    if "dd"  in ans or "d" in ans or "y" in ans or "ㅛ" in ans or "1" in ans or "yes" in ans or "YES" in ans or "DD" in ans or "D" in ans or "Y" in ans or '응' in ans or '어' in ans or '네' in ans or '예' in ans:
        return True
    elif 's' in ans or 'ss'  in ans or 'SS' in ans or 'S' in ans or 'NO' in ans or 'no' in ans or 'n' in ans or 'N' in ans or '0'  in ans or '아니'  in ans or 'ㄴㄴ' in ans or 'ㄴ' in ans or '아니오' in ans or '아니요' in ans or " "in ans or ans == '' or ans == None:
        return False
    else :
        return 2

cli_HOST = ""
keep_lv1 = True
while keep_lv1 :
    user_ans2 = input("접속 대상의 아이피를 입력해주세요 (미입력시 송신대기):")
    if get_ans_yes_or_no_or_another(user_ans2) == False :
        print("송신대기를 시작합니다.")
        keep_lv1 = False
    else :
        while True :
            user_ans3 = input(str(user_ans2)+"와 연결하시겠습니까?(y/n) :")
            if user_ans3 == "y" :
                print(user_ans2,"와의 연결확정이 확인됐습니다.")
                keep_lv1 = False
                break
            elif user_ans3 == "n":
                print(user_ans2,"와의 연결 취소가 확인됐습니다.")
                break
            else :
                print("y 또는 n 만 입력해주세요.\ny는 승인이며 n은 취소입니다.")
                continue

cli_HOST = 0
keep_lv1 = True
while keep_lv1 :
    user_ans2 = input("접속을 받을 포트를 입력해주세요 :")
    if get_ans_yes_or_no_or_another(user_ans2) == False :
        print("다시 입력해주세요.")
        continue
    else :
        while True :
            user_ans3 = input(str(user_ans2)+"로 연결하시겠습니까?(y/n) :")
            if user_ans3 == "y" :
                print(user_ans2,"와의 연결확정이 확인됐습니다.")
                cli_PORT = copy.deepcopy(user_ans2)
                keep_lv1 = False
                break
            elif user_ans3 == "n":
                print(user_ans2,"와의 연결 취소가 확인됐습니다.")
                break
            else :
                print("y 또는 n 만 입력해주세요.\ny는 승인이며 n은 취소입니다.")
                continue