A, B, C, D = map(int, input().split())
ans = 'Yes'

for i in range(10000):
    C -= B
    if C <= 0:
        break
    A -= D
    if A <= 0:
        ans = 'No'
        break
print(ans)
