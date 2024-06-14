from collections import deque


l, n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(l)]

# 상우하좌 순서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

info = [[-1, -1, -1, -1]]  # 기사의 좌상단 좌표(r, c), 높이(h), 폭(w)
hp = [0]  # 기사의 체력
damage = [0] * (n + 1)

# 기사의 정보와 체력을 저장
for _ in range(n):
    r, c, h, w, k = map(int, input().split())
    info.append([r - 1, c - 1, h, w])
    hp.append(k)

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

    # 이동방향으로 탐색
    r, c, h, w = info[num]
    move_knight = [num]  # 이동하게 될 기사 목록
    check_list = deque()  # 탐색 좌표

    visited = [[0] * l for _ in range(l)]  # 방문 여부

    # 위아래 방향일 경우 기사의 폭에 해당하는 좌표를 check_list에 추가
    if d == 0 or d == 2:
        for dc in range(w):
            visited[r][c + dc] = 1
            check_list.append((r, c + dc))

    # 좌우 방향일 경우 기사의 높이에 해당하는 좌표를 check_list에 추가
    else:
        for dr in range(h):
            visited[r + dr][c] = 1
            check_list.append((r + dr, c))


    # 벽을 만난다면 continue
    can_move = True
    while check_list:
        ci, cj = check_list.popleft()

        ni, nj = ci + di[d], cj + dj[d]

        # 이동할 위치가 범위를 벗어나거나 벽일 경우 이동 불가로 바꾸고 while문 종료
        if ni < 0 or ni == l or nj < 0 or nj == l:
            can_move = False
            break
        if board[ni][nj] == 2:
            can_move = False
            break

        # 방문 지역일 경우 continue
        if visited[ni][nj]:
            continue
        
        # 빈칸일 경우 continue
        if not knight[ni][nj]:
            continue

        # 이동할 위치에 다른 기사가 있을 때 move_knight에 없을 경우
        if knight[ni][nj] not in move_knight:
            # 기사를 move_knight에 추가 후 기사의 영역 확인
            new_knight = knight[ni][nj]
            move_knight.append(new_knight)
            r, c, h, w = info[new_knight]

            # 위아래 방향일 경우 기사의 폭에 해당하는 좌표를 check_list에 추가
            if d == 0 or d == 2:
                for dc in range(w):
                    visited[r][c + dc] = 1
                    check_list.append((r, c + dc))

            # 좌우 방향일 경우 기사의 높이에 해당하는 좌표를 check_list에 추가
            else:
                for dr in range(h):
                    visited[r + dr][c] = 1
                    check_list.append((r + dr, c))

        # move_knight에 있는 기사일 경우 방문 표시 후 check_list에 추가
        else:
            visited[ni][nj] = 1
            check_list.append((ni, nj))

    # 이동 불가라면 아래 과정 생략
    if not can_move:
        continue

    # 기사 이동
    for mk in move_knight:
        info[mk][0] += di[d]
        info[mk][1] += dj[d]

    # 이동한 자리에 함정이 있는지 확인
    ## 명령 받은 기사는 대미지 X
    for mk in move_knight:
        # 명령을 받은 기사는 제외
        if mk == num:
            continue

        r, c, h, w = info[mk]

        # 이동을 진행한 기사의 영역에 함정 개수 확인
        for dr in range(h):
            for dc in range(w):
                nr, nc = r + dr, c + dc
                if board[nr][nc] == 1:
                    hp[mk] -= 1
                    damage[mk] += 1

        # 체력이 음수값이 된다면 0으로 변환
        if hp[mk] < 0:
            hp[mk] = 0

# 모든 명령 종료 후 생존한 기사들의 총 대미지 합 출력
sum_damage = 0
for i in range(1, n + 1):
    if hp[i]:
        sum_damage += damage[i]

print(sum_damage)