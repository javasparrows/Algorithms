def main():
    N = int(input())
    B = list(map(int, input().split()))

    res = 0
    for i in range(N-2):
        res += min(B[i], B[i+1])

    res += B[0]
    res += B[-1]
    print(res)
    
main()