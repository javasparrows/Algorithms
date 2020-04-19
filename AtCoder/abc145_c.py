import itertools

N = int(input())
X = []
for i in range(N):
    X.append([int(j) for j in input().split()])


def distance(X1, X2):
    return ((X1[0] - X2[0])**2 + (X1[1] - X2[1])**2)**0.5


def mean(array):
    return sum(array)/len(array)


p = itertools.permutations(X, N)

ans = []
for X in p:
    D = []
    for i in range(N-1):
        X1, X2 = X[i], X[i+1]
        D.append(distance(X1, X2))
    ans.append(sum(D))
print(mean(ans))
