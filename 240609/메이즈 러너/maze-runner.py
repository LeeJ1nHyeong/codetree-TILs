from collections import deque


# 참가자 이동
def move():
    global move_cnt
    global participate

    next_maze = [[0] * n for _ in range(n)]  # 참가자가 이동한 후의 미로 상황

    for i in range(n):
        for j in range(n):
            # 참가자일 경우 출구와 가까워지는 방향으로 이동
            if maze[i][j] < 0:
                short_exit = abs(i - exit_i) + abs(j - exit_j)

                is_move = False  # 참가자 이동 여부 확인
                for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
                    ni, nj = i + di, j + dj

                    # 범위를 벗어나거나, 벽이거나 출구에서 멀어지는 방향일 경우 continue
                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue
                    if maze[ni][nj] > 0:
                        continue
                    if short_exit < abs(ni - exit_i) + abs(nj - exit_j):
                        continue

                    # 참가자 수 만큼 이동 횟수 증가
                    move_cnt += -maze[i][j]

                    # 참가자 이동 표시
                    is_move = True

                    # next_maze의 이동할 좌표에 인원 수 만큼 추가(음수)
                    # 참가자가 중복으로 존재할 수 있기 때문에 증가하는 방식으로 구현
                    next_maze[ni][nj] += maze[i][j]

                    # 다음 이동 위치가 출구일 경우 참가자 수 차감 및 다음 좌표 0으로 저장
                    if ni == exit_i and nj == exit_j:
                        participate -= -next_maze[ni][nj]
                        next_maze[ni][nj] = 0

                    # 참가자가 이동했다면 for문 종료
                    break

                # 참가자가 이동하지 않았을 경우 next_maze에 인원 수 만큼 추가(음수)
                # 참가자가 중복으로 존재할 수 있기 때문에 증가하는 방식으로 구현
                if not is_move:
                    next_maze[i][j] += maze[i][j]

            # 벽일 경우 next_maze에 그대로 복사
            elif maze[i][j] > 0:
                next_maze[i][j] = maze[i][j]

    return next_maze  # 참가자 이동 후 미로 상태 return


# 최소 정사각형 탐색
def min_square():
    global min_size, min_i, min_j

    # 크기가 2인 정사각형부터 탐색
    for size in range(2, n + 1):
        for i1 in range(n - size + 1):
            for j1 in range(n - size + 1):
                i2, j2 = i1 + size - 1, j1 + size - 1

                # 정사각형 범위에 출구가 없을 경우 continue
                if not (i1 <= exit_i <= i2 and j1 <= exit_j <= j2):
                    continue

                # 정사각형 범위에 참가자가 존재할 경우 정사각형 크기, 좌상단 좌표 저장 후 return
                for i in range(i1, i2 + 1):
                    for j in range(j1, j2 + 1):
                        if maze[i][j] < 0:
                            min_size = size
                            min_i, min_j = i1, j1
                            return


# 미로 회전
def rotate(min_i, min_j, size):
    global exit_i, exit_j

    rotate_maze = [[0] * n for _ in range(n)]  # 회전 후 미로
    rotate_exit_i, rotate_exit_j = 0, 0  # 회전 후 출구 좌표
    for i in range(n):
        for j in range(n):
            rotate_maze[i][j] = maze[i][j]

    # 지정한 범위 내에서 90도 회전 진행 
    for i in range(size):
        for j in range(size):
            # 벽일 경우 1 차감
            if maze[min_i + i][min_j + j] > 0:
                maze[min_i + i][min_j + j] -= 1

            # 출구 좌표일 경우 회전 후 출구 좌표에 따로 저장
            if min_i + i == exit_i and min_j + j == exit_j:
                rotate_exit_i, rotate_exit_j = min_i + j, min_j + (size - 1) - i

            rotate_maze[min_i + j][min_j + (size - 1) - i] = maze[min_i + i][min_j + j]

    # 회전 후 출구 좌표 최신화
    exit_i, exit_j = rotate_exit_i, rotate_exit_j

    return rotate_maze  # 회전 후 미로 return


n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
participate = m

# 참가자들의 위치를 미로에 음수값으로 저장
# 한 위치에 여러 참가자가 있을 수 있기 때문에 차감하는 식으로 구현
for _ in range(m):
    i, j = map(int, input().split())
    maze[i - 1][j - 1] -= 1

# 출구 좌표 (편의를 위해 인덱스 형태로 진행)
exit_i, exit_j = map(int, input().split())
exit_i -= 1
exit_j -= 1

# 정사각형 최소 크기, 최소 크기일 경우의 좌상단 좌표
min_size, min_i, min_j = 0, 0, 0

move_cnt = 0  # 참가자 이동 횟수

# k번 동안 참가자 이동 및 미로 회전 진행
for _ in range(k):
    # 참가자 이동
    maze = move()

    # 모든 참가자가 탈출했다면 즉시 종료
    if not participate:
        break
    
    # 최소 1명의 참가자와 출구가 같이 존재하는 정사각형 범위 구하기
    min_square()

    # 정사각형 회전
    maze = rotate(min_i, min_j, min_size)

# k번의 턴 진행 혹은 모든 참가자가 탈출했을 경우 참가자의 이동 횟수 총 합과 마지막 출구 위치 출력
print(move_cnt)
print(exit_i + 1, exit_j + 1)