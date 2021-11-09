n = int(input())

sum = 0
# range에서 끝 숫자는 포함되지 않으니까 +1 해준다 
for i in range(n+1):
    sum = sum + i

print(sum)
