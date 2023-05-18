n = int(input())
ids = list(map(int, input().split()))
rows = list(map(int, input().split()))

k = int(input())
text = list(map(int, input().split()))

my_dict = dict()

for i in range(n):
    my_dict[ids[i]] = rows[i]

ans = 0
prev = my_dict[text[0]]
for i in range(1, k):
    if prev != my_dict[text[i]]:
        ans += 1
    prev = my_dict[text[i]]
print(ans)
