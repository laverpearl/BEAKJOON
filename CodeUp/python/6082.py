"""
기초-종합 / 3 6 9 게임의 왕이 되자 


입력
30 보다 작은 정수 1개가 입력된다. (1 ~ 29)

출력
1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다. 

참고
print(a, end=' ') -> 출력 후 공백문자(빈칸, ' ')로 끝낸다

"""

a = int(input())
for i in range(1, a+1):
    if i <= 10:
        if i % 3 == 0:
            print('X', end=' ')
        else:
            print(i, end=' ')
    elif i <= 20:
        if (i-10) % 3 == 0:
            print('X', end=' ')
        else:
            print(i, end=' ')
    else:
        if (i-20) % 3 == 0:
            print('X', end=' ')
        else:
            print(i, end=' ')