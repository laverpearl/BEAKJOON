"""
기초 비교연산 / 정수 2개 입력받아 비교하기

입력
2개의 정수가 공백을 두고 입력된다

출력
b가 a보다 크거나 같은경우 True를, 그렇지 않은경우 False를 출력

"""


a, b = map(int, input().split())
print(a<=b)