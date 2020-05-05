def main():
    N, K = map(int, input().split())
    S = input()

    count = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            count +=1 

    ans = min(count + K*2, N-1)
    print(ans)
    
main()