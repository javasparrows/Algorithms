import itertools

N = int(input())
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]

P_dict = itertools.permutations(sorted(P), N)
P_dict = [i for i in list(P_dict)]
Q_dict = itertools.permutations(sorted(Q), N)
Q_dict = [i for i in list(Q_dict)]

ans = 0
for i in range(len(P_dict)):
    if list(P_dict[i]) == P:
        ans += (i+1)
    if list(Q_dict[i]) == Q:
        ans -= (i+1)

print(ans if ans >= 0 else -ans)
