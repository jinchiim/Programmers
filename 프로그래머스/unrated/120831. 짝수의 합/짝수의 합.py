def solution(n):
    0 < n <= 1000
    sum = 0
    for answer in range(1,n+1):
        if answer % 2 == 0:
            sum += answer
    return sum