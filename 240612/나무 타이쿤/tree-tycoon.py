# 특수 영양제 이동
def move_nutrient():
    next_nutrient = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 특수 영양제를 d방향으로 p칸 이동
            if nutrient[i][j]:
                # 범위를 벗어나면 반대편과 이어져있다고 가정
                ni, nj = (i + di[d] * p) % n, (j + dj[d] * p) % n

                # 이동한 위치에 특수 영양제 표시
                next_nutrient[ni][nj] = 1

                # 특수 영양제를 이동한 자리의 리브로수 높이 1 증가
                tree[ni][nj] += 1

    return next_nutrient


# 리브로수 성장
def grow():
    next_tree = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 특수 영양제가 있는 위치에서 인접한 대각선 4방향 탐색
            if nutrient[i][j]:
                grown_tree = tree[i][j]
                for di, dj in (-1, -1), (-1, 1), (1, -1), (1, 1):
                    ni, nj = i + di, j + dj

                    # 범위를 벗어난 지역은 제외
                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    # 높이가 1 이상인 리브로수 탐색
                    if tree[ni][nj]:
                        grown_tree += 1

                # 높이가 1 이상인 리브로수 개수만큼 성장
                next_tree[i][j] += grown_tree

            else:
                next_tree[i][j] = tree[i][j]

    return next_tree


# 리브로수 잘라내기
def cut():
    for i in range(n):
        for j in range(n):
            # 특수 영양제가 없는 위치 탐색
            if not nutrient[i][j]:
                # 높이가 2 이상인 리브로수에 대해 2 감소 후 해당 위치에 특수 영양제 부여
                if tree[i][j] < 2:
                    continue

                tree[i][j] -= 2
                nutrient[i][j] = 1
            
            # 기존에 특수 영양제가 있었다면 특수 영양제 회수
            else:
                nutrient[i][j] = 0


n, m = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(n)]
nutrient = [[0] * n for _ in range(n)]
nutrient[n - 2][0], nutrient[n - 2][1] = 1, 1
nutrient[n - 1][0], nutrient[n - 1][1] = 1, 1

# 오른쪽 방향부터 반시계방향
di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, 1, 1, 0, -1, -1, -1, 0, 1]

for _ in range(m):
    d, p = map(int, input().split())

    # 특수 영양제 이동
    nutrient = move_nutrient()

    # 특수 영양제 땅 성장
    tree = grow()

    # 잘라내기
    cut()

# m년 후 남아있는 리브로수의 총 높이 합 출력           
ans = 0
for t in tree:
    ans += sum(t)

print(ans)