def solution(s):
    answer = ''

    for i in s:
        if answer == '': # 첫 단어 시작
            answer = i.lower()
            answer = i[0].upper()
            continue
        if i == ' ': # 공백이면 바로 공백 적용
            answer += i
        else: # 현재는 공백이 아닐경우
            if answer[-1] == ' ': # 바로 전이 공백
                    answer += i.upper() # 영어일 경우 대문자
            else:
                answer += i.lower()

    return answer