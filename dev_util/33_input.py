import copy


def return_isalph(w) :
    #w = "c"
    if w.isdigit() :
        return "n"
    else :
        if w.encode().isalpha():
            return "g"
        else: 
            return "k"

while True :
    #inputs : "ghdwpaks홍제만ghdwpaks"
    inputs = input("입력 : ")
    inputs = list(inputs)
    res = []
    stamp = 0
    for i in range(1,len(inputs)) :
        if inputs[i-1] == " " and inputs[i] == " " :
            continue
        if not return_isalph(inputs[i-1]) == return_isalph(inputs[i]) :
            res.append(inputs[stamp:i])
            stamp = copy.deepcopy(i)
        elif i == len(inputs) -1 :
            res.append(inputs[stamp:i+1])
    for i in range(len(res)) :
        res[i] = "".join( res[i])
