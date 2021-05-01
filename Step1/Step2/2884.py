h,m = map(int,input().split())

if m < 45 and h > 0:
    h = h - 1
    m = m + 15
    print(h, m)
elif m < 45 and h == 0:
    h = 23
    m = m + 15
    print(h, m)
else:
    m = m -45
    print(h, m)
