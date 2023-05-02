lists = [1] + [0] * 31
for _ in range(28):
    i = int(input())
    lists[i] = 1


print(lists.index(0))
lists.pop(lists.index(0))
print(lists.index(0)+1)