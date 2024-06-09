from collections import deque


def move():
    global move_cnt
    global participate

    next_maze = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] < 0:
                short_exit = abs(i - exit_i) + abs(j - exit_j)

                is_move = False
                for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
                    ni, nj = i + di, j + dj

                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    if maze[ni][nj] > 0:
                        continue

                    if short_exit < abs(ni - exit_i) + abs(nj - exit_j):
                        continue

                    move_cnt += -maze[i][j]
                    is_move = True
                    next_maze[ni][nj] += maze[i][j]
                    if ni == exit_i and nj == exit_j:
                        participate -= -next_maze[ni][nj]
                        next_maze[ni][nj] = 0
                    break

                if not is_move:
                    next_maze[i][j] = maze[i][j]

            elif maze[i][j] > 0:
                next_maze[i][j] = maze[i][j]

    return next_maze


def bfs():
    return


def rotate(min_i, min_j, min_square):
    global exit_i, exit_j

    rotate_maze = [[0] * n for _ in range(n)]
    rotate_exit_i, rotate_exit_j = 0, 0
    for i in range(n):
        for j in range(n):
            rotate_maze[i][j] = maze[i][j]

    for i in range(min_square):
        for j in range(min_square):
            if maze[min_i + i][min_j + j] > 0:
                maze[min_i + i][min_j + j] -= 1

            if min_i + i == exit_i and min_j + j == exit_j:
                rotate_exit_i, rotate_exit_j = min_i + j, min_j + (min_square - 1) - i

            rotate_maze[min_i + j][min_j + (min_square - 1) - i] = maze[min_i + i][min_j + j]

    exit_i, exit_j = rotate_exit_i, rotate_exit_j

    return rotate_maze


n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
participate = m

for _ in range(m):
    i, j = map(int, input().split())
    maze[i - 1][j - 1] -= 1

exit_i, exit_j = map(int, input().split())
exit_i -= 1
exit_j -= 1

move_cnt = 0

# print("maze----------init")
# for m in maze:
#     print(*m)
for _ in range(k):
    maze = move()

    # print("maze----------first")
    # for m in maze:
    #     print(*m)

    if not participate:
        break
                    
    min_square = n
    min_i, min_j = n, n

    visited = [[0] * n for _ in range(n)]
    queue = deque([(exit_i, exit_j)])
    visited[exit_i][exit_j] = 1

    while queue:
        i, j = queue.popleft()
        if maze[i][j] < 0:
            row_length, column_length = abs(i - exit_i) + 1, abs(j - exit_j) + 1
            if min_square < max(row_length, column_length):
                continue

            if min_square == max(row_length, column_length):
                if row_length >= column_length:
                    if min_i < min(i, exit_i):
                        continue
                    if min_i == min(i, exit_i):
                        if min_j < max(j, exit_j) - min_square + 1:
                            continue
                else:
                    if min_i < max(i, exit_i) - min_square + 1:
                        continue
                    if min_i == max(i, exit_i) - min_square + 1:
                        if min_j < min(j, exit_j):
                            continue

            min_square = max(row_length, column_length)
            if row_length >= column_length:
                min_i = min(i, exit_i)
                min_j = max(j, exit_j) - min_square + 1
                if min_j < 0:
                    min_j = 0

            else:
                min_i = max(i, exit_i) - min_square + 1
                if min_i < 0:
                    min_i = 0
                min_j = min(j, exit_j)
            continue

        for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
            ni, nj = i + di, j + dj

            if ni < 0 or ni == n or nj < 0 or nj == n:
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj))

    # print(min_i, min_j, min_square)

    maze = rotate(min_i, min_j, min_square)

    # print("maze----------rotate")
    # for m in maze:
    #     print(*m)
    # print(move_cnt, exit_i + 1, exit_j + 1)
    # print()


print(move_cnt)
print(exit_i + 1, exit_j + 1)