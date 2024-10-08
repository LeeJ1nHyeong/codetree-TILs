def backtrack(idx, s):
    global min_sum, max_sum

    if idx == n:
        min_sum = min(s, min_sum)
        max_sum = max(s, max_sum)
        return

    if calculator[0]:
        calculator[0] -= 1
        backtrack(idx + 1, s + num[idx])
        calculator[0] += 1

    if calculator[1]:
        calculator[1] -= 1
        backtrack(idx + 1, s - num[idx])
        calculator[1] += 1

    if calculator[2]:
        calculator[2] -= 1
        backtrack(idx + 1, s * num[idx])
        calculator[2] += 1


n = int(input())
num = list(map(int, input().split()))
calculator = list(map(int, input().split()))

min_sum, max_sum = 1e9, -1e9

backtrack(1, num[0])

print(min_sum, max_sum)