# 영역 구하기

# 벽 만들기
# 영역은 BFS로 구하기
# 8:03부터

import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().rstrip().split())
board = [[0 for _ in range(N)] for _ in range(M)]

for k in range(K):
    # print(k, "번쨰 ---------")
    Ly, Lx, Ry, Rx = map(int, input().rstrip().split())
    for i in range(M-Rx, M-Lx):
        for j in range(Ly, Ry):
            # print(i, j)
            board[i][j] = 1

d_xy = [(0,1), (1,0), (0,-1), (-1,0)]
visited = [[0 for _ in range(N)] for _ in range(M)]
ans_num = 0
ans_cnt = []
for i in range(M):
    for j in range(N):
        if visited[i][j] or board[i][j]:
            continue

        # BFS
        q = deque([(i, j)])
        visited[i][j] = 1
        ans_num += 1
        cnt = 1
        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + d_xy[d][0]
                ny = y + d_xy[d][1]

                if nx<0 or nx>=M or ny<0 or ny>=N:
                    continue
                # print(nx, ny)
                if board[nx][ny] or visited[nx][ny]:
                    # 벽이거나 이미 방문한 경우
                    continue

                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
        # print(cnt)

        ans_cnt.append(cnt)

print(ans_num)
print(*sorted(ans_cnt), sep=' ')