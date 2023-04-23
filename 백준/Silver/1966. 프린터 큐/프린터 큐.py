t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    queue = list(map(int, input().split()))
    idx_list = [[p,x] for p,x in enumerate(queue)]
    queue.sort(reverse = True)
    
    cnt = 0
    while True:
        if queue[0] == idx_list[0][1]:
            cnt += 1
            
            if idx_list[0][0] == m:
                print(cnt)
                break
            else:
                queue.pop(0)
                idx_list.pop(0)
        else:
            idx_list.append(idx_list.pop(0))