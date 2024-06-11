from collections import deque


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
person = [(n, n)] * (m + 1)  # 각 사람의 좌표
store = [(n, n)]

# 각 번호 별 목표 편의점 저장
for _ in range(m):
    i, j = map(int, input().split())
    store.append((i - 1, j - 1))

# 편의점 도착 여부
arrive = [0] * (m + 1)

t = 0  # 시간

# print("init----------")
# for b in board:
#     print(*b)

while sum(arrive) != m:
    t += 1

    change_wall = []
    # 한 칸씩 이동
    for num in range(1, m + 1):
        # 도착한 사람의 번호는 제외
        if arrive[num]:
            continue

        i, j = person[num]
        
        # 좌표를 부여받지 않았다면 continue
        if (i, j) == (n, n):
            continue

        si, sj = store[num]

        move_i, move_j = n, n

        # 최단거리로 갈 수 있는 방향 탐색
        queue = deque([(i, j)])
        visited = [[0] * n for _ in range(n)]
        visited[i][j] = 1

        prev_i = [[0] * n for _ in range(n)]
        prev_j = [[0] * n for _ in range(n)]

        while queue:
            ci, cj = queue.popleft()

            if (ci, cj) == (si, sj):
                break

            for di, dj in (-1, 0), (0, -1), (0, 1), (1, 0):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == n:
                    continue

                if visited[ni][nj]:
                    continue

                if board[ni][nj] == -1:
                    continue

                visited[ni][nj] = 1
                prev_i[ni][nj] = ci
                prev_j[ni][nj] = cj
                queue.append((ni, nj))
        
        # 역추적 진행
        now_i, now_j = si, sj

        while True:
            if prev_i[now_i][now_j] == i and prev_j[now_i][now_j] == j:
                move_i, move_j = now_i, now_j
                break

            now_i, now_j = prev_i[now_i][now_j], prev_j[now_i][now_j]

        person[num] = (move_i, move_j)

        # 목표 편의점에 도착했다면 도착 표시 후 해당 지역 벽(-1)으로 변환
        if (move_i, move_j) == store[num]:
            arrive[num] = 1
            change_wall.append((move_i, move_j))

    if sum(arrive) == m:
        break

    # 해당 시간에 모든 사람들이 움직인 후 change_wall에 있는 모든 좌표들을 벽으로 교체
    for i, j in change_wall:
        board[i][j] = -1

    # print("move----------")
    # for b in board:
    #     print(*b)

    # t <= m인 t번은 베이스 캠프로 이동
    if t <= m:
        num = t
        min_bi, min_bj = n, n

        # 목표 편의점에서 이동가능한 가장 가까운 베이스캠프 탐색
        si, sj = store[num]

        queue = deque([(si, sj, 0)])
        visited = [[0] * n for _ in range(n)]
        visited[si][sj] = 1

        min_cnt = n * n
        while queue:
            ci, cj, cnt = queue.popleft()

            if cnt > min_cnt:
                continue

            if board[ci][cj] == 1:
                if cnt == min_cnt:
                    if ci > min_bi:
                        continue

                    if ci == min_bi:
                        if cj > min_bj:
                            continue

                min_cnt = cnt
                min_bi, min_bj = ci, cj
                continue

            for di, dj in (-1, 0), (0, -1), (0, 1), (1, 0):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == n:
                    continue

                if visited[ni][nj]:
                    continue

                if board[ni][nj] == -1:
                    continue

                visited[ni][nj] = 1
                queue.append((ni, nj, cnt + 1))

        person[num] = (min_bi, min_bj)
        board[min_bi][min_bj] = -1

    # print("basecamp----------")
    # for b in board:
    #     print(*b)

    # print("person----------")
    # print(person)

    # print("store----------")
    # print(store)

    # print("arrive----------")
    # print(arrive)

    # print()


print(t)