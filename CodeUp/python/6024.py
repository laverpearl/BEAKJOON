"""
기초 / 입출력

단어 2개 입력받아 이어붙이기


입력
알파벳과 숫자로 이루어진 2개의 단어가 공백으로 구분되어 입력된다

입력 예시
aaa bbb

출력
입력된 2개의 단어를 순서대로 붙여 출력한다

"""


word = input().split()
print(word[0],word[1],sep='')
# sep=''으로 이어붙여 출력


# print(word)으로 출력시 ['aaa', 'bbb']