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

for _ in range(m):
    r, c, d = map(int, input().split())
    board[r - 1][c - 1].append(d - 1)

# print("init----------")
# for b in board:
#     print(b)

monster = 0
for _ in range(t):
    # 몬스터 알 부화
    egg = []  # 생존 중인 몬스터가 부화할 알

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                for d in board[i][j]:
                    egg.append((i, j, d))

    # 몬스터 이동
    next_board = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                for d in board[i][j]:
                    is_move = False
                    for k in range(8):
                        ni, nj = i + m_di[(d + k) % 8], j + m_dj[(d + k) % 8]

                        if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                            continue

                        if dead_monster[ni][nj]:
                            continue

                        if (ni, nj) == (pi, pj):
                            continue

                        is_move = True
                        next_board[ni][nj].append((d + k) % 8)
                        break

                    if not is_move:
                        next_board[ni][nj].append(d)

    board = next_board

    # print("monster move----------")
    # for b in board:
    #     print(b)

    # 팩맨 이동 경로 선정
    max_cnt = -1
    max_d1, max_d2, max_d3 = -1, -1, -1
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                visited = [[0] * 4 for _ in range(4)]
                cnt = 0
                ni, nj = pi, pj

                # 첫번째 이동
                ni += p_di[d1]
                nj += p_dj[d1]

                if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                    continue

                visited[ni][nj] = 1
                cnt += len(board[ni][nj])

                # 두번째 이동
                ni += p_di[d2]
                nj += p_dj[d2]

                if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                cnt += len(board[ni][nj])

                # 세번째 이동
                ni += p_di[d3]
                nj += p_dj[d3]

                if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                cnt += len(board[ni][nj])

                if cnt <= max_cnt:
                    continue

                max_cnt = cnt
                max_d1, max_d2, max_d3 = d1, d2, d3

    # print(max_d1, max_d2, max_d3)
    # print(max_cnt)

    # 팩맨 이동
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

    # print("이동 후 팩맨----------")
    # print(pi, pj)

    # 몬스터 시체 소멸
    next_dead_monster = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            if dead_monster[i][j]:
                dead_monster_ij = []
                for dm in dead_monster[i][j]:
                    if dm > 0:
                        dead_monster_ij.append(dm - 1)

                next_dead_monster[i][j] = dead_monster_ij

    dead_monster = next_dead_monster

    # print("dead----------")
    # for dm in dead_monster:
    #     print(dm)

    # 몬스터 복제
    for i, j, d in egg:
        board[i][j].append(d)

    # 복제 후 생존 중인 몬스터 탐색
    after_monster = 0
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                after_monster += len(board[i][j])

    monster = after_monster

    # print("turn end----------")
    # for b in board:
    #     print(b)

    # print()

    # 몬스터가 없다면 즉시 종료
    if not monster:
        break

print(monster)