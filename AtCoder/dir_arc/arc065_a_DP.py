# 動的計画法 (Dynamic Programming) での解法

S = input()
words = ['dream', 'dreamer', 'erase', 'eraser']

dp = [0] * (len(S)+1)
dp[0] = 1
done = 'NO'

for i in range(len(S)):
    if not dp[i]:
        continue
    for w in words:
        if S[i:i+len(w)] == w:
            dp[i+len(w)] = 1

    if dp[len(S)]:
        done = 'YES'
        break

print(done)
