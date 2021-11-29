octets = [1,1,1,1]

for i in range(len(octets)) :
    
    while True :
        if octets[i] > 255 :
            break
        cli_HOST = ""
        for j in range(len(octets)) :
            cli_HOST += str(octets[j])
            if not j == len(octets)-1 :
                cli_HOST += "."
        print("cli_HOST :",cli_HOST)
        octets[i]+=1