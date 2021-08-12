def knapsack_simple(N, h):
    dp = [float('inf')]*(N)
    dp[0] = 0

    for i in range(0, N-1):
        # dp[i+1]をそのままにするかどうか
        dp[i+1] = min(dp[i+1], dp[i] + abs(h[i+1]-h[i]))
        if i < N-2:
            # dp[i+2]をそのままにするかどうか
            dp[i+2] = min(dp[i+2], dp[i] + abs(h[i+2]-h[i]))
    return dp[N-1]
