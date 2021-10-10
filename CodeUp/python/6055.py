"""
기초 논리연산 / 하나라도 참이면 참 출력


입력
두개의 정수가 공백을 두고 입력된다

출력
하나라도 참일 경우 True를 출력하고, 그 외의 경우에는 False를 출력한다


"""

a, b = map(int, input().split())
print(bool(a) or bool(b))