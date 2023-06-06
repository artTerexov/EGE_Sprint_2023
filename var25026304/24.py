with open('24.txt') as f:
    s = f.readline()

c = 0
cmax = 0
for i in range(len(s) - 1):
    if not(s[i] in "NOP" and s[i + 1] in "NOP"):
        c += 1
    else:
        c += 1
        cmax = max(cmax, c)
        c = 0

print(cmax, c)

# ABCDENOHGYFHGYFYPP