with open('17.txt') as f:
    s = [int(i) for i in f.readlines()]

minimum = max(s) * 2
result = []
for i in s:
    if len(str(i)) == 3 and str(i)[-1] == '5':
        minimum = min(minimum, i)

for i in range(len(s) - 1):
    if (len(str(s[i])) == 3 or len(str(s[i + 1])) == 3) and (s[i] + s[i + 1]) % minimum == 0:
        result.append(s[i] + s[i + 1])

print(len(result), max(result))