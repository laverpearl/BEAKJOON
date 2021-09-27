"""

시간 입력받아 그대로 출력하기


sep은 분류기호 (seperator)를 의미한다.


예시

a, b = input().split(':')
print(a, b, sep=':')


참고

input().split(':') 을 사용하면 콜론 ':' 기호를 기준으로 자른다

print(a, b, sep=':')을 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다
a : b


"""

a, b = input().split(':')
print(a, b, sep=':')