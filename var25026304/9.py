with open('9') as f:
    s = [[int(j) for j in i.split()] for i in f.readlines()]

count = 0
for i in s:
    if len(set(i)) == 5 and 3 * (min(i) + max(i)) >= 2 * (sum(i) - min(i) - max(i)):
        count += 1

print(count)