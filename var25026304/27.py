with open('27_B.txt') as f:
    s = [int(i) for i in f.readlines()]

k = s.pop(0)
s.pop(0)

# result = 0
# for i in range(len(s)):
#     for j in range(i + k, len(s)):
#         result = max(result, s[i] + s[j])

resultN = 0
maxN = 0

for i in range(k, len(s)):
    maxN = max(maxN, s[i - k])
    resultN = max(resultN, s[i] + maxN)
print(resultN)