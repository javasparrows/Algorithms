K = int(input())


def calc_next(ar):
    res = []
    for val in ar:
        for j in range(-1, 2):
            add = (val % 10) + j
            if add >= 0 and add <= 9:
                res.append(val*10+add)
    return res


cur = []
all_ = []
# 1桁の場合
for v in range(1, 10):
    cur.append(v)
    all_.append(v)

# 10桁まで
for d in range(1, 10):
    # 次の桁を列挙
    cur = calc_next(cur)

    # allに格納
    for val in cur:
        all_.append(val)

# K番目
print(all_[K-1])
