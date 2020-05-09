N, K = map(int, input().split())
MOD = 10**9 + 7

low = high = 0
ans = 0
for i in range(K, N+2):
    low = i*(i-1)//2  # i個取った時の和の最小値
    high = i*(2*N - i + 1)//2  # i個取った時の和の最大値
    ans += (high - low + 1)  # i個取った時の和の場合の数
    ans %= MOD

print(ans)
