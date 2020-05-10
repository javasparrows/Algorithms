#include<iostream>
#include<vector>
using namespace std;
typedef long long ll;
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define FOR(i,a,b) for(ll i=a;i<=(ll)(b);i++)


//標準入力　スペースか改行で区切ってくれる
int a, b, c;
cin >> a >> b >> c;

//標準出力
cout << "a" << "b";               //こういう書き方もできる
cout << "a" << 100 << "b" << endl;        //こういう書き方もできる

//for文
for (int i = 0; i < N; i++) {
}

//配列
vector<int> vec;          //配列の宣言
vec = { 10, 20, 30 };    //配列への代入
vec.size()                //配列の要素数 上の場合3が帰ってくる
vec.at(i)                 //配列のi番目にアクセス
vector<vector<int>> vec(10, vector<int>(10));   //二次元配列の宣言