from collections import deque


l, n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(l)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

info = [[-1, -1, -1, -1]]
hp = [0]
damage = [0] * (n + 1)

# print("board----------")
# for b in board:
#     print(*b)

for _ in range(n):
    r, c, h, w, k = map(int, input().split())
    info.append([r - 1, c - 1, h, w])
    hp.append(k)

# print("init hp----------")
# print(hp)

for _ in range(q):
    num, d = map(int, input().split())

    # 기사가 사라졌다면 명령 생략
    if not hp[num]:
        continue

    # 기사의 현재 위치 최신화
    knight = [[0] * l for _ in range(l)]

    for i in range(1, n + 1):
        if not hp[i]:
            continue
        r, c, h, w = info[i]

        for dr in range(h):
            for dc in range(w):
                nr, nc = r + dr, c + dc
                knight[nr][nc] = i

    # print("before knight----------")
    # for kn in knight:
    #     print(*kn)

    # 이동방향으로 탐색
    r, c, h, w = info[num]
    move_knight = [num]  # 이동하게 될 기사 목록
    check_list = deque()

    visited = [[0] * l for _ in range(l)]

    # 위아래 방향일 경우
    if d == 0 or d == 2:
        for dc in range(w):
            visited[r][c + dc] = 1
            check_list.append((r, c + dc))

    # 좌우 방향일 경우
    else:
        for dr in range(h):
            visited[r + dr][c] = 1
            check_list.append((r + dr, c))


    # 벽을 만난다면 continue
    can_move = True
    while check_list:
        ci, cj = check_list.popleft()

        ni, nj = ci + di[d], cj + dj[d]

        if ni < 0 or ni == l or nj < 0 or nj == l:
            can_move = False
            break

        if board[ni][nj] == 2:
            can_move = False
            break

        if visited[ni][nj]:
            continue
        
        if not knight[ni][nj]:
            continue

        if knight[ni][nj] not in move_knight:
            new_knight = knight[ni][nj]
            move_knight.append(new_knight)
            r, c, h, w = info[new_knight]

            # 위아래 방향일 경우
            if d == 0 or d == 2:
                for dc in range(w):
                    visited[r][c + dc] = 1
                    check_list.append((r, c + dc))

            # 좌우 방향일 경우
            else:
                for dr in range(h):
                    visited[r + dr][c] = 1
                    check_list.append((r + dr, c))

        else:
            visited[ni][nj] = 1
            check_list.append((ni, nj))

    if not can_move:
        continue

    # print("move list----------")
    # print(move_knight)

    # 기사 이동
    for mk in move_knight:
        info[mk][0] += di[d]
        info[mk][1] += dj[d]

    # 이동한 자리에 함정이 있는지 확인
    ## 명령 받은 기사는 대미지 X
    ## 체력이 음수값이 된다면 0으로 변환
    for mk in move_knight:
        if mk == num:
            continue
        r, c, h, w = info[mk]

        for dr in range(h):
            for dc in range(w):
                nr, nc = r + dr, c + dc
                if board[nr][nc] == 1:
                    hp[mk] -= 1
                    damage[mk] += 1

        if hp[mk] < 0:
            hp[mk] = 0

    # print("hp----------")
    # print(hp)

    # print("damage----------")
    # print(damage)

    # print()

# 모든 명령 종료 후 생존한 기사들의 총 대미지 합 출력
sum_damage = 0
for i in range(1, n + 1):
    if hp[i]:
        sum_damage += damage[i]

print(sum_damage)