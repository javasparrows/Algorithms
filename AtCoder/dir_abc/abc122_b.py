S = input()
a = 'ACGT'
memo = []
cnt = 0
for s in S:
    if s in a:
        cnt += 1
    else:
        cnt = 0
    memo.append(cnt)
print(max(memo))
