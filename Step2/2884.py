# 두 수를 a b 이렇게 받는다면 
h,m = map(int,input().split())

if m < 45 and h > 0:
    h = h - 1
    m = m + 15
    print(h, m)
# 0시일때를 생각해야한다.
elif m < 45 and h == 0:
    h = 23
    m = m + 15
    print(h, m)
else:
    m = m -45
    print(h, m)
