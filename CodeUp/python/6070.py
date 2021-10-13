"""
기초-조건/선택실행구조 / 월 입력받아 계절 출력하기




입력
월을 의미하는 1개의 정수가 입력된다(1~12)

출력
계절 이름을 출력한다

"""

a = int(input())

if 3 <= a <= 5:
    print("spring")

elif 6 <= a <= 8:
    print("summer")

elif 9 <= a <= 11:
    print("fall")

else:
    print("winter")