"""
기초 논리연산 / 참 거짓 바꾸기

참고
bool -> True, False를 나타내는 자료형

a = bool(int(input()))
한번에 한 단계씩 계산/처리/평가 된다
input() -> int() -> bool() 순서로 처리

참 또는 거짓의 논리값을 역으로 바꾸기 위해 not 예약어 사용가능 (NOT 연산)

참, 거짓의 논리값인 불값을 다루어주는 예약어 -> not, and, or

정수값 0은 False이고, 나머지 정수값들은 True로 평가된다

입력 
정수 1개가 입력된다

출력
입력된 정수의 불 값이 False이면 True, True이면 False를 출력한다

"""

n = bool(int(input()))
print(not n)