# 치즈
# 골드4

# 가장자리에는 없음
# 1시간 -> 공기에 닿은 치즈 녹아 없어짐

# 전체 돌면서 내부 구멍 파악 & 표시하기
# 치즈 개수도 저장
# 치즈의 가장자리 확인하기
#   1면 이상이 공기와 접촉

# 100x100x50 정도일 것 -> 500000

# 일단 해보기!

import sys
from collections import deque
input = sys.stdin.readline

sero, garo = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(sero)]

total = 0

d_xy = [(0,1), (1,0), (0,-1), (-1,0)]

# 내부 빈공간 찾기 & 치즈 개수 세기
visited = [[0 for _ in range(garo)] for _ in range(sero)]
# (0,0) 해당하는 것들 표시
board[0][0] = -1
visited[0][0] = 1


# 치즈
def check(x, y):
    cnt = 0
    for d in range(4):
        nx = x + d_xy[d][0]
        ny = y + d_xy[d][1]

        if nx<0 or nx>=sero or ny<0 or ny>=garo:
            continue
        if visited[nx][ny]:
            continue

        if board[nx][ny] == -1:
            # 외부와 접하는지 확인
            cnt += 1

    if cnt >= 1:
        # 외부와 접하는 곳이 하나 이상이면
        return True
    else:
        # 아니면
        return False

# visited 배열 초기화

count = 1
prev_count = 0
time = 0
while count > 0:
    # print("--------다시 시작----------")
    visited = [[0 for _ in range(garo)] for _ in range(sero)]
    # 진짜 외부공간 찾기
    q_outside = deque([(0, 0)])
    while q_outside:
        x_out, y_out = q_outside.popleft()
        # print(x_out, y_out)

        for d in range(4):
            nx_out = x_out + d_xy[d][0]
            ny_out = y_out + d_xy[d][1]

            if nx_out < 0 or nx_out >= sero or ny_out < 0 or ny_out >= garo:
                continue
            if board[nx_out][ny_out] == 1:
                continue

            if not visited[nx_out][ny_out]:
                board[nx_out][ny_out] = -1
                visited[nx_out][ny_out] = 1
                q_outside.append((nx_out, ny_out))
                # print("새로 추가 좌표: ", (nx_out, ny_out))

    # print(*board, sep='\n')
    visited = [[0 for _ in range(garo)] for _ in range(sero)]

    count = 0
    for i in range(sero):
        for j in range(garo):
            if board[i][j] == 1 and not visited[i][j]:
                # print("들어와?", (i, j))
                visited[i][j] = 1

                if check(i, j):
                    # print("통과", (i, j))
                    board[i][j] = -1  # 녹은 것으로 표시
                    count += 1

    # print("=========================")
    # print(*board, sep='\n')
    # print(count)
    if count>0:
        time += 1
        prev_count = count

print(time)
print(prev_count)