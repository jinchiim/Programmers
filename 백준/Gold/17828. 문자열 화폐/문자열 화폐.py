n,m = map(int, input().split()) #  count , num

answer = ['A'] * n

if n * 26 < m or n > m:
    print("!")
    
else:
    m -= n
    i = n - 1
    
    while m > 0:
        if m > 26:      # 남은 수기 26p보다 큰 경우
            answer[i] = 'Z'
            i -= 1
            m -= 25
        else:
            answer[i] = chr(m + 65) # 대문자 이므로 65부터 시작
            break
            
    print("".join(answer))