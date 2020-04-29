#include <iostream>
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
typedef long long ll;
using namespace std;

int N,A,B;

int findSumOfDigits(int n) {
  int sum = 0;
  while (n>0) {
    sum += n%10;
    n/= 10;
  }
  return sum;
}

int main() {
  cin >> N >> A >> B;
  int total = 0;
  REP(i,N+1) {
    int num = findSumOfDigits(i);
    if (A <= num && num <= B) total += i;
  }
  cout << total << endl;
}