def clear():
    for i in range(n):
        for j in range(n):
            board[i][j] = 0

# 산타 좌표 저장
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


# 루돌프와 가장 가까운 산타 선택
def select_santa():

    def set_min_santa(n, dist, i, j):
        global min_santa_num
        global min_distance
        global min_i, min_j

        min_santa_num = n
        min_distance = dist
        min_i, min_j = i, j

    
    for num in range(1, p + 1):
        # 탈락한 산타는 제외
        if not is_alive[num]:
            continue

        i, j = santa[num]
        distance = (i - ri) ** 2 + (j - rj) ** 2

        # 최단거리가 설정되어있지 않으면 바로 적용
        if min_distance == -1:
            set_min_santa(num, distance, i, j)
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

        # 조건을 만족했다면 해당 산타로 저장
        set_min_santa(num, distance, i, j)


# 루돌프와 산타 충돌
def collision(num, turn, s, i, j, di, dj):
    score[num] += s
    is_stun[num] = turn

    i += di * d
    j += dj * d

    if i < 0 or i >= n or j < 0 or j >= n:
        is_alive[num] = 0
        return

    else:
        santa[num] = (i, j)
        prev_santa_num = board[i][j]
        board[i][j] = num

        # 산타 상호작용
        interaction(prev_santa_num, i, j, di, dj)


# 산타 간의 상호작용
def interaction(num, i, j, di, dj):
    # 상호작용 대상 산타가 없을 때까지 진행
    while True:
        # 상호작용 대상 산타가 없을 경우 while문 종료
        if not num:
            return

        # 진행 방향으로 1칸씩 이동
        i += di
        j += dj

        # 산타가 맵 밖으로 벗어났을 경우 탈락 처리 후 while문 종료
        if i < 0 or i >= n or j < 0 or j >= n:
            is_alive[num] = 0
            return

        # 상호작용한 산타의 좌표 최신화 후 다음 산타가 있는지 확인
        santa[num] = (i, j)
        temp = board[i][j]
        board[i][j] = num
        num = temp


# 산타 이동
def move_santa():
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
            collision(num, turn, d, ni, nj, -di, -dj)

        # 루돌프와 충돌하지 않을 경우
        else:
            board[ni][nj] = num
            santa[num] = (ni, nj)


# 루돌프 이동
def move_rudolph(min_i, min_j):
    di, dj = 0, 0

    if ri > min_i:
        di = -1
    elif ri < min_i:
        di = 1

    if rj > min_j:
        dj = -1
    elif rj < min_j:
        dj = 1

    return di, dj


# 턴 종료
def end_turn():
    # 생존 중인 산타의 점수 1점 추가
    for num in range(1, p + 1):
        if is_alive[num]:
            score[num] += 1


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

    # 루돌프와 가장 가까운 산타 선정
    min_santa_num = 0
    min_distance = -1
    min_i, min_j = -1, -1

    select_santa()

    # 루돌프 이동
    di, dj = move_rudolph(min_i, min_j)

    ri += di
    rj += dj

    # 루돌프가 움직여서 산타와 충돌했을 경우
    if board[ri][rj]:
        santa_num = board[ri][rj]
        board[ri][rj] = 0
        si, sj = santa[santa_num]

        collision(santa_num, turn, c, si, sj, di, dj)

    # 산타 이동
    move_santa()

    # 턴 종료
    end_turn()

print(*score[1:])