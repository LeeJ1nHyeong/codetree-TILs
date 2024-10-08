def backtrack(i, j, cnt, s):
    global ans

    if cnt == 4:
        ans = max(s, ans)
        return

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj

        if ni < 0 or ni == n or nj < 0 or nj == m:
            continue

        if visited[ni][nj]:
            continue

        visited[ni][nj] = 1
        backtrack(ni, nj, cnt + 1, s + board[ni][nj])
        visited[ni][nj] = 0


def t_block(i, j):
    global ans

    center = board[i][j]
    t = []

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj

        if ni < 0 or ni == n or nj < 0 or nj == m:
            continue

        t.append(board[ni][nj])

    if len(t) >= 3:
        t.sort(reverse=True)
        t_sum = center + sum(t[:3])

        ans = max(t_sum, ans)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue

        visited[i][j] = 1
        backtrack(i, j, 1, board[i][j])
        visited[i][j] = 0
        
        t_block(i, j)

print(ans)