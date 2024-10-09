from collections import deque

# 초기 설정
def init():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
            active[i][j] = 0

# 공격 적용
def attack_turret(i, j, p):
    board[i][j] -= p
    if board[i][j] < 0:
        board[i][j] = 0
    
    active[i][j] = 1

# 레이저 공격
def laser_attack(wi, wj, si, sj):
    queue = deque([(wi, wj)])
    visited[wi][wj] = 1

    can_attack = False
    while queue:
        ci, cj = queue.popleft()

        if ci == si and cj == sj:
            can_attack = True
            break

        # 우, 하, 좌, 상 순서로 탐색
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = (ci + di) % n, (cj + dj) % m

            # 방문했거나 벽일 경우 continue
            if visited[ni][nj]:
                continue
            if not board[ni][nj]:
                continue

            # 방문 표시 후 이전 좌표 저장
            visited[ni][nj] = 1
            prev_i[ni][nj] = ci
            prev_j[ni][nj] = cj

            queue.append((ni, nj))

    # 레이저 공격이 가능할 경우 공격 진행
    if can_attack:
        power = board[wi][wj]
        attack_turret(si, sj, power)

        i, j = prev_i[si][sj], prev_j[si][sj]
        while not (i == wi and j == wj):
            attack_turret(i, j, power // 2)
            next_i, next_j = prev_i[i][j], prev_j[i][j]
            i, j = next_i, next_j

    return can_attack

# 폭탄 공격
def bomb_attack(wi, wj, si, sj):
    # 강한 포탑 공격력의 절반에 해당하는 값을 공격력으로 설정
    power = board[wi][wj]

    attack_turret(si, sj, power)

    # 강한 포탑 기준 8방향의 포탑에 폭탄 공격
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
        ni, nj = (si + di) % n, (sj + dj) % m
        # 8방향 중 공격자 포탑일 경우 continue
        if ni == wi and nj == wj:
            continue
        if board[ni][nj]:
            attack_turret(ni, nj, power // 2)

# 포탑 수리
def repair():
    for i in range(n):
        for j in range(m):
            if board[i][j] and not active[i][j]:
                board[i][j] += 1


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
recent_attack = [[0] * m for _ in range(n)]  # 최근 공격 시간
active = [[0] * m for _ in range(n)]  # 활성화 여부

prev_i = [[0] * m for _ in range(n)]  # 직전 방문 지역의 i좌표 저장
prev_j = [[0] * m for _ in range(n)]  # 직전 방문 지역의 j좌표 저장

for turn in range(1, k + 1):
    # 살아있는 포탑을 탐색하여 저장
    turret = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                turret.append((board[i][j], recent_attack[i][j], i, j))

    # 살아있는 포탑이 1개 이하일 경우 종료
    if len(turret) <= 1:
        break

    # 방문 기록, 활성화 여부 초기화
    init()

    # 문제 조건에 따른 우선순위 순서대로 정렬
    turret.sort(key=lambda x: (x[0], -x[1], -(x[2] + x[3]), -x[3]))

    # 가장 약한 포탑 설정
    weak_i, weak_j = turret[0][2], turret[0][3]
    board[weak_i][weak_j] += n + m
    recent_attack[weak_i][weak_j] = turn
    active[weak_i][weak_j] = 1

    # 가장 강한 포탑
    strong_i, strong_j = turret[-1][2], turret[-1][3]

    # 레이저 공격 진행
    laser_success = laser_attack(weak_i, weak_j, strong_i, strong_j)

    # 레이저 공격 불가 시 폭탄 공격 진행
    if not laser_success:
        bomb_attack(weak_i, weak_j, strong_i, strong_j)

    # 공격 종료 후 포탑 수리
    repair()

# 모든 턴이 끝났거나 남아있는 포탑이 1개 이하일 경우 남은 포탑 중 가장 강한 포탑의 공격력 출력
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, board[i][j])
print(ans)