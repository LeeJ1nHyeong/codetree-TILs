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
                    next_maze[i][j] += maze[i][j]

            elif maze[i][j] > 0:
                next_maze[i][j] = maze[i][j]

    return next_maze


def min_square():
    global min_size, min_i, min_j

    for size in range(2, n + 1):
        for i1 in range(n - size + 1):
            for j1 in range(n - size + 1):
                i2, j2 = i1 + size - 1, j1 + size - 1

                if not (i1 <= exit_i <= i2 and j1 <= exit_j <= j2):
                    continue

                for i in range(i1, i2 + 1):
                    for j in range(j1, j2 + 1):
                        if maze[i][j] < 0:
                            min_size = size
                            min_i, min_j = i1, j1
                            return


def rotate(min_i, min_j, size):
    global exit_i, exit_j

    rotate_maze = [[0] * n for _ in range(n)]
    rotate_exit_i, rotate_exit_j = 0, 0
    for i in range(n):
        for j in range(n):
            rotate_maze[i][j] = maze[i][j]

    for i in range(size):
        for j in range(size):
            if maze[min_i + i][min_j + j] > 0:
                maze[min_i + i][min_j + j] -= 1

            if min_i + i == exit_i and min_j + j == exit_j:
                rotate_exit_i, rotate_exit_j = min_i + j, min_j + (size - 1) - i

            rotate_maze[min_i + j][min_j + (size - 1) - i] = maze[min_i + i][min_j + j]

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

min_size, min_i, min_j = 0, 0, 0

move_cnt = 0

# print("maze----------init")
# for m in maze:
#     print(*m)
for _ in range(k):
    maze = move()

    # print("maze----------first")
    # for m in maze:
    #     print(*m)

    # print("first move cnt---------")
    # print(move_cnt)

    if not participate:
        break
    
    min_square()
    # print("square----------")
    # print(min_i, min_j, min_size)

    maze = rotate(min_i, min_j, min_size)

    # print("maze----------rotate")
    # for m in maze:
    #     print(*m)
    # print("rotate move cnt---------")
    # print(move_cnt)
    # print("rotate exit----------")
    # print(exit_i, exit_j)
    # print()

print(move_cnt)
print(exit_i + 1, exit_j + 1)