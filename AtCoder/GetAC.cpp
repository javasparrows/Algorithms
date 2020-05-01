#include<iostream>
#include<vector>
#include<string>
using namespace std;
typedef long long ll;

int N, Q;
string S;

int main() {
    cin >> N >> Q;
    cin >> S;
    
    vector<int> s(N+1, 0);
    for (int i = 0; i < N; i++) {
        if (S[i] == 'A' && S[i+1] == 'C') s[i+1] = s[i] + 1;
        else s[i+1] = s[i];
    }

    for (int i = 0; i < Q; i++) {
        int l, r;
        cin >> l >> r;
        
        cout << s[r-1] - s[l-1] << endl;
    }
}