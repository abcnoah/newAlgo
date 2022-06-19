#내 풀이
#리스트의 인덱스를 이용하여 해당 값이 존재하면 리스트의 값을 False로 줘서 True인 값들만 더하도록
def solution(numbers):
    answer = 0
    number_list = [True for i in range(10)]
    
    for number in numbers:
        number_list[number] = False
    
    for i in range(len(number_list)):
        if number_list[i]:
            answer += i
    
    return answer

#     #다른 사람 풀이
# def solution(numbers):
#     answer = 0
#     for i in range(10):
# 				if i not in numbers:
# 						answer += i
    
#     return answer