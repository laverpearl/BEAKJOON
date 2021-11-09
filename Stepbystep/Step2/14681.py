a = int(input())
b = int(input())

if a>0 and b> 0:
    print("1")
elif a>0 and b<0:
    print("4")
elif a<0 and b>0:
    print("2")
else:
    print("3")


# 숫자를 따로 받아서 input은 따로 받게 하고, 각 사분면당 조건을 if랑 elif로,, 