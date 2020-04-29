#include <iostream>
#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
using namespace std;

int N;
int A[210];

int main() {
    cin >> N;
    REP(i,N) cin >> A[i];
  
    int res = 0;
  
    while (true) {
        bool exist_odd = false;
        REP(i,N) {
            if (A[i] % 2 == !0) exist_odd = true;
        }
      
        if (exist_odd) break;
      
        REP(i,N) A[i] /= 2;
        res++;
    }
  
    cout << res << endl;
}