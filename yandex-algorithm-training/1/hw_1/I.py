# hole D*E
# size of brick A*B*C
# ---
# determine if bricks can get though hole
# ---
# sort the A,B,C - then pick 2 smallest
# sort DE - then check elementwise the <=
# ---

a, b, c, d, e = (float(input()) for i in range(5))
hole = sorted([d, e])
min_brick = sorted([a, b, c])[:2]
if hole[0] >= min_brick[0] and hole[1] >= min_brick[1]:
    print('YES')
else:
    print('NO')