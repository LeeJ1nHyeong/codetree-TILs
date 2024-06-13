n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
herbicide = [[0] * n for _ in range(n)]


# 나무가 있는지 확인
def is_alive():
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                return True

    return False

# 초기 성장
def grow():
    next_board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                continue

            if board[i][j] == -1:
                next_board[i][j] = -1

            else:
                cnt = 0
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = i + di, j + dj

                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    if board[ni][nj] > 0:
                        cnt += 1

                next_board[i][j] = board[i][j] + cnt

    return next_board


def breed():
    next_board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                continue

            if board[i][j] == -1:
                next_board[i][j] = -1
                continue

            next_board[i][j] = board[i][j]
            breed_list = []

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj

                if ni < 0 or ni == n or nj < 0 or nj == n:
                    continue

                if board[ni][nj] > 0 or board[ni][nj] == -1:
                    continue

                if herbicide[ni][nj] >= year:
                    continue

                breed_list.append((ni, nj))

            if breed_list:
                for bi, bj in breed_list:
                    next_board[bi][bj] += board[i][j] // len(breed_list)

    return next_board


# 조건에 맞는 위치 확인
def check(cnt, max_cnt, i, j, max_i, max_j):
    if cnt < max_cnt:
        return False

    if cnt == max_cnt:
        if i > max_i:
            return False

        if i == max_i:
            if j > max_j:
                return False

    return True


dead_tree = 0

# print("init----------")
# for b in board:
#     print(*b)

# print()

for year in range(1, m + 1):
    # print(f"year = {year}")

    # 나무가 있는지 확인
    if not is_alive():
        break

    # 초기 성장
    board = grow()

    # print("grow----------")
    # for b in board:
    #     print(*b)

    # 번식
    board = breed()

    # print("breed----------")
    # for b in board:
    #     print(*b)

    # 제초제 위치 선정
    max_cnt = 0
    max_i, max_j = n, n

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                cnt = board[i][j]
                for di, dj in (-1, -1), (-1, 1), (1, 1), (1, -1):
                    for l in range(1, k + 1):
                        ni, nj = i + di * l, j + dj * l

                        if ni < 0 or ni == n or nj < 0 or nj == n:
                            break

                        if board[ni][nj] <= 0:
                            break

                        cnt += board[ni][nj]

                if check(cnt, max_cnt, i, j, max_i, max_j):
                    max_cnt = cnt
                    max_i, max_j = i, j

    # print("herbicide----------")
    # print(max_i, max_j, max_cnt)

    # 제초제 뿌리기
    dead_tree += board[max_i][max_j]
    board[max_i][max_j] = 0
    herbicide[max_i][max_j] = year + c

    for di, dj in (-1, -1), (-1, 1), (1, 1), (1, -1):
        for l in range(1, k + 1):
            ni, nj = max_i + di * l, max_j + dj * l

            if ni < 0 or ni == n or nj < 0 or nj == n:
                break

            if board[ni][nj] <= 0:
                herbicide[ni][nj] = year + c
                break

            dead_tree += board[ni][nj]
            board[ni][nj] = 0
            herbicide[ni][nj] = year + c

    # print("제초제 뿌린 후----------")
    # for b in board:
    #     print(*b)

    # print("herbicide----------")
    # for h in herbicide:
    #     print(*h)

    # print("dead----------")
    # print(dead_tree)

    # print()

print(dead_tree)