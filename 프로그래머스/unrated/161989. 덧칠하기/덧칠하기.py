def solution(n, m, section):
    cnt = 0
    num = 0
    
    for i in section:
        if (num < i):
            cnt += 1
            num = m + i - 1
            
    return cnt