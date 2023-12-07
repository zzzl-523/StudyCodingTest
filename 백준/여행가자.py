# 여행 가자
# 골드4

# Union-Find로 풀어보기
import sys
input = sys.stdin.readline

parent = []

def find_parent(i):
    if parent[i] != i:
        return find_parent(parent[i])
    return parent[i]

def union_parent(a, b):
    global parent

    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solution():
    global parent

    N = int(input())
    M = int(input())
    parent = [0]+[num for num in range(1, N+1)]

    for i in range(N):
        arr = list(map(int, input().rstrip().split()))
        for j in range(N):
            if arr[j]:
                union_parent(i+1, j+1)

    course = list(map(int, input().rstrip().split()))

    prev_root = find_parent(course[0])
    count = 1
    for i in range(1, M):
        if find_parent(course[i]) == prev_root:
            count += 1

    if count == M:
        print("YES")
    else:
        print("NO")

solution()