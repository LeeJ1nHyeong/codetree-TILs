from collections import deque

# 회전
def rotate(ci, cj):
    global max_rotate
    global max_i, max_j
    global max_rotate_angle
    global gain_list

    r, c = ci - 1, cj - 1  # 회전하는 위치 범위 설정

    # 90도, 180도, 270도 회전 후 유적 상태
    rotate_90 = [[0] * 5 for _ in range(5)]
    rotate_180 = [[0] * 5 for _ in range(5)]
    rotate_270 = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            rotate_90[i][j] = board[i][j]
            rotate_180[i][j] = board[i][j]
            rotate_270[i][j] = board[i][j]

    # 중심 좌표 기준 3X3 범위를 90도, 180도, 270도 회전
    for i in range(3):
        for j in range(3):
            rotate_90[r + j][c + 2 - i] = board[r + i][c + j]
            rotate_180[r + 2 - i][c + 2 - j] = board[r + i][c + j]
            rotate_270[r + 2 - j][c + i] = board[r + i][c + j]

    ## 90도, 180도, 270도 회전 시킨 후의 유적을 이용하여 bfs 진행
    ## 문제 조건에 따른 우선순위에 따라 최신화 여부 확인
    ## 1차 유물 획득 개수 가장 큰 경우 -> 회전 각도 작은 방법 -> 열 가장 작은 구간 -> 행 가장 작은 구간
    # 90도 회전
    gain_list_90 = bfs(rotate_90)
    if gain_list_90:
        is_max = True
        if len(gain_list_90) < len(gain_list):
            is_max = False

        if len(gain_list_90) == len(gain_list):
            if max_rotate_angle == 90:
                if max_j < cj:
                    is_max = False

                if max_j == cj:
                    if max_i < ci:
                        is_max = False

        if is_max:
            max_rotate = rotate_90
            max_rotate_angle = 90
            gain_list = gain_list_90
            max_i, max_j = ci, cj

    # 180도 회전
    gain_list_180 = bfs(rotate_180)
    if gain_list_180:
        is_max = True
        if len(gain_list_180) < len(gain_list):
            is_max = False

        if len(gain_list_180) == len(gain_list):
            if max_rotate_angle < 180:
                is_max = False

            if max_rotate_angle == 180:
                if max_j < cj:
                    is_max = False

                if max_j == cj:
                    if max_i < ci:
                        is_max = False
        if is_max:
            max_rotate = rotate_180
            max_rotate_angle = 180
            gain_list = gain_list_180
            max_i, max_j = ci, cj

    # 270도 회전
    gain_list_270 = bfs(rotate_270)
    if gain_list_270:
        is_max = True
        if len(gain_list_270) < len(gain_list):
            is_max = False

        if len(gain_list_270) == len(gain_list):
            if max_rotate_angle < 270:
                is_max = False

            if max_rotate_angle == 270:
                if max_j < cj:
                    is_max = False

                if max_j == cj:
                    if max_i < ci:
                        is_max = False
        if is_max:
            max_rotate = rotate_270
            max_rotate_angle = 270
            gain_list = gain_list_270
            max_i, max_j = ci, cj

# bfs
def bfs(rotate_board):
    visited = [[0] * 5 for _ in range(5)]

    gain_list = []  # 획득한 유물 좌표
    for i in range(5):
        for j in range(5):
            # 미방문 위치에서 bfs 진행
            if not visited[i][j]:
                visited[i][j] = 1
                target = rotate_board[i][j]  # 타겟
                part_gain_list = [(i, j)]  # 시작위치에서 얻은 유물 좌표
                queue = deque([(i, j)])

                while queue:
                    ci, cj = queue.popleft()

                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        ni, nj = ci + di, cj + dj

                        # 범위를 벗어나거나 타겟 번호가 아니거나 방문 좌표일 경우 continue
                        if ni < 0 or ni == 5 or nj < 0 or nj == 5:
                            continue
                        if rotate_board[ni][nj] != target:
                            continue
                        if visited[ni][nj]:
                            continue

                        # 방문 표시 후 유물 좌표를 추가한 뒤 queue에 좌표 추가
                        visited[ni][nj] = 1
                        part_gain_list.append((ni, nj))
                        queue.append((ni, nj))

                # 유물이 3개 이상 연결되어 있을 경우 유물 획득
                if len(part_gain_list) >= 3:
                    gain_list += part_gain_list

    return gain_list  # 획득한 유물 좌표 리스트 return


k, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
piece = list(map(int, input().split()))

value = []  # 획득한 유물

idx = 0  # 새로운 유물조각 번호
for _ in range(k):
    # 1차 획득 값이 가장 큰 경우의 데이터
    max_rotate = []  # 회전시킨 유적
    max_rotate_angle = 360  # 회전시킨 각도
    max_i, max_j = -1, -1  # 회전 중심 좌표
    gain_list = []  # 획득한 유물 좌표

    cnt = 0  # 해당 턴에 획득한 유물 개수

    # (1, 1) ~ (3, 3)까지 회전하여 탐색
    for i in range(1, 4):
        for j in range(1, 4):
            rotate(i, j)

    # 획득한 유물이 없을 경우 종료
    if not gain_list:
        break

    # 획득한 유물 개수 추가
    cnt += len(gain_list)
    # 열 오름차순, 행 내림차순으로 정렬
    gain_list.sort(key=lambda x: (x[1], -x[0]))

    # 획득한 유물 위치에 새로운 유물 조각 추가
    for i, j in gain_list:
        max_rotate[i][j] = piece[idx]
        idx += 1

    # 이 후 획득할 수 있는 유물이 없을 때까지 연쇄 획득 진행
    while True:
        add_gain_list = bfs(max_rotate)

        if not add_gain_list:
            break

        cnt += len(add_gain_list)
        add_gain_list.sort(key=lambda x: (x[1], -x[0]))
        for i, j in add_gain_list:
            max_rotate[i][j] = piece[idx]
            idx += 1

    # 해당 턴에 얻을 수 있는 유물 개수를 value에 추가
    value.append(cnt)

    # 유적 최신화
    board = max_rotate

print(*value)  # 획득한 유물 개수 출력