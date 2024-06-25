# x1, y1    x2, y2
# 4 combinations in each one we calculate
# the area: (a1 + a2) * max(b1, b2)

x1, y1, x2, y2 = (int(i) for i in input().split())

def calc_area(x1, y1, x2, y2):
    x = x1 + x2
    y = max(y1, y2)
    area = x * y
    return (area, x, y)

max_comb = (1e7, 0, 0)
for comb in ((x1, y1, x2, y2),
            (x1, y1, y2, x2),
            (y1, x1, x2, y2),
            (y1, x1, y2, x2)):
    cur_res = calc_area(*comb)
    if cur_res[0] < max_comb[0]:
        max_comb = cur_res
        
print(max_comb[1], max_comb[2])