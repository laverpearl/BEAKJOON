"""
기초-종합 / 언제까지 더해야 할까?

입력
정수 1개가 입력된다

출력
1,2,3,4,5...를 순서대로 계속더해 합을 만들어가다가, 
입력된 정수와 같거나 커졌을때 마지막에 더한 정수를 출력한다


"""

a = int(input())
b = 0
for i in range(a):
    b += i
    if b >= a:
        print(i)
        break
