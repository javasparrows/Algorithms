def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    H = list(map(int, input().split()))

    res = tmp = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            tmp += 1
        else:
            tmp = 0
        if tmp > res:
            res = tmp

    print(res)

main()
