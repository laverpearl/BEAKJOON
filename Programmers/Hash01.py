def solution(participant, completion):
    #정렬이용해서 알파벳 순서로,,
    participant.sort()
    completion.sort()
    
    #반복문 돌려가면서 비교하기
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    #반복문 다 돌렸을때까지 이름순서가 같다면,,
    return participant[i+1]