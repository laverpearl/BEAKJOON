# 처음에 테스트 케이스 숫자 받아와서
t = int(input())

# for 문으로 A,B 숫자 입력 받아와서 프린트
for i in range(t):
    A,B = map(int,input().split())
    print(A+B)
     