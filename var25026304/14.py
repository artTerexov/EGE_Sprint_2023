for x in '0123456789ABCDE':
    num_1 = int('99658' + x + '29', 15)
    num_2 = int('102' + x + '023', 15)
    if (num_1 + num_2) % 14 == 0:
        print(x, (num_1 + num_2) // 14)


for x in range(15):
    num_1 = 9 * 15 ** 0 + 2 * 15 ** 1 + x * 15 ** 2 + 8 * 15 ** 3 + 5 * 15 ** 4 + 6 * 15 ** 5 + 9 * 15 ** 6 + 9 * 15 ** 7
    num_2 = 3 * 15 ** 0 + 2 * 15 ** 1 + 0 * 15 ** 2 + x * 15 ** 3 + 2 * 15 ** 4 + 0 * 15 ** 5 + 1 * 15 ** 6
    if (num_1 + num_2) % 14 == 0:
        print(x, (num_1 + num_2) // 14)