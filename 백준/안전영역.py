# 안전 영역

# import math
# import time
# start = time.time()
# math.factorial(100000)
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = []
nums = []

for i in range(N):
    arr = list(map(int, input().split()))
    nums += arr
    board.append(arr)

nums = list(set(nums))

d_xy = [(0,1), (1,0), (0,-1), (-1,0)]
ans = 0

for num in nums:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue

            visited[i][j] = 1
            if board[i][j] < num:
                continue

            # 안전 영역
            q = deque([(i, j)])
            temp += 1
            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx = x + d_xy[k][0]
                    ny = y + d_xy[k][1]

                    if nx<0 or nx>=N or ny<0 or ny>=N:
                        continue
                    if board[nx][ny] < num or visited[nx][ny]:
                        visited[nx][ny] = 1
                        continue

                    q.append((nx, ny))
                    visited[nx][ny] = 1
    ans = max(ans, temp)

print(ans)
#
# end = time.time()
# print(f"{end-start:.5f} sec")