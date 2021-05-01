# 숫자 정수로 받아오기 int(input())으로,    한번 틀렸음
n = int(input())

#range(1,10) --> 1 2 3 4 5 6 7 8 9 
for i in range(1,10):
    print(n, "*", i, "=", n*i)
    i = i + 1 
