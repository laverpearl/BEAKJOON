# 윤년 / 윤년이면 1을, 윤년이 아니면 0을 출력하는 프로그램
# 윤년은 연도가 4의 배수이면서 100의 배수가 아닐때 또는 400의 배수일때



year = int(input())

if (year%4 == 0) and (year%100 != 0):
    print('1')
elif year%400 == 0:
    print('1')
else:
    print('0')

