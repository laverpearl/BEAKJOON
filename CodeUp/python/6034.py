"""
기초 산술연산 / 정수 2개 입력받아 차 계산하기


입력 예시
123 -123

출력 예시
256


"""


# a, b를 str로 받고 계산을 int로 계산
a, b = input().split()
print(int(a) - int(b))