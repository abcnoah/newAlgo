def solution(id_list, report, k):
    answer = {x:0 for x in id_list} #신고횟수 리턴용
    dic_return = {x:0 for x in id_list} #유저별 신고받은 횟수
    
    #중복 제거
    set_report = set(report)
    for i in set_report:
        dic_return[i.split()[1]] += 1
    for i in set_report:
        if dic_return[i.split()[1]] >= k:
            answer[i.split()[0]] += 1
    
    return list(answer.values())