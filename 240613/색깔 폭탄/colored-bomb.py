from collections import deque


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score = 0

## 빈칸을 m + 1로 구현

# 폭탄 묶음 탐색
def search():
    max_bomb_cnt = 0
    max_red_bomb_cnt = 0
    max_i, max_j = n, n
    max_target = 0
    visited = [[0] * n for _ in range(n)]

    # 조건에 맞는 좌표인지 확인
    def check():
        # 가장 큰 폭탄 묶음, 크기가 같다면 빨간색 폭탄 수가 적은 묶음, 같다면 기준점의 행이 큰 묶음, 같다면 기준점의 열이 작은 묶음
        if bomb_cnt < max_bomb_cnt:
            return False

        if bomb_cnt == max_bomb_cnt:
            if red_bomb_cnt > max_red_bomb_cnt:
                return False

            if red_bomb_cnt == max_red_bomb_cnt:
                if center_i < max_i:
                    return False

                if center_i == max_i:
                    if center_j > max_j:
                        return False

        return True


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

            # bfs 초기 세팅
            target = board[i][j]
            queue = deque([(i, j)])
            visited[i][j] = 1

            bomb_cnt = 1
            red_bomb_cnt = 0
            center_i, center_j = i, j

            # bfs 진행
            while queue:
                ci, cj = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = ci + di, cj + dj

                    # 범위 밖을 벗어나면 continue
                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    if board[ni][nj] != target:
                        # 빨간색 폭탄이 아니면 continue
                        if board[ni][nj]:
                            continue
                    
                    # 방문 지역이라면 continue
                    if visited[ni][nj]:
                        continue

                    # 폭탄 개수 1 증가 후 방문 표시
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
            if check():
                max_bomb_cnt = bomb_cnt
                max_red_bomb_cnt = red_bomb_cnt
                max_i, max_j = center_i, center_j
                max_target = target

    return max_i, max_j, max_bomb_cnt

# 폭탄 터뜨리기
def bomb(max_i, max_j):
    target = board[max_i][max_j]  # 폭탄 번호
    visited = [[0] * n for _ in range(n)]  # 방문 여부

    # 기준점 위치를 빈칸(m + 1)으로 변경
    board[max_i][max_j] = m + 1

    # bfs 초기 세팅
    queue = deque([(max_i, max_j)])
    visited[max_i][max_j] = 1

    # bfs 진행
    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == n or nj < 0 or nj == n:
                continue
            
            if board[ni][nj] != target:
                # 빨간색 폭탄이 아니면 continue
                if board[ni][nj]:
                    continue

            # 방문 지역은 continue
            if visited[ni][nj]:
                continue

            # 방문 표시 후 빈칸으로 변경
            visited[ni][nj] = 1
            board[ni][nj] = m + 1
            queue.append((ni, nj))

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
    # 빨간색 폭탄 위치 탐색
    red_bomb = []
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                red_bomb.append((i, j))

    # 폭탄 묶음 탐색
    max_i, max_j, max_bomb_cnt = search()

    # 폭탄 묶음이 없으면 while문 종료
    if (max_i, max_j) == (n, n):
        break

    # 폭탄 터뜨리기
    bomb(max_i, max_j)

    # 점수 추가
    score += max_bomb_cnt ** 2

    # 중력 작용
    gravity()

    # 반시계 방향 90도 회전
    board = rotate()

    # 회전 후 중력 작용
    gravity()

print(score)