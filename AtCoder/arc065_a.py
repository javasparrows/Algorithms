## 後ろから探索していく方法

s = input()
t = ['dream', 'dreamer', 'erase', 'eraser']
s = s[::-1]
t = [i[::-1] for i in t]

can = True
i = 0
while i < len(s):
    can2 = False
    # 4つの単語のどれか1つででも当てはまるかを調べる
    for j in range(4):
        d = t[j]
        if s[i:i+len(d)] == d:
            can2 = True
            i += len(d)
    if not can2:
        can = False
        break

if can:
    print('YES')
else:
    print('NO')