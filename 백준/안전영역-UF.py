# 안전영역
# Union-Find로 풀기

import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        # print(x, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
        calculation(parent, item, d_xy, N, )
    else:
        parent[a] = b

def calculation(parent, item, d_xy, N, pos_height, height):
    for d in range(4):
        new = item + d_xy[d]

        if new < 0 or new > N * N - 1:
            continue
        if pos_height[new] <= height:
            parent[new] = -1
            continue

        union_parent(parent, item, new)

    return parent
def solution():
    global parent
    ans = 0
    N = int(input())

    height_pos = {} # 딕셔너리로 height_pos
    pos_height = {}


    # print(parent)

    for i in range(N):
        arr = list(map(int, input().rstrip().split()))
        for j in range(N):
            if arr[j] not in height_pos.keys():
                height_pos[arr[j]] = [j+N*i]
            else:
                height_pos[arr[j]].append((j+N*i))

            pos_height[j+N*i] = arr[j]


    # print(height_pos)
    # print(pos_height)

    key_list = sorted(height_pos.keys())
    key_length = len(key_list)

    d_xy = [1, N, -1, -N]

    # 빗물 높이 for문
    for idx, height in enumerate(key_list):
        print("------순서--",idx,"-----값--",height,"------")
        parent = [i for i in range(N * N)]
        visited = [0 for _ in range(N * N)]

        # 높이가 빗물 이상 되는 것들 for문
        for i in range(idx+1, key_length):
            for item in height_pos[key_list[i]]:
                if pos_height[item] <= height:
                    parent[item] = -1
                    continue

                # print(item, end=') ')

                        # print(parent)

                    # visited[new] = 1
            #     print()
            # print()
        #
        temp = []
        for thing in parent:
            if thing==-1:
                continue
            temp.append(find_parent(parent, thing))

        temp = set(temp)
        print(len(temp), " | ", temp)
        # for c in range(N):
        #     for b in range(N):
        #         num = c*N+b
        #         if num%5==4:
        #             print(parent[c*N+b])
        #         else: print(parent[c*N+b], end='  ')

        print(parent)


        ans = max(ans, len(set(parent)))
        print(len(set(parent))-1)
        print(set(parent))
    print(ans)

solution()
