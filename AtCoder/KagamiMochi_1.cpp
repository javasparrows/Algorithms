#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)

int main() {
  int N;
  int d[110];
  cin >> N;
  REP(i,N) cin >> d[i];
  
  int num[110] = {0};
  REP(i,N) {
    num[d[i]]++;
  }
  
  int res = 0;
  REP(i,101) {
    if (num[i]) res++;
  }
  
  cout << res << endl;
}