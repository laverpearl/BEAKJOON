"""
기초 산술연산 / 실수 2개 입력받아 나눈 결과 계산하기




입력예시
10.0 3.0

출력예시
3.333


"""

a, b = map(float, input().split())
c = a/b # 나눗셈 연산자 -> /
print(format(c,".3f"))