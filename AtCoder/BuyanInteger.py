A, B, X = list(map(int, input().split()))

def d(n):
    return len(str(n))

high = 10**9 + 1
low = 0
while high - low > 1:
    mid = (high + low)//2
    a = A*mid + B*d(mid)
    if a > X:
        high = mid
    else:
        low = mid

print(low)
