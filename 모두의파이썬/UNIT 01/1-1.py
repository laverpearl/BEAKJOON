"""
1부터 n까지 연속한 숫자의 합을 구하는 알고리즘




실행결과
55
5050

"""


def sum(n):
    m = 0
    for i in range(1, n+1): # 1부터 n까지
        m = m + i
    return m

print(sum(10))
print(sum(100))

