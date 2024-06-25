troom, tcond = [int(i) for i in input().split()]
mode = input()

if tcond < troom:
    if mode in ['auto', 'freeze']:
        print(tcond)
    else:
        print(troom)
else:
    if mode in ['auto', 'heat']:
        print(tcond)
    else:
        print(troom)
        