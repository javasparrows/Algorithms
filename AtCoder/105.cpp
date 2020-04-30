#include<iostream>
using namespace std;

// 約数の個数を数える
int div_count(int n) {
  int c = 0;
  int k;
  for (k=1; k<=n; k++) {
    if (n%k == 0) c++;
  }
  return c;
}

int main() {
  int N;
  cin >> N;
  
  int ans = 0;
  for (int i=1; i<=N; i+=2) {
    int num = div_count(i);
    if (num == 8) ans++;
  }
  
  cout << ans << endl;
}