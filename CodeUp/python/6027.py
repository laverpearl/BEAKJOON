"""
기초 출력변환 / 10진 정수 입력받아 16진수로 출력하기


10진수 형태로 입력받고 
%x로 출력하면 16진수(hexadecimal) 소문자로 출력된다
%o로 출력하면 8진수(octal) 문자열로 출력된다

예시

n = int(input())
print('%x'%n)
하면 n에 저장되어있는 값을 16진수 소문자 형태 문자열로 출력된다


입력
255

출력
ff

"""


n = int(input())
print('%x'%n)