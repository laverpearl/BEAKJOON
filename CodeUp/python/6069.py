"""
기초-조건/선택실행구조 / 평가 입력받아 다르게 출력하기



문제

평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자. 

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what? 


입력
영문자 1개가 입력된다.
(A, B, C, D 등 문자 1개가 입력된다.) 

출력
문자에 따라 다른 내용이 출력된다.

"""

m = input()

if m == "A":
    print("best!!!")

elif m == "B":
    print("good!!")

elif m == "C":
    print("run!")

elif m == ("D"):
    print("slowly~")
    
else:
    print("what?")