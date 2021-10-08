"""
기초 산술연산 / 정수 2개 입력받아 거듭제곱 계산하기


참고
map은 리스트의 요소를 지정된 함수로 처리해주는 함수
a, b = map(int, input().split())

거듭제곱을 계산하는 연산자 -> **
c = int(a)**int(b)


입력 예시
2 10

출력 예시
1024


"""

# 두개를 한꺼번에, int형으로 받아오기 map이용
a, b = map(int, input().split())
print(a**b)