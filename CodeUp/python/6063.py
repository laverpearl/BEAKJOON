"""
기초 3항 연산 / 정수 두개 입력받아 큰 값 출력하기


참고 
3항연산 -> 3개의 요소로 이루어져있다
"x if C else y"의 형태로 작성 / C는 조건식 또는 값 


입력
두 정수가 공백을 두고 입력된다

출력 
두 정수중 큰 값을 10진수로 출력한다


"""

a, b = map(int, input().split())
print(a if(a>b) else b)