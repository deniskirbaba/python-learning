# stop = 1 min
# int_a = a, int_b = b
# n_a = n, n_b = m
# ----
# min and max time of waiting (-1 if incorrect)
# ---
# time_min = stop + (stop + int) * (n - 1)
# time_max = (stop + int) * n

# calculate this values for a, b
# pick the max(min_a, min_b) = overall_min and min(max_a, max_b) = overall_max

# about -1:
# if the minmax intervals dont intersects = -1
# check this
# ---

stop = 1
a, b, n, m = (int(input()) for i in range(4))

def calc_min_max(interval, n, stop):
    return stop + (stop + interval) * (n - 1), (stop + interval) * n + interval

min_a, max_a = calc_min_max(a, n, stop)
min_b, max_b = calc_min_max(b, m, stop)

min_res = max(min_a, min_b)
max_res = min(max_a, max_b)

if min_res > max_res:
    print(-1)
else:
    print(min_res, max_res)