#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)

int main() {
  int N;
  int a[110];
  cin >> N;
  REP(i,N) cin >> a[i];
  
  sort(a, a+N, greater<int>());
  int A,B = 0;
  REP(i,N) {
    if (i%2 == 0) A += a[i];
    else B += a[i];
  }
  
  cout << A-B << endl;
}