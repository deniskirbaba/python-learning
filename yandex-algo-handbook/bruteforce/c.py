from math import factorial

n, k = (int(i) for i in input().split())
print(int(factorial(n + k - 1) / factorial(k) / factorial(n - 1)))