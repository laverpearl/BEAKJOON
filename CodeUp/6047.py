"""
기초 비트시프트연산 / 2의 거듭제곱 배로 곱해 출력하기


a<<1 ---> a*2^1
a<<2 ---> a*2^2
a<<3 ---> a*2^3
a<<4 ---> a*2^4


a<<b ---> a*2^b



입력
정수 2개(a, b)가 공백을 두고 입력된다.
0 <= a, b <= 10

출력
a를 2^b배 만큼 곱한 값을 출력한다.


입력예시
1 3

출력예시
8


"""

a, b = map(int, input().split())
print(a<<b)