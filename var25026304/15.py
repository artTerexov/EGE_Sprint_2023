for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        if (((x & 52 != 0) and (x & 36 == 0)) <= (not (x & A == 0))) == 0:
            flag = False
            break
    if flag:
        print(A)
        break
