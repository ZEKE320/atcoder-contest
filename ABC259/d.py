import numpy as np
from sys import stdin


def check(c_1, c_2):
    c = np.sqrt((c_1[0] - c_2[0]) ** 2 + (c_1[1] - c_2[1]) ** 2)
    if c <= c_1[2] + c_2[2]:
        return True
    else:
        return False


N = int(stdin.readline().rstrip())

ROUTE = np.array(list(map(int, stdin.readline().rstrip().split()))).reshape(2, 2)

CIRCLES = list()

for _ in range(N):
    CIRCLES.append(tuple(map(int, stdin.readline().rstrip().split())))

c_arr = np.array(CIRCLES).reshape(N, 3)

print(c_arr)

edge = list()

for i in range(N):
    for j in range(N - (i + 1)):
        crossing = check(c_arr[i], c_arr[i + (j + 1)])
        # print(i, i + (j + 1), c_arr[i], c_arr[i + (j + 1)])
        if crossing == True:
            edge.append([i, i + (j + 1)])

print(edge)


