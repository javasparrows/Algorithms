#include <iostream>
using namespace std;
typedef long long ll;

#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define FOR(i,a,b) for(ll i=a;i<=(ll)(b);i++)

const int MAX = 110;
bool dp[MAX][MAX*MAX];

int N;
int p[MAX];

int main() {
  int sum;
  int a;
  cin >> N;
  REP(i,N) {
    cin >> a;
    p[i] = a;
    sum += a;
  }
  
  REP(i,N) dp[0][i] = false;
  dp[0][0] = true;
  
  FOR(num,1,N+1) {
    REP(val, sum+1) {
       if(val - p[num-1] < 0) {
         // val-p[num-1]が負になる場合はdp[num-1][val]だけチェック
         dp[num][val] = dp[num - 1][val];
       }
       else {
         // num-1番目まででvalかval-p[num-1]が作れたらOK
         dp[num][val] = dp[num - 1][val] || dp[num - 1][val - p[num - 1]];
       }
    }
  }
  
  // N番目までで作れる数の個数を計算
  int ans = 0;
  REP(i,sum+1) {
    if (dp[N][i]) ans++;
  }
  
  cout << ans << endl;
}