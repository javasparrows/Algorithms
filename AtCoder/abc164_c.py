import numpy as np
N = int(input())
S = []
for i in range(N):
    S.append(input())
print(np.unique(S).size)