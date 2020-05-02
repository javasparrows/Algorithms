#include <iostream>
#include <vector>
#include <map>
using namespace std;
typedef long long ll;

int N;

int main() {
    cin >> N;
    vector<ll> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    
    // 累積和と連想配列
    vector<ll> s(N+1, 0);
    map<ll, ll> nums;
    for (int i = 0; i < N; i++) s[i+1] = s[i] + A[i];
    // sの中のそれぞれの数を数え上げる。（その数があったら1を足すという単純なアルゴリズム）
    for (int i = 0; i < N+1; i++) nums[s[i]]++;
    
    // 集計処理
    ll res = 0;
    for (auto it : nums) {
        ll  num = it.second;  // it.firstがit.second個ある
        res += num * (num - 1) / 2;
    }
    cout << res << endl;
}