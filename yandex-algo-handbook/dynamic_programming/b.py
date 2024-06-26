# 1 from any set
# 2 from any one set
# 2 from one and 1 from another set
# ---
# let R(0, 0) = L
# R(i, j) = L, if R(i - 1, j) = W and 
#                 R(i, j - 1) = W and 
#                 R(i - 2, j) = W and 
#                 R(i, j - 2) = W and 
#                 R(i - 1, j - 2) = W and 
#                 R(i - 2, j - 1) = W
# else R(i, j) = W
# --

n, m = (int(i) for i in input().split())
r = [[1] * (m + 2) for i in range(n + 2)]
r[2][2] = 0

for i in range(2, n + 2):
    for j in range(2, m + 2):
        if (
            r[i - 1][j] == 1 and r[i][j - 1] == 1 and
            r[i - 2][j] == 1 and r[i][j - 2] == 1 and
            r[i - 1][j - 2] == 1 and r[i - 2][j - 1]
        ):
            r[i][j] = 0
if r[-1][-1] == 0:
    print('Loose')
else:
    print('Win')