"""
기초-반복실행구조 / 정수 1개 입력받아 그 수까지 출력하기2



입력
정수 1개가 입력된다(1~100)

출력
0부터 그 수까지 줄을 바꿔 한개씩 출력한다


"""

n = int(input())
for i in range(n+1):
    print(i)
    i += 1
