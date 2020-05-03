N = int(input())
M = int(N**0.5)
l = []
if N <= 3:
    print(1)
else:
    for a in range(1, M+1):
        if N % a == 0:
            b = int(N/a)
        else:
            continue
        l.append(max(len(str(a)), len(str(b))))
    print(min(l))
