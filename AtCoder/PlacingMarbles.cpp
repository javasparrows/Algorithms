#include <iostream>
#include <string>
#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
using namespace std;
 
int main() {
    string s;
    cin >> s;
    int counter = 0;
    REP(i,s.size()) {
        if (s[i] == '1') counter++;
    }
    cout << counter << endl;
}