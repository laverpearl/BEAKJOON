"""
기초 / 입출력

연월일 입력받아 나누어 출력하기


참고 (자르기)

s = input()
print(s[0:2])

를 실행하면 0번째 문자부터 1번째 문자까지 잘라 출력한다
s[a,b] 라고하면, s라는 단어에서 a번째 문자부터 b-1번째 문자까지
잘라낸 부분을 의미한다


입력 210928

"""


date = input()
# []안은 , 가 아니라 :
print(date[0:2], date[2:4], date[4:6], sep=' ') 

