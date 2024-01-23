from bisect import bisect_left,bisect_right

def count_bisect(a,left_value,right_value):
    right_index = bisect_left(a,right_value)
    left_index = bisect_right(a,left_value)

    return right_index-left_index

def solution(words,quries):
    answer = []
    
    array = [[] for _ in range(10001)] 
    reverse_array = [[] for _ in range(10001)]

    for word in words:
        len_word = len(word)
        array[len_word].append(word)
        reverse_array[len_word].append(word[::-1]) # 거꾸로

    for i in range(10001): # bisect를 사용하기 위해 정렬
        array[i].sort()
        reverse_array[i].sort()
    for i in quries:
        len_quries = len(i)
        if i[0] != '?':
            res = count_bisect(array[len_quries],i.replace('?','a'),i.replace('?','z')) 
        else:
            res = count_bisect(reverse_array[len_quries],i[::-1].replace('?','a'),i[::-1].replace('?','z'))
        answer.append(res)

    return answer