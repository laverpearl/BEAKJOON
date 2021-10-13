"""
기초-조건/선택실행구조 / 정수 1개 입력받아 분류하기


입력
정수 1개가 입력된다

출력
음수이면서 짝수이면, A
음수이면서 홀수이면, B
양수이면서 짝수이면, C
양수이면서 홀수이면, D
를 출력한다.


다른풀이

a = int(input())
if a<0 and (a%2 == 0):
    print("A")
elif a<0 and (a%2 != 0):
    print("B")
elif a>0 and (a%2 == 0):
    print("C")
else:
    print("D")

"""

a = int(input())
if a < 0:
    if (a%2) == 0:
        print("A")
    else:
        print("B")

else:
    if (a%2) == 0:
        print("C")
    else:
        print("D")