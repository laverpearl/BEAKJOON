"""
기초 비트시프트 연산 / 정수 1개 입력받아 2배 곱해 출력하기

2배 곱해 출력하기
1. *2 사용하기
2. 비트단위시프트연산자 <<1 사용하기



비트단위시프트 연산자 

컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에, 
2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0또는 양의 정수인경우)이나 1(음의 정수인경우)이 개수만큼 추가되고, 
가장 오른쪽에 있는 1비트는 사라진다.





"""


a = int(input())
print(a<<1)