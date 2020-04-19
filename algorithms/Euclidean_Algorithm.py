# 最大公約数を求める有名なアルゴリズム
def euclid(a, b):
    c = a % b
    if c != 0:
        return euclid(b, c)
    else:
        return b