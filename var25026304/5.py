for N in range(4, 100):
    n = bin(N)[2:]
    if N % 3 == 0:
        n = n + n[-3:]
    else:
        n = n + bin(N % 3 * 3)[2:]
    R = int(n, 2)
    if R < 76:
        print(N)