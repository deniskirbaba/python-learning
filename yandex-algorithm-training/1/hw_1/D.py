a, b, c = (int(input()) for i in range(3))

if c < 0:
    print('NO SOLUTION')
elif a == 0:
    if b**0.5 == c:
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')
else:
    ans = (c**2 - b) / a
    if ans % 1 == 0:
        print(int(ans))
    else:
        print('NO SOLUTION')