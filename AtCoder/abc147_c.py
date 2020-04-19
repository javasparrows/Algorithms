# https://tane-no-blog.com/766/
# 上記サイトを参考にしています。

N = int(input())

As = []

for i in range(N):
    n = int(input())
    for j in range(n):
        person, state = [int(k) for k in input().split()]
        As.append([[person-1, state]])

honest = 0
for i in range(2**N):
    flag = 0
    for j in range(N):  # 人一人ごとにループを回す
        if (i >> j) & 1:   # 人jは正直と仮定
            for x, y in As[j]:
                print(j >> x, j, x)
                if (j >> x) & 1 != y:  # 人jは正直だが矛盾を発見
                    flag = 1
                    break
    if flag == 0:
        # 1の数をカウントし最大となるものを選択
        honest = max(honest, bin(i)[2:].count('1'))

print(honest)
