#include<iostream>
#include<set>
using namespace std;
typedef long long ll;
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)

int main() {
  int N;
  int d[110];
  cin >> N;
  REP(i,N) cin >> d[i];
  
  set<int> values;
  REP(i,N) values.insert(d[i]);
  
  cout << values.size() << endl;
}