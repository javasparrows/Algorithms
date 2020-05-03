s = input()
n = len(s)
ans = 0

for i in range(2**(n-1)):
    f = s[0]
    
    for j in range(n-1):
        if i>>j & 1:
            f += '+'
        f += s[j+1]
        
    ans += eval(f)
    
print(ans)