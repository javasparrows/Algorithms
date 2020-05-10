K = int(input())

all_ = []
def rec(d, val, all_):
    '''
    d: 現在の桁数
    val: 現在の値
    all: ここに格納していく（参照型にしておく）
    '''
    # 格納
    all_.append(val)

    # 10桁だったらそれ以上やらずに打ち切り
    if d == 10:
        return

    # (ここで再帰呼び出しをする)
