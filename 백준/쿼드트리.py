# 쿼드트리
# 실버1

# 전부 0 -> 0, 전부 1-> 1
# 쪼개서 이렇게 될 때까지 쪼개기

# 쪼개기 함수
# 0, 1인지 판별하는 함수
# 판별 후 괄호로 묶는 함수

import sys
input = sys.stdin.readline
ans = ""


def divide(idx, arr):
    global ans
    # print("====================")
    # print("idx ", idx)
    # print(*arr, sep='\n')

    ck = check(arr)


    if ck <= 1:
        ans += str(ck)
        # print(ans)
        return
    else:
        mid = int(len(arr) / 2)

        arr1, arr2, arr3, arr4 = [], [], [], []
        # 왼쪽 위
        for i in range(mid):
            temp = []
            for j in range(mid):
                temp.append(arr[i][j])
            arr1.append(temp)
        # 오른쪽 위
        for i in range(mid):
            temp = []
            for j in range(mid, len(arr)):
                temp.append(arr[i][j])
            arr2.append(temp)
        # 왼쪽 아래
        for i in range(mid, len(arr)):
            temp = []
            for j in range(mid):
                temp.append(arr[i][j])
            arr3.append(temp)
        # 오른쪽 아래
        for i in range(mid, len(arr)):
            temp = []
            for j in range(mid, len(arr)):
                temp.append(arr[i][j])
            arr4.append(temp)

        ans += "("
        divide(1, arr1)
        divide(2, arr2)
        divide(3, arr3)
        divide(4, arr4)
        ans += ")"

    return

def check(arr):
    total = 0
    ck = -1

    for i in range(len(arr)):
        total += sum(arr[i])

    if total == 0:
        ck = 0
    elif total == len(arr)**2:
        ck = 1
    else:
        ck = 2

    return ck

def func(string):
    return int(string)

N = int(input())
board = [list(map(func, input().rstrip())) for _ in range(N)]

divide(0, board)

print(ans)
