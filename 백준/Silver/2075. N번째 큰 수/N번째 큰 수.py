n = int(input())
nums = []
for i in range(n):
    nums += list(map(int,input().split()))
    nums.sort(reverse=True)
    nums = nums[:n]
print(nums[-1])