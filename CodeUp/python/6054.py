"""
기초 논리연산 / 둘 다 참일 경우만 참 출력하기


입력
두개의 정수가 공백을 두고 입력된다

출력 
둘 다 True일 경우에만 True를 출력, 그 외의 경우에는 False를 출력



"""

a, b = map(int, input().split())
print(bool(a) and bool(b))