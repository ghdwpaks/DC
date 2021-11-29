from multiprocessing import Process, Queue

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result = Queue()
    th = []
    th.append(Process(target=work, args=(1, START, END//2, result)))
    th.append(Process(target=work, args=(2, END//2, END, result)))
    for i in range(len(th)) :
        th[i].start()
    for j in range(len(th)) :
        th[i].join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    print(f"Result: {total}")