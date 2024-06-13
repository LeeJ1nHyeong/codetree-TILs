from collections import deque


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score = 0

red_bomb = []

for i in range(n):
    for j in range(n):
        if not board[i][j]:
            red_bomb.append((i, j))


# 폭탄 묶음 탐색
def search():
    return

# 폭탄 터뜨리기
def bomb():
    return

# 중력 작용
def gravity():
    for j in range(n):
        move = 0
        for i in range(n - 1, -1, -1):
            if board[i][j] == m + 1:
                move += 1

            else:
                if board[i][j] == -1:
                    move = 0
                else:
                    if move:
                        board[i + move][j] = board[i][j]
                        board[i][j] = m + 1

# 반시계 방향 90도 회전
def rotate():
    next_board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            next_board[n - 1 - j][i] = board[i][j]

    return next_board


while True:
# for _ in range(1):
    # 폭탄 묶음 탐색
    max_bomb_cnt = 0
    max_red_bomb_cnt = 0
    max_i, max_j = n, n
    max_target = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 빨간 폭탄(0)이나 검은색 돌(-1)은 탐색 제외
            if board[i][j] <= 0:
                continue

            # 빈 칸 (m + 1)은 제외
            if board[i][j] == m + 1:
                continue

            # 방문지역은 탐색 제외
            if visited[i][j]:
                continue

            # 빨간색 폭탄 방문 표시 해제
            for ri, rj in red_bomb:
                visited[ri][rj] = 0

            target = board[i][j]
            queue = deque([(i, j)])
            visited[i][j] = 1

            bomb_cnt = 1
            red_bomb_cnt = 0
            center_i, center_j = i, j

            while queue:
                ci, cj = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = ci + di, cj + dj

                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    if board[ni][nj] != target:
                        if board[ni][nj]:
                            continue
                    
                    if visited[ni][nj]:
                        continue

                    bomb_cnt += 1
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                    # 빨간색 폭탄인지 확인
                    if not board[ni][nj]:
                        red_bomb_cnt += 1

                    # 빨간색 폭탄이 아니라면 기준점 여부 확인
                    else:
                        if ni < center_i:
                            continue
                        
                        if ni == center_i:
                            if nj > center_j:
                                continue

                        center_i, center_j = ni, nj

            # 폭탄 수가 2개 미만이면 제외
            if bomb_cnt < 2:
                continue

            # 가장 큰 폭탄 묶음인지 확인
            if bomb_cnt < max_bomb_cnt:
                continue

            if bomb_cnt == max_bomb_cnt:
                if red_bomb_cnt > max_red_bomb_cnt:
                    continue

                if red_bomb_cnt == max_red_bomb_cnt:
                    if center_i < max_i:
                        continue

                    if center_i == max_i:
                        if center_j > max_j:
                            continue

            max_bomb_cnt = bomb_cnt
            max_red_bomb_cnt = red_bomb_cnt
            max_i, max_j = center_i, center_j
            max_target = target

    # print("폭탄 기준점 위치----------")
    # print(max_i, max_j)

    # 폭탄 묶음이 없으면 while문 종료
    if (max_i, max_j) == (n, n):
        break

    # 폭탄 터뜨리기
    ## 빈칸을 m + 1로 구현
    target = max_target
    visited = [[0] * n for _ in range(n)]
    board[max_i][max_j] = m + 1
    queue = deque([(max_i, max_j)])
    visited[max_i][max_j] = 1

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == n or nj < 0 or nj == n:
                continue
            
            if board[ni][nj] != target:
                if board[ni][nj]:
                    continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            board[ni][nj] = m + 1
            queue.append((ni, nj))

    score += max_bomb_cnt ** 2

    # print("bomb----------")
    # for b in board:
    #     print(*b)

    # 중력 작용
    gravity()

    # print("1st gravity----------")
    # for b in board:
    #     print(*b)

    # 반시계 방향 90도 회전
    board = rotate()

    # print("rotate----------")
    # for b in board:
    #     print(*b)
    
    # 회전 후 중력 작용
    gravity()

#     print("2nd gravity----------")
#     for b in board:
#         print(*b)

#     print()

# for b in board:
#     print(*b)

print(score)