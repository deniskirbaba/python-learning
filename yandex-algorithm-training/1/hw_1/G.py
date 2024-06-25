# N - kg всего сплава
# K - kg заготовка
# M - kg деталь - если остается возвращаем в сплав
# найти количество деталей 

# one cycle: сплав -> число деталей, остатки
# func of cycle and call it recursively
# while residue of splav >= K

# complexity: O(number of calls of function)
# number of calls of function =
# n = n_k * k + res1
# k = n_m * m + res2

# n = n_k * (n_m * m + res2) + res1

n, k, m = (int(i) for i in input().split())

def work_cycle(n, k, m):
    '''Calculate the number of components that can be produced from one cycle'''
    res = n % k
    n_k = n // k
    
    res += n_k * (k % m)
    n_m = n_k * (k // m)
    return n_m, res

n_m, res = work_cycle(n, k, m)
while res >= k and k >= m:
    new_n_m, res = work_cycle(res, k, m)
    n_m += new_n_m
    
print(n_m)