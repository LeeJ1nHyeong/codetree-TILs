m, t = map(int, input().split())

board = [[[] for _ in range(4)] for _ in range(4)]
dead_monster = [[[] for _ in range(4)] for _ in range(4)]

# 몬스터 이동 8방향
m_di = [-1, -1, 0, 1, 1, 1, 0, -1]
m_dj = [0, -1, -1, -1, 0, 1, 1, 1]

# 팩맨 이동 8방향
p_di = [-1, 0, 1, 0]
p_dj = [0, -1, 0, 1]

# 팩맨 처음 위치
pi, pj = map(int, input().split())
pi -= 1
pj -= 1

# 처음 몬스터 정보 저장
for _ in range(m):
    r, c, d = map(int, input().split())
    board[r - 1][c - 1].append(d - 1)


# 몬스터 이동
def move_monster():
    next_board = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                # 각 몬스터별로 진행 가능한 방향을 찾아 이동
                for d in board[i][j]:
                    is_move = False
                    for k in range(8):
                        ni, nj = i + m_di[(d + k) % 8], j + m_dj[(d + k) % 8]

                        if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                            continue

                        # 진행 방향에 몬스터 시체가 있다면 continue
                        if dead_monster[ni][nj]:
                            continue

                        # 진행 방향에 팩맨이 있다면 continue
                        if (ni, nj) == (pi, pj):
                            continue

                        is_move = True
                        next_board[ni][nj].append((d + k) % 8)
                        break

                    # 진행이 불가능하다면 그대로 놔두기
                    if not is_move:
                        next_board[i][j].append(d)

    return next_board


def delete_dead_monster():
    next_dead_monster = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            # 몬스터 시체가 있는 칸 탐색
            if dead_monster[i][j]:
                dead_monster_ij = []
                # 유지되는 몬스터 시체만 따로 추출하여 next_dead_monster에 저장
                for dm in dead_monster[i][j]:
                    if dm > 1:
                        dead_monster_ij.append(dm - 1)

                next_dead_monster[i][j] = dead_monster_ij

    return next_dead_monster


for turn in range(1, t + 1):
    # 몬스터 복제 시도
    egg = []  # 생존 중인 몬스터가 부화할 알

    # 현재 위치에 존재하는 몬스터의 위치와 진행 방향을 egg에 튜플 형태로 저장
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                for d in board[i][j]:
                    egg.append((i, j, d))

    # 몬스터 이동
    board = move_monster()

    # 팩맨 이동 경로 선정
    max_cnt = -1
    max_d1, max_d2, max_d3 = -1, -1, -1
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                visited = []
                cnt = 0
                ni, nj = pi, pj

                # 첫번째 이동
                ni += p_di[d1]
                nj += p_dj[d1]

                if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                    continue

                visited.append((ni, nj))
                cnt += len(board[ni][nj])

                # 두번째 이동
                ni += p_di[d2]
                nj += p_dj[d2]

                if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                    continue

                if (ni, nj) not in visited:
                    cnt += len(board[ni][nj])
                    visited.append((ni, nj))

                # 세번째 이동
                ni += p_di[d3]
                nj += p_dj[d3]

                if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                    continue

                if (ni, nj) not in visited:
                    cnt += len(board[ni][nj])
                    visited.append((ni, nj))

                if cnt <= max_cnt:
                    continue

                max_cnt = cnt
                max_d1, max_d2, max_d3 = d1, d2, d3


    ## 팩맨 이동
    # 첫번째 이동
    pi += p_di[max_d1]
    pj += p_dj[max_d1]

    if board[pi][pj]:
        for _ in range(len(board[pi][pj])):
            dead_monster[pi][pj].append(3)

        board[pi][pj] = []

    # 두번째 이동
    pi += p_di[max_d2]
    pj += p_dj[max_d2]

    if board[pi][pj]:
        for _ in range(len(board[pi][pj])):
            dead_monster[pi][pj].append(3)

        board[pi][pj] = []

    # 세번째 이동
    pi += p_di[max_d3]
    pj += p_dj[max_d3]

    if board[pi][pj]:
        for _ in range(len(board[pi][pj])):
            dead_monster[pi][pj].append(3)

        board[pi][pj] = []

    # 몬스터 시체 소멸
    dead_monster = delete_dead_monster()

    # 몬스터 복제
    for i, j, d in egg:
        board[i][j].append(d)

# 모든 턴 종료 후 남아있는 몬스터 수 출력
monster = 0
for i in range(4):
    for j in range(4):
        if board[i][j]:
            monster += len(board[i][j])

print(monster)