#if문 / 두 수 비교하기 

#a,b input 으로 숫자 받아오기
a,b = map(int,input().split())
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')