from collections import deque


def down(i, j):
    
    for di, dj in (1, -1), (2, 0), (1, 1):
        ni, nj = i + di, j + dj

        if ni >= r + 3 or forest[ni][nj]:
            return False

    return True


def rotate_left(i, j):

    for di, dj in (-1, -1), (0, -2), (1, -1), (1, -2), (2, -1):
        ni, nj = i + di, j + dj

        if (ni >= r + 3 or nj < 0) or forest[ni][nj]:
            return False

    return True


def rotate_right(i, j):

    for di, dj in (-1, 1), (0, 2), (1, 1), (1, 2), (2, 1):
        ni, nj = i + di, j + dj

        if (ni >= r + 3 or nj >= c) or forest[ni][nj]:
            return False

    return True


def clean():
    for i in range(r + 3):
        for j in range(c):
            forest[i][j] = 0


def bfs(i, j):
    visited = [[0] * c for _ in range(r + 3)]

    max_i = 0

    queue = deque([(i, j)])
    visited[i][j] = 1

    while queue:
        ci, cj = queue.popleft()

        max_i = max(max_i, ci - 2)

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == r + 3 or nj < 0 or nj == c:
                continue

            if not forest[ni][nj]:
                continue

            if visited[ni][nj]:
                continue

            if abs(forest[ni][nj]) != abs(forest[ci][cj]):
                if forest[ci][cj] > 0:
                    continue

            visited[ni][nj] = 1
            queue.append((ni, nj))

    return max_i


r, c, k = map(int, input().split())
forest = [[0] * c for _ in range(r + 3)]
ans = 0

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for num in range(1, k + 1):
    j, d = map(int, input().split())
    j -= 1
    i = 1

    while True:
        # 아래로 이동
        if down(i, j):
            i += 1
            continue

        # 왼쪽으로 회전
        if rotate_left(i, j):
            i += 1
            j -= 1
            d = (d - 1) % 4
            continue

        # 오른쪽으로 회전
        if rotate_right(i, j):
            i += 1
            j += 1
            d = (d + 1) % 4
            continue

        # 이동 불가라면 while문 종료
        break

    # 골렘 일부가 숲을 벗어났다면 숲 초기화 후 다음 골렘부터 새로 탐색
    if i <= 3:
        clean()
        continue

    # 골렘 위치를 숲에 저장
    forest[i][j] = num
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if k == d:
            forest[ni][nj] = -num
        else:
            forest[ni][nj] = num

    spirit_i, spirit_j = i, j

    ans += bfs(spirit_i, spirit_j)

print(ans)