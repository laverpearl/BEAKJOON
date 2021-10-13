"""
기초 3항 연산 / 정수 3개 입력받아 가장 작은값 출력하기


입력
3개의 정수가 공백으로 구분되어 입력된다

출력
가장 작은 값을 출력한다

"""

a, b, c = map(int,input().split())
d = a if(a<b) else b
print(d if(d<c) else c)