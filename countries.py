n = int(input())

min_salary = list(map(int, input().split()))
is_educated = list(map(int, input().split()))
is_family = list(map(int, input().split()))

q = int(input())

salary = list(map(int, input().split()))
educated = list(map(int, input().split()))
family = list(map(int, input().split()))

ans = list()

for i in range(q):
    for j in range(n):
        enough_salary = False
        enough_education = False
        enough_family = False

        if salary[i] >= min_salary[j]:
            enough_salary = True
        if educated[i] >= is_educated[j]:
            enough_education = True
        if family[i] == j + 1 and is_family[j] == 1:
            enough_family = True

        if (enough_salary and enough_education) or enough_family:
            ans.append(j + 1)
            break
    if len(ans) == i:
        ans.append(0)
print(*ans)
