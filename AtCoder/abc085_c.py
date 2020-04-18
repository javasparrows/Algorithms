n, sum_ = [int(i) for i in input().split()]
ok = False
for i in range(n+1):
    for j in range(n-i+1):
        k = n-i-j
        s = i*10000 + j*5000 + k*1000
        if s == sum_:
            print(i, j, k)
            ok = True
            break
    if ok == True:
        break

if ok == False:
    print(-1, -1, -1)
