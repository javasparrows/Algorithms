S = input()
mod_bucket = [0] * 2019
mod_bucket[0] = 1
 
_S = S[::-1]
mod = 0
p = 1
for i in range(len(S)):
    print(p, int(_S[i]), mod, (p * int(_S[i]) + mod))
    mod = (p * int(_S[i]) + mod) % 2019
    mod_bucket[mod] += 1
    p = p*10%2019

# mod = 2の数を数える
ans = sum([mod*(mod-1)/2 for mod in mod_bucket])
print(int(ans))