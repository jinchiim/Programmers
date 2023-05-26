n = int(input()) # 관찰 횟수 N
cross = [2] * 11
answer = 0

for _ in range(n):
    cow, x = map(int, input().split())
    if cross[cow] != 2 and  cross[cow] != x:
        answer += 1
    cross[cow] = x
    
print(answer)
