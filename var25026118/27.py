with open('27B.txt') as f:
    s = [int(i) for i in f.readlines()]

N = s.pop(0)
K = s.pop(0)

maxResult = 0

max_1 = max_2 = 0

inx_1 = inx_2 = 0

for i in range(len(s) - 2 * K):
    if inx_1 - i < K:
        max_1 = max(s[i + K: -K])
        inx_1 = s.index(max_1, i + K)
        max_2 = max(s[inx_1 + K:])
    maxResult = max(maxResult, s[i] + max_1 + max_2)

s = s[::-1]

max_1 = max_2 = 0

inx_1 = inx_2 = 0
for i in range(len(s) - 2 * K):
    if inx_1 - i < K:
        max_1 = max(s[i + K: -K])
        inx_1 = s.index(max_1, i + K)
        max_2 = max(s[inx_1 + K:])
    maxResult = max(maxResult, s[i] + max_1 + max_2)

print(maxResult)

# 11655285 329810315375
# 11655285 329810315375