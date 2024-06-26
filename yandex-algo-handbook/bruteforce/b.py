from math import factorial

n, k = (int(i) for i in input().split())
if k > n:
    print(0)
else:
    print(int(factorial(n) / factorial(k) / factorial(n - k)))