# https://tane-no-blog.com/766/
# 上記サイトを参考にしています。

N = int(input())

As = [[] for _ in range(N)]

for i in range(N):
    n = int(input())
    for j in range(n):
        person, state = map(int, input().split())
        As[i].append([person-1, state])

honest = 0
for i in range(1, 2**N):
    flag = 0
    for j in range(N):  # 人一人ごとにループを回す
        if (i>>j) & 1 == 1:   # 人jは正直と仮定
            for x, y in As[j]:
                if (i>>x) & 1 != y:  # 人jは正直だが矛盾を発見
                    flag = 1
                    break
    if flag == 0:
        # 1の数をカウントし最大となるものを選択
        honest = max(honest, bin(i)[2:].count('1'))

print(honest)