# ax + by = e
# cx + dy = f
# ---
# find solution
# ---
# if det_main nonzero -> two solutions
# if not...
#   if not all detx, dety are 0 -> no solutions


from enum import Enum

class SolutionType(Enum):
    NO_SOLUTION = 0,
    INF_DEP_SOLUTIONS = 1,
    ONE_SOLUTION = 2,
    INF_Y_SOLUTIONS = 3,
    INF_X_SOLUTIONS = 4,
    INF_UNDEP_SOLUTIONS = 5,

def det(a, b, c, d):
    return a * d - b * c

def solve(a, b, c, d, e, f):
    det_main = det(a, b, c, d)
    det_x = det(e, b, f, d)
    det_y = det(a, e, c, f)

    if det_main != 0:
        return (SolutionType.ONE_SOLUTION.value[0], round(det_x / det_main, 5), round(det_y / det_main, 5))
    elif det_x == 0 and det_y == 0:
        if a == 0 and b == 0 and e == 0:
            a, b, e = c, d, f
        if c == 0 and d == 0  and f == 0:
            c, d, f = a, b, e
        if a == 0 and b == 0 and e != 0 or c == 0 and d == 0 and f != 0:
            return (SolutionType.NO_SOLUTION.value[0], )
        elif a == 0 and b == 0 and c == 0 and d == 0:
            return (SolutionType.INF_UNDEP_SOLUTIONS.value[0], )
        elif a == 0:
            return (SolutionType.INF_X_SOLUTIONS.value[0], round(e / b, 5))
        elif b == 0:
            return (SolutionType.INF_Y_SOLUTIONS.value[0], round(e / a, 5))
        else:
            return (SolutionType.INF_DEP_SOLUTIONS.value[0], round(-a / b, 5), round(e / b, 5))
    else:
        return (SolutionType.NO_SOLUTION.value[0], )
    

coefs = [float(input()) for i in range(6)]
print(*solve(*coefs))
