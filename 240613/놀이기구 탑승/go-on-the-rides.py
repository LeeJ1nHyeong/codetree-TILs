n = int(input())
board = [[0] * n for _ in range(n)]
like = [[] for _ in range(n * n + 1)]

score = 0

# 자리 배치
for _ in range(n * n):
    num, *like_list = map(int, input().split())
    like[num] = like_list

    max_i, max_j = n, n  # 조건에 맞는 좌표
    max_like_cnt = 0  # 좋아하는 친구 수
    max_blank_cnt = 0  # 빈칸 수

    for i in range(n):
        for j in range(n):
            # 비어있는 자리에서 탐색 진행
            if not board[i][j]:
                like_cnt = 0  # 좋아하는 친구 수
                blank_cnt = 0  # 빈칸 수

                # 4방향 탐색
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = i + di, j + dj

                    # 범위 밖으로 벗어나면 제외
                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    # 빈칸이라면 blank_cnt 1 증가
                    if not board[ni][nj]:
                        blank_cnt += 1
                    
                    # 자리에 학생이 있을 경우
                    else:
                        # 그 학생이 좋아하는 친구 목록에 있다면 like_cnt 1 증가
                        if board[ni][nj] in like_list:
                            like_cnt += 1

                ## 조건에 맞는 자리인지 탐색
                # 좋아하는 사람 수, 같다면 빈칸 수, 같다면 작은 행, 같다면 작은 열 순서로 조건 확인
                if like_cnt < max_like_cnt:
                    continue

                if like_cnt == max_like_cnt:
                    if blank_cnt < max_blank_cnt:
                        continue

                    if blank_cnt == max_blank_cnt:
                        if i > max_i:
                            continue

                        if i == max_i:
                            if j > max_j:
                                continue

                # 조건을 만족한다면 최신화
                max_i, max_j = i, j
                max_like_cnt = like_cnt
                max_blank_cnt = blank_cnt

    # 자리 배정
    board[max_i][max_j] = num

# 점수 계산
for i in range(n):
    for j in range(n):
        # 해당 학생이 앉은 좌석을 기준으로 4방향에 좋아하는 친구 수에 따라 점수 부여
        num = board[i][j]
        like_cnt = 0
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj

            if ni < 0 or ni == n or nj < 0 or nj == n:
                continue

            if board[ni][nj] in like[num]:
                like_cnt += 1

        if like_cnt:
            score += 10 ** (like_cnt - 1)

# 점수 출력
print(score)