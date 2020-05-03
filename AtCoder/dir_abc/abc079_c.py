s = input()
n_op = len(s) - 1  # 隙間の個数
for i in range(2**n_op):
    # まずは演算子の組み合わせを全て作る
    op = ['-'] * n_op
    for j in range(n_op):
        if i >> j & 1:
            op[n_op - 1 - j] = '+'

    formula = ''
    for p_s, p_op in zip(s, op+['']):
        formula += p_s + p_op
    if eval(formula) == 7:
        print(formula + '=7')
        break
