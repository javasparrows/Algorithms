from collections import Counter
S = [s for s in input()]
N = len(S)

l = Counter(S)
l = list(l.values())

odd = [s for s in l if s % 2 == 1]

k = len(odd)

if k == 0:
    print(N)
else:
    print(2 * ((N-k)//(2*k)) + 1)
