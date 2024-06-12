# 특수 영양제 이동
def move_nutrient():
    next_nutrient = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if nutrient[i][j]:
                ni, nj = (i + di[d] * p) % n, (j + dj[d] * p) % n
                next_nutrient[ni][nj] = 1
                tree[ni][nj] += 1

    return next_nutrient


# 리브로수 성장
def grow():
    next_tree = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if nutrient[i][j]:
                grown_tree = tree[i][j]
                for di, dj in (-1, -1), (-1, 1), (1, -1), (1, 1):
                    ni, nj = i + di, j + dj

                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    if tree[ni][nj]:
                        grown_tree += 1

                next_tree[i][j] += grown_tree

            else:
                next_tree[i][j] = tree[i][j]

    return next_tree


# 리브로수 잘라내기
def cut():
    for i in range(n):
        for j in range(n):
            if not nutrient[i][j]:
                if tree[i][j] < 2:
                    continue

                tree[i][j] -= 2
                nutrient[i][j] = 1
                
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