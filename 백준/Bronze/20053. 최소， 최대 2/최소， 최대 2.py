t = int(input())
for i in range(t):
        n = int(input())
        case = list(map(int, input().split(" ")))
        print(min(case), max(case))