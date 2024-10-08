from collections import deque

def backtrack(cnt):

    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if board[i][j]:
                continue

            board[i][j] = 1
            backtrack(cnt + 1)
            board[i][j] = 0


def bfs():
    global ans

    queue = deque(fire)
    visited = [[0] * m for _ in range(n)]

    while queue:
        i, j = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj

            if ni < 0 or ni == n or nj < 0 or nj == m:
                continue
            
            if board[ni][nj]:
                continue
            
            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj))

    cnt = 0

    for i in range(n):
        for j in range(m):
            if not board[i][j] and not visited[i][j]:
                cnt += 1

    ans = max(cnt, ans)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

fire = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            fire.append((i, j))

ans = 0

backtrack(0)

print(ans)