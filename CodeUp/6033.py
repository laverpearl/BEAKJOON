"""
기초 산술연산 / 문자 1개 입력받아 다음 문자 출력하기


영문자 a의 그 다음문자는 b
숫자 0의 그 다음문자는 1

예시
...
print(chr(n+1))


참고
숫자는 수를 표현하는 문자로서 '0'은 문자 그 자체를 의미하고,
0은 값을 의미한다.

힌트
아스키문자표에서 'A'는 10진수 65로 저장되고
'B'는 10진수 66으로 저장된다
문자도 값으로 덧셈을 할 수 있다
어떤 문자의 값에 1을 더하면 그 다음문자의 값이 된다.

ord()
문자열을 아스키코드로 반환할 수 있는하수



"""


n = ord(input())
print(chr(n+1))