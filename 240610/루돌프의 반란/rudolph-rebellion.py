def clear():
    for i in range(n):
        for j in range(n):
            board[i][j] = 0

def save_santa():
    # board 비우기
    clear()

    # 산타 좌표 저장
    for num in range(1, p + 1):
        # 탈락한 산타는 제외
        if not is_alive[num]:
            continue
        si, sj = santa[num]
        board[si][sj] = num


def select_santa():
    global min_santa_num
    global min_distance
    global min_i, min_j

    for num in range(1, p + 1):
        # 탈락한 산타는 제외
        if not is_alive[num]:
            continue

        i, j = santa[num]
        distance = (i - ri) ** 2 + (j - rj) ** 2

        # 최단거리가 설정되어있지 않으면 바로 적용
        if min_distance == -1:
            min_santa_num = num
            min_distance = distance
            min_i, min_j = i, j
            continue

        # 루돌프와 가장 가까운 거리, 거리가 같다면 i가 큰 산타, i가 같다면 j가 큰 산타로 선정
        if distance > min_distance:
            continue

        if distance == min_distance:
            if i < min_i:
                continue
            
            if i == min_i:
                if j < min_j:
                    continue

        min_santa_num = num
        min_distance = distance
        min_i, min_j = i, j


n, m, p, c, d = map(int, input().split())
board = [[0] * n for _ in range(n)]

# 산타 생존 여부
is_alive = [1] * (p + 1)
is_alive[0] = 0

# 산타가 기절한 턴
is_stun = [-1] * (p + 1)

# 점수
score = [0] * (p + 1)

# 루돌프 좌표
ri, rj = map(int, input().split())
ri -= 1
rj -= 1

# 산타 좌표
santa = [(0, 0)] * (p + 1)
santa[0] = (-1, -1)

for _ in range(p):
    num, si, sj = map(int, input().split())
    santa[num] = (si - 1, sj - 1)

for turn in range(1, m + 1):
    # 남아있는 산타가 없으면 게임 종료
    if not sum(is_alive):
        break

    # 산타 좌표를 board에 저장
    save_santa()

    # print("init----------")
    # for b in board:
    #     print(*b)

    # 루돌프와 가장 가까운 산타 선정
    min_santa_num = 0
    min_distance = -1
    min_i, min_j = -1, -1

    select_santa()

    # print("min_santa----------")
    # print(min_santa_num, min_i, min_j)

    # 루돌프 이동
    di, dj = 0, 0

    if ri > min_i:
        di = -1
    elif ri < min_i:
        di = 1

    if rj > min_j:
        dj = -1
    elif rj < min_j:
        dj = 1

    ri += di
    rj += dj

    # print("루돌프----------")
    # print(ri, rj)

    # 루돌프가 움직여서 산타와 충돌했을 경우
    if board[ri][rj]:
        santa_num = board[ri][rj]
        score[santa_num] += c
        is_stun[santa_num] = turn

        board[ri][rj] = 0

        si, sj = santa[santa_num]

        si += di * c
        sj += dj * c

        if si < 0 or si >= n or sj < 0 or sj >= n:
            is_alive[santa_num] = 0

        else:
            santa[santa_num] = (si, sj)
            prev_santa_num = board[si][sj]
            board[si][sj] = santa_num

            # 산타 상호작용
            while True:
                if not prev_santa_num:
                    break

                i, j = santa[prev_santa_num]
                i += di
                j += dj

                if i < 0 or i >= n or j < 0 or j >= n:
                    is_alive[prev_santa_num] = 0
                    break

                santa[prev_santa_num] = (i, j)
                temp = board[i][j]
                board[i][j] = prev_santa_num
                prev_santa_num = temp

    # print("rudolph move----------")
    # for b in board:
    #     print(*b)

    # 산타 이동
    for num in range(1, p + 1):
        # 탈락했거나 기절 중인 산타는 제외
        if not is_alive[num] or is_stun[num] == turn or is_stun[num] == turn - 1:
            continue

        si, sj = santa[num]

        min_distance = (ri - si) ** 2 + (rj - sj) ** 2
        ni, nj = -1, -1
        di, dj = 0, 0
        # 상우하좌 순서로 이동 가능 여부 확인
        for mi, mj in (-1, 0), (0, 1), (1, 0), (0, -1):
            move_i, move_j = si + mi, sj + mj

            # 범위 밖으로 벗어나면 continue
            if move_i < 0 or move_i == n or move_j < 0 or move_j == n:
                continue

            # 이동할 지역에 다른 산타가 있다면 continue
            if board[move_i][move_j]:
                continue

            # 루돌프와 멀어지는 방향이라면 continue
            if min_distance <= (move_i - ri) ** 2 + (move_j - rj) ** 2:
                continue

            min_distance = (move_i - ri) ** 2 + (move_j - rj) ** 2
            ni, nj = move_i, move_j
            di, dj = mi, mj

        if ni == -1 and nj == -1:
            continue

        # 이동이 가능할 경우 원래 산타가 있던 지역 비우기
        board[si][sj] = 0

        # 이동한 산타가 루돌프와 충돌했을 경우
        if ni == ri and nj == rj:
            score[num] += d
            is_stun[num] = turn

            ni += -di * d
            nj += -dj * d

            if ni < 0 or ni == n or nj < 0 or nj == n:
                is_alive[num] = 0

            else:
                santa[num] = (ni, nj)
                prev_santa_num = board[ni][nj]
                board[ni][nj] = num

                # 산타 상호작용
                while True:
                    if not prev_santa_num:
                        break

                    ni -= di
                    nj -= dj

                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        is_alive[prev_santa_num] = 0
                        break

                    santa[prev_santa_num] = (ni, nj)
                    temp = board[ni][nj]
                    board[ni][nj] = prev_santa_num
                    prev_santa_num = temp

        # 루돌프와 충돌하지 않을 경우
        else:
            board[ni][nj] = num
            santa[num] = (ni, nj)

    # print("santa move----------")
    # for b in board:
    #     print(*b)

    # 턴 종료
    for num in range(1, p + 1):
        if is_alive[num]:
            score[num] += 1

    # print("score----------")
    # print(*score[1:])

    # print()

print(*score[1:])