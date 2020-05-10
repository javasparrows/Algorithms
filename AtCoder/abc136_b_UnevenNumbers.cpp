#include<iostream>
using namespace std;

int main() {
  int N;
  cin >> N;
  
  int res = 0;
  for (int i=1; i<N+1; i++) {
    int count = 0;
    int d = i;
    while (d) {
      d /= 10;
      count++;
    }
    if (count % 2) res++;
  }
  
  cout << res << endl;
}