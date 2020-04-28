#include <iostream>
using namespace std;
template <class T> inline bool chmax(T &a, T b) {if (a < b) {a = b; return true;} return false;}
template <class T> inline bool chmin(T &a, T b) {if (a > b) {a = b; return true;} return false;}

// 入力
int N;
long long W, weight[110], value[110]; // 少し余裕を持たせてサイズ110で用意

// DP table
long long dp[110][100100] = {0};

int main() {
    cin >> N >> W;
    for (int i = 0; i < N; ++i) cin >> weight[i] >> value[i];

    // DP
    for (int i = 0; i < N; ++i) {
      for (int sum_w = 0; sum_w <= W; ++sum_w) {
        // i番目の品物を選び場合
        if (sum_w - weight[i] >= 0) {
          chmax(dp[i+1][sum_w], dp[i][sum_w - weight[i]] + value[i]);
        }
        // i番目の品物を選ばない場合
        chmax(dp[i+1][sum_w], dp[i][sum_w]);
      }
    }

    cout << dp[N][W] << endl;
}