n = int(input())
for _ in range(n):
    quiz = input().split('X')
    quiza = [(len(i)*(len(i)+1)//2) for i in quiz]
    print(sum(quiza))