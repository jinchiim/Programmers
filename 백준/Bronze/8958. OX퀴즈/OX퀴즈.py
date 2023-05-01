n = int(input())
for _ in range(n):
    quiz = input().split('X')
    print(sum([(len(i)*(len(i)+1)//2) for i in quiz]))