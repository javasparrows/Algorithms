N, Q = map(int, input().split())

tree_list = [input().split() for _ in range(N-1)]

query_list = [input().split() for _ in range(Q)]
query_list_int = [[int(k) for k in i] for i in query_list]

val_list = [0]*N
linked_node_list = [[] for _ in range(N)]

# 無向グラフのリンク関係を作成（上流への接続も含んでいる）
for a, b in tree_list:
    a, b = int(a)-1, int(b)-1
    linked_node_list[a].append(b)  # 子の追加
    linked_node_list[b].append(a)  # 子の追加

for index, val in query_list_int:
    val_list[index-1] += val

stack = [0]  # ルートノードの値を入れたスタックを生成、巡回するターゲットを格納する
parent = [0] * (N+1)  # 訪問済みノードを記憶するスタックを格納する

# 再帰関数を使うとメモリ制限に引っかかるので、whileで順次実行する
# スタックでLIFOを使う。LIFOになるので、一番若い者をみながら深さ優先探索にできる。
# 親ノードを覚えておいて弾くようにする
# 有向グラフで定義すれば親を弾く処理はいらない

while True:
    # ルートから順に巡回
    v = stack.pop()   # 後ろから要素を取り出す
    for child in linked_node_list[v]:
        print(child, parent[v])
        if child != parent[v]:
            parent[child] = v  # 訪問済みノードを格納
            stack.append(child)  # このノードvの接続先ノードをスタックに格納
            val_list[child] += val_list[v]  # 累積和
    if not stack:
        # スタックがなくなれば巡回終了
        break

print(*val_list)
