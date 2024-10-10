n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
herbicide = [[0] * n for _ in range(n)]  # 제초제
dead_tree = 0  # 박멸한 나무의 수


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
            # 빈 칸은 제외
            if not board[i][j]:
                continue

            # 벽 위치 그대로 복사
            if board[i][j] == -1:
                next_board[i][j] = -1

            else:
                # 나무가 있는 위치로부터 4방향 탐색하여 나무 수만큼 성장
                cnt = 0
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = i + di, j + dj

                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    if board[ni][nj] > 0:
                        cnt += 1

                next_board[i][j] = board[i][j] + cnt

    return next_board

# 번식
def breed():
    next_board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 빈 칸은 제외
            if not board[i][j]:
                continue

            # 벽 위치 그대로 복사
            if board[i][j] == -1:
                next_board[i][j] = -1
                continue

            # 나무가 있는 위치에서 번식 진행
            next_board[i][j] = board[i][j]
            breed_list = []  # 번식할 위치

            # 나무가 있는 위치로부터 인접한 4방향 탐색
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj

                # 범위를 벗어나거나 나무 또는 벽이 있을 경우는 제외
                if ni < 0 or ni == n or nj < 0 or nj == n:
                    continue
                if board[ni][nj] > 0 or board[ni][nj] == -1:
                    continue

                # 제초제가 남아있는 위치는 제외
                if herbicide[ni][nj] >= year:
                    continue

                # 조건을 만족하는 위치는 breed_list에 추가
                breed_list.append((ni, nj))

            # 번식 가능한 위치가 있을 경우 나무 수를 번식 위치 수만큼 나눈 몫만큼 번식 진행
            if breed_list:
                for bi, bj in breed_list:
                    next_board[bi][bj] += board[i][j] // len(breed_list)

    return next_board

# 제초제 위치 선정
def select_herbicide():
    max_cnt = 0  # 박멸할 수 있는 최대 나무 수
    max_i, max_j = n, n  # 그 때의 위치

    for i in range(n):
        for j in range(n):
            # 나무가 있는 위치 탐색
            if board[i][j] > 0:
                # 박멸 가능한 나무 수
                cnt = board[i][j]

                # 현재 위치로부터 대각선 방향으로 k칸까지 탐색
                for di, dj in (-1, -1), (-1, 1), (1, 1), (1, -1):
                    for l in range(1, k + 1):
                        ni, nj = i + di * l, j + dj * l

                        # 범위를 벗어나면 진행 방향 종료
                        if ni < 0 or ni == n or nj < 0 or nj == n:
                            break

                        # 빈 칸이거나 벽을 만나면 진행 방향 종료
                        if board[ni][nj] <= 0:
                            break

                        # 나무 수 추가
                        cnt += board[ni][nj]

                # 조건에 맞는 위치라면 최신화
                if check(cnt, max_cnt, i, j, max_i, max_j):
                    max_cnt = cnt
                    max_i, max_j = i, j

    return max_i, max_j  # 나무를 최대로 박멸 가능한 위치 return

# 조건에 맞는 위치 확인
def check(cnt, max_cnt, i, j, max_i, max_j):
    # 나무를 최대로 박멸가능한 위치, 같다면 행이 작은 위치, 행이 같다면 열이 작은 위치로 선정
    if cnt < max_cnt:
        return False

    if cnt == max_cnt:
        if i > max_i:
            return False

        if i == max_i:
            if j > max_j:
                return False

    return True

# 제초제 뿌리기
def spread_herbicide(max_i, max_j):

    # 제초제 뿌리기
    kill_tree(max_i, max_j)

    # 제초제 뿌린 위치로부터 대각선 방향으로 진행
    for di, dj in (-1, -1), (-1, 1), (1, 1), (1, -1):
        # 1칸부터 k칸까지 진행
        for l in range(1, k + 1):
            ni, nj = max_i + di * l, max_j + dj * l

            # 범위 벗어나면 진행 방향 종료
            if ni < 0 or ni == n or nj < 0 or nj == n:
                break

            # 벽이거나 나무가 없는 곳은 제초제 뿌리기 저장만 하고 진행 방향 종료
            if board[ni][nj] <= 0:
                herbicide[ni][nj] = year + c
                break

            # 제초제 뿌리기
            kill_tree(ni, nj)

# 나무 박멸
def kill_tree(i, j):
    global dead_tree
    
    # 해당 자리의 나무를 없애기
    dead_tree += board[i][j]
    board[i][j] = 0

    # 제초제 뿌리기
    herbicide[i][j] = year + c


# m년까지 진행
for year in range(1, m + 1):
    # 살아있는 나무가 없으면 종료
    if not is_alive():
        break

    # 초기 성장
    board = grow()

    # 번식
    board = breed()

    # 제초제 위치 선정
    max_i, max_j = select_herbicide()

    # 제초제 뿌리기
    spread_herbicide(max_i, max_j)

# 박멸한 나무 수 출력
print(dead_tree)