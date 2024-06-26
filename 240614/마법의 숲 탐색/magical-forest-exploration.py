from collections import deque


r, c, k = map(int, input().split())

# 북쪽에서 시작하기 때문에 위 3줄을 추가
forest = [[0] * c for _ in range(r + 3)]

g_di = [-1, 0, 1, 0]
g_dj = [0, 1, 0, -1]

ans = 0  # 최대로 위치한 행의 총 합

# 숲 초기화
def clear_forest():
    for i in range(r + 3):
        for j in range(c):
            forest[i][j] = 0

# 조건 확인
def check(ni, nj):
    # 범위 밖을 벗어나거나 골렘이 있다면 False return
    if ni < 0 or ni >= r + 3 or nj < 0 or nj >= c:
        return False

    if forest[ni][nj]:
        return False

    return True


# 아래로 이동
def down(i, j):
    # 아래쪽 3곳 비었는지 확인
    for di, dj in (1, -1), (2, 0), (1, 1):
        ni, nj = i + di, j + dj

        # 이동 조건을 만족하지 못했다면 False return
        if not check(ni, nj):
            return False

    return True  # 이동 조건을 만족했다면 True return


# 왼쪽으로 회전
def rotate_left(i, j):

    # 왼쪽 3곳 비었는지 확인
    for di, dj in (1, -1), (0, -2), (-1, -1):
        ni, nj = i + di, j + dj

        # 이동 조건을 만족하지 못했다면 False return
        if not check(ni, nj):
            return False

    # 이 후 아래쪽 2곳 비었는지 확인
    for di, dj in (1, -2), (2, -1):
        ni, nj = i + di, j + dj

        # 이동 조건을 만족하지 못했다면 False return
        if not check(ni, nj):
            return False

    return True


# 오른쪽으로 회전
def rotate_right(i, j):

    # 오른쪽 3곳 비었는지 확인
    for di, dj in (1, 1), (0, 2), (-1, 1):
        ni, nj = i + di, j + dj

        # 이동 조건을 만족하지 못했다면 False return
        if not check(ni, nj):
            return False

    # 이 후 아래쪽 2곳 비었는지 확인
    for di, dj in (1, 2), (2, 1):
        ni, nj = i + di, j + dj

        # 이동 조건을 만족하지 못했다면 False return
        if not check(ni, nj):
            return False

    return True


# bfs
def bfs(i, j):
    ## 절댓값이 같은 곳은 자유 이동
    ## 절댓값이 다를 때 현재 위치가 출구(음수값)이라면 이동 가능
    ## 위 세줄 추가한 거 생각해야함
    
    # bfs 초기 세팅
    visited = [[0] * c for _ in range(r + 3)]
    visited[i][j] = 1
    queue = deque([(i, j)])

    max_i = 0  # 최대한 남쪽으로 이동했을 때의 행

    # bfs 진행
    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 3 or ni == r + 3 or nj < 0 or nj == c:
                continue

            if not forest[ni][nj]:
                continue

            if visited[ni][nj]:
                continue

            # 다른 골렘으로 이동할 때 현재 위치가 출구가 아니라면 continue
            if abs(forest[ci][cj]) != abs(forest[ni][nj]):
                if forest[ci][cj] > 0:
                    continue

            visited[ni][nj] = 1
            queue.append((ni, nj))

            # 최대로 남쪽으로 이동했는지 확인
            max_i = max(max_i, ni - 2)

    return max_i


for num in range(1, k + 1):
    j, d = map(int, input().split())  # 시작 열, 출구 방향
    j -= 1

    # 이동할 수 없을 때까지 아래, 왼쪽 회전, 오른쪽 회전 진행
    next_d = d
    i = 1
    while True:
        # 아래로 이동
        if down(i, j):
            i += 1
            continue

        # 왼쪽 회전 시 출구 반시계 방향으로 회전
        if rotate_left(i, j):
            i += 1
            j -= 1
            next_d = (next_d - 1) % 4
            continue

        # 오른쪽 회전 시 출구 시계 방향으로 회전
        if rotate_right(i, j):
            i += 1
            j += 1
            next_d = (next_d + 1) % 4
            continue

        break

    # 이동 종료 후 골렘이 겪자 밖을 벗어났다면 숲 초기화 후 다음 골렘으로 넘기기
    if i <= 3:
        clear_forest()
        continue

    # 정령 시작 위치
    spirit_i, spirit_j = i, j

    # 골렘을 숲에 구현
    ## 출구는 음수로 표현
    forest[i][j] = num
    for k in range(4):
        ni, nj = i + g_di[k], j + g_dj[k]
        if k == next_d:
            forest[ni][nj] = -num
        else:
            forest[ni][nj] = num

    # 정령 이동
    ## bfs 진행하면서 최대 행 더해주기
    ans += bfs(spirit_i, spirit_j)

# 최대로 위치한 행의 총 합
print(ans)