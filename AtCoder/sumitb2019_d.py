N = int(input())
S = input()

ans = 0
for i in range(1000):
    num = str(i).zfill(3)
    if S.find(num[0]) == -1:
        continue  # 1文字目が合っているかどうか
    S1 = S[S.find(num[0])+1:]
    if S1.find(num[1]) == -1:
        continue  # 2文字目が合っているかどうか
    S2 = S1[S1.find(num[1])+1:]
    if S2.find(num[2]) == -1:
        continue  # 3文字目が合っているかどうか
    ans += 1
print(ans)