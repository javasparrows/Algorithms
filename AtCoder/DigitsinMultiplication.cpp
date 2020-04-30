#include<iostream>
using namespace std;
typedef long long ll;

int count_digits(ll n) {
  int res = 0;
  while (n) {
    n /= 10;
    res++;
  }
  return res;
}

int main() {
  ll N;
  cin >> N;
  
  int ans = 10000;
  
  for (ll A=1; A*A<=N; A++) {
    if (N%A == 0) {
      ll B = N/A;
      int count = max(count_digits(A), count_digits(B));
      ans = min(ans, count);
    }
  }
  
  cout << ans << endl;
}