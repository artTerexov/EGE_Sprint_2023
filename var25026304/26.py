with open('26.txt') as f:
    s = [[int(j) for j in i.split()]for i in f.readlines()]

k = s.pop(0)[0]
s.pop(0)

s.sort()

buff = [0] * k
c = 0
num = 0
for p in s:
    for i in range(len(buff)):
        if p[0] > buff[i]:
            buff[i] = p[1]
            c += 1
            num = i
            break

print(c, num + 1)