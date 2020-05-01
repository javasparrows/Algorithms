#include<iostream>
#include<vector>
using namespace std;
typedef long long ll;
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
 
int main() {
    // エラトステネスのふるい
    int MAX = 101010;
    vector<int> is_prime(MAX, 1);
    is_prime[0] = 0, is_prime[1] = 0;
    for (int i = 2; i<MAX; i++) {
        if (!is_prime[i]) continue;
        for (int j = i*2; j < MAX; j += i) is_prime[j] = 0;
    }
    
    // 2017likeかどうか
    vector<int> a(MAX, 0);
    for (int i = 0; i < MAX; i++) {
        if (i%2 == 0) continue;
        if (is_prime[i] && is_prime[(i+1)/2]) a[i] = 1;
    }
    
    // 累積和
    vector<int> s(MAX, 0);
    for (int i = 0; i < MAX; i++) s[i+1] = s[i] + a[i];
    
    ll Q;
    cin >> Q;
    REP(i,Q) {
        int l, r;
        cin >> l >> r;
        r++;
        
        cout << s[r] - s[l] << endl;
    }
}