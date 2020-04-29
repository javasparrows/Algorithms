#include <iostream>
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
using namespace std;
template <class T> inline bool chmax(T &a, T b) {if (a < b) {a = b; return true;} return false;}
template <class T> inline bool chmin(T &a, T b) {if (a > b) {a = b; return true;} return false;}
typedef long long ll;
const ll INF = 1LL<<60;
const int MAX_N = 110;
const int MAX_V = 100100;

// 入力
int N;
ll W, weight[MAX_N], value[MAX_N]; // 少し余裕を持たせてサイズ110で用意

// DP table
ll dp[MAX_N][MAX_V];

int main() {
    cin >> N >> W;
    REP(i,N) cin >> weight[i] >> value[i];
  
    // 初期化
    REP(i,MAX_N) REP(j,MAX_V) dp[i][j] = INF;
  
    // 初期条件
    dp[0][0] = 0;

    // DP
    REP(i,N) {
        REP(sum_v,MAX_V) {
        // i番目の品物を選び場合
        if (sum_v - value[i] >= 0) {
          chmin(dp[i+1][sum_v], dp[i][sum_v - value[i]] + weight[i]);
        }
        // i番目の品物を選ばない場合
        chmin(dp[i+1][sum_v], dp[i][sum_v]);
      }
    }
  
    // 最適地の出力
    ll res = 0;
    REP(sum_v,MAX_V) {
        if (dp[N][sum_v] <= W) res = sum_v;
    }
    cout << res << endl;
}