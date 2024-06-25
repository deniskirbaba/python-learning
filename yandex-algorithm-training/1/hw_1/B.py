a, b, c = [int(input()) for i in range(3)]

if a + b > c and b + c > a and a + c > b:
    print('YES')
else:
    print('NO')