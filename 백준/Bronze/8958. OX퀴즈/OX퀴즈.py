n = int(input())
for _ in range(n):
    quiz = input()
    if quiz[0] == "O":
        a = [1]
    else:
        a = [0]
    for j in quiz[1:]:
        if j == "O":
            a.append(a[-1]+1)
        else:
            a.append(0)
    print(sum(a))