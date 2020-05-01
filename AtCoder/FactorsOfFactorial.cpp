#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

vector<pair<ll, ll>> prime_factorize(ll N) { // 約数の個数を数える関数
  vector<pair<ll, ll> > res;
  for (ll a = 2; a*a <= N; a++) {
    if (N % a != 0) continue;
    ll ex = 0;
    while (N % a == 0) {  // aが素因数だったらexを加算してNをaで割る
      ex++;
      N /= a;
    }
    res.push_back({a, ex});
  }
  if (N != 1) res.push_back({N, 1});
  return res;
}

int main() {
  ll N;
  cin >> N;

  const int MOD = 1000000007;
  vector<ll> ex(N+1, 0);  // exp(p) := pの指数
  for (ll n=2; n <= N; n++) {
    const auto& res = prime_factorize(n);  // nの素因数分解
    for (auto p : res) ex[p.first] += p.second;
  }
  ll res = 1;
  for (int p = 2; p <= N; p++) {
    res *= ex[p] + 1;  // 約数の個数は(exp+1)の積
    res %= MOD;
  }
  
  cout << res << endl;
}