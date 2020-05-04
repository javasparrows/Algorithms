#include<iostream>
#include<set>
using namespace std;
typedef long long ll;
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)

int N;
ll Y;

int main() {
  cin >> N >> Y;
  
  int total = 0;
  int res10000 = -1, res5000 = -1, res1000 = -1;
  REP(i,N+1) {
    for (int j = 0; j+i<N+1; j++) {
      int k = N - i - j;
      total = 10000*i + 5000*j + 1000*k;
      if (total == Y) {
        res10000 = i;
        res5000 = j;
        res1000 = k;
        break;
      }
    }
  }
  
  cout << res10000 << ' ' << res5000 << ' ' << res1000 << endl;
}