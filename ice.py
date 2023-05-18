n, x, t = map(int, input().split())
statues = list(map(int, input().split()))

abses = list()

for i in range(n):
    abses.append((i, (abs(x - statues[i]))))
ans = 0
ans_list = list()
abses_sorted = sorted(abses, key=lambda x: x[1])
for id, item in abses_sorted:
    if item <= t:
        ans += 1
        ans_list.append(id + 1)
        t -= item
print(ans)
print(*ans_list)
