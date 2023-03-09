def solution(k, score):
    lists = []
    result = []
    for i in score:
        lists.append(i)
        lists.sort()
        if len(lists) >  k:
            del(lists[0])
        result.append(lists[0])
    return result