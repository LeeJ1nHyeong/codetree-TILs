def search():
    can_move = 0

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]

        if not board[ni][nj]:
            can_move += 1

    return can_move


def rotate():
    global d

    d = (d - 1) % 4

    ni, nj = i + di[d], j + dj[d]
    if not board[ni][nj]:
        go()
        return
    else:
        rotate()

    return


def go():
    global i, j

    i += di[d]
    j += dj[d]


def back():
    global i, j

    i -= di[d]
    j -= dj[d]


n, m = map(int, input().split())
i, j, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

ans = 0

while True:
    # 현재 위치가 한 번도 온 적이 없다면 방문 표시
    if not board[i][j]:
        board[i][j] = 2
        ans += 1

    # 다음 이동 가능 구역 탐색
    can_move = search()

    # 이동
    ## 이동할 곳이 있다면 이동 가능한 위치가 나올 때까지 좌회전
    if can_move:
        rotate()

    ## 이동할 곳이 없다면 후진
    else:
        back()

        ## 후진한 위치가 벽이라면 종료
        if board[i][j] == 1:
            break

print(ans)