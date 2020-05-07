def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = [int(input()) for _ in range(N)]

    memo = [0]*(max(A)+1)
    for a in A:
        memo[a] += 1

    res = 0
    for m in memo:
        if m > 1:
            res += m - 1

    print(res)


main()
