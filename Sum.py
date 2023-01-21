
x = int(input())
ans = []
for i in range(x):
    sets = input().split()
    if int(sets[2]) == int(sets[0]) + int(sets[1]) or int(sets[1]) == int(sets[0]) + int(sets[2]) or int(sets[0]) == int(sets[1]) + int(sets[2]):
        ans.append('yes')
    else:
        ans.append('no')
for i in ans:
    print(i)
