"""
기초-종합 / 짝수 합 구하기 


입력 
정수 1개가 입력된다 (1~100)

출력
1부터 그 수까지 짝수만 합해 출력한다

"""

n = int(input())
m = int(0)
for i in range(n+1):
    if (i % 2) == 0:
        m += i
print(int(m))
