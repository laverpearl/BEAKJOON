"""
기초-종합 / 거기까지 이제그만!


입력
언제까지 합을 계산할 지, 정수 1개를 입력받는다.
단, 입력되는 자연수는 100,000,000이하이다. 

출력
1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
그때까지의 합을 출력한다. 


"""

a = int(input())
b = int(0)
for i in range(1, a+1):
    b += i
    if b >= a:
        print(b)
        break
