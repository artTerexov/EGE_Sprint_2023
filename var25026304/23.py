def calc(num, flag):
    if num == 17 and flag == 1:
        return 1
    if num > 17:
        return 0
    if num == 9:
        flag += 1
    if num == 12:
        return 0
    return calc(num + 1, flag) + calc(num + 2, flag) + calc(num * 2, flag)


print(calc(2, 0))