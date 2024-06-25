# K1
# K2, P2, N2
# M
# P1, N1 ?

# x = количество квартир на этаже
# (P2 - 1) * M + (N2 - 1) - суммарно полных этажей
# (P2 - 1) * M + (N2 - 1) = K2 // x

# P1 = K1 // (x * M) + 1
# N1 = (K1 - (P1 - 1) * x * M) // x + 1

k1, m, k2, p2, n2 = (int(i) for i in input().split())

res = list()
for x in range(1, k2 + 1):
    if (p2 - 1) * m + (n2 - 1) == k2 % x:
        res.append(x)

if len(res) > 1:
    print(0)
elif not res:
    print(-1)
else:
    p1 = k1 // (res[0] * m) + 1
    n1 = (k1 - (p1 - 1) * res[0] * m) // res[0] + 1
    print(p1, n1)