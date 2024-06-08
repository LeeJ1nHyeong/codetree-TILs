from collections import deque


def rotate(ci, cj):
    global max_rotate
    global max_i, max_j
    global max_rotate_angle
    global gain_list

    r, c = ci - 1, cj - 1

    rotate_90 = [[0] * 5 for _ in range(5)]
    rotate_180 = [[0] * 5 for _ in range(5)]
    rotate_270 = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            rotate_90[i][j] = board[i][j]
            rotate_180[i][j] = board[i][j]
            rotate_270[i][j] = board[i][j]

    for i in range(3):
        for j in range(3):
            rotate_90[r + j][c + 2 - i] = board[r + i][c + j]
            rotate_180[r + 2 - i][c + 2 - j] = board[r + i][c + j]
            rotate_270[r + 2 - j][c + i] = board[r + i][c + j]

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


def bfs(rotate_board):
    visited = [[0] * 5 for _ in range(5)]

    gain_list = []
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                visited[i][j] = 1
                target = rotate_board[i][j]
                part_gain_list = [(i, j)]
                queue = deque([(i, j)])

                while queue:
                    ci, cj = queue.popleft()

                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        ni, nj = ci + di, cj + dj

                        if ni < 0 or ni == 5 or nj < 0 or nj == 5:
                            continue

                        if rotate_board[ni][nj] != target:
                            continue

                        if visited[ni][nj]:
                            continue

                        visited[ni][nj] = 1
                        part_gain_list.append((ni, nj))
                        queue.append((ni, nj))

                if len(part_gain_list) >= 3:
                    gain_list += part_gain_list

    return gain_list


k, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]

piece = list(map(int, input().split()))

value = []

idx = 0
for _ in range(k):
    # print("board----------")
    # for b in board:
    #     print(*b)
    max_rotate = []
    max_rotate_angle = 360
    max_i, max_j = -1, -1
    gain_list = []

    cnt = 0

    for i in range(1, 4):
        for j in range(1, 4):
            rotate(i, j)

    if not gain_list:
        break

    # print("max_rotate----------init")
    # print(max_i, max_j, max_rotate_angle)
    # for mr in max_rotate:
    #     print(*mr)

    cnt += len(gain_list)
    gain_list.sort(key=lambda x: (x[1], -x[0]))

    for i, j in gain_list:
        max_rotate[i][j] = piece[idx]
        idx += 1

    # print("max_rotate----------first")
    # for mr in max_rotate:
    #     print(*mr)

    while True:
        add_gain_list = bfs(max_rotate)

        if not add_gain_list:
            break

        cnt += len(add_gain_list)
        add_gain_list.sort(key=lambda x: (x[1], -x[0]))
        for i, j in add_gain_list:
            max_rotate[i][j] = piece[idx]
            idx += 1

    #     print("max_rotate----------chain")
    #     for mr in max_rotate:
    #         print(*mr)

    # print("max_rotate----------final")
    # for mr in max_rotate:
    #     print(*mr)

    # print()

    value.append(cnt)
    # print(cnt)

    board = max_rotate

print(*value)