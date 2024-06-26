# 'n' time intervals
# need to find maximum non-intersect intervals
# ---
# at each step:
#   find the interval with the minimal right edge
#   add this interval to the result array
#   delete all intervals which intersects with this interval
# 
# if found multiple sch intervals, choose the bigger one
# --- 

n = int(input())
intervals = [[int(j) for j in input().split()] for i in range(n)]

# sort by right edge ascending and left edge descending
intervals.sort(key=lambda x: (x[1], x[0]))

# create res array (actually just counter)
res_cnt = 1

# pick the first interval and go through all intervals
# delete all intervals whose left edge <= cur right edge
# if not - we find next res interval
if len(intervals) > 1:
    cur_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] > cur_interval[1]:
            cur_interval = intervals[i]
            res_cnt += 1
print(res_cnt)
    