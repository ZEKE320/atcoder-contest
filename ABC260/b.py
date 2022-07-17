#%%
import numpy as np
from sys import stdin

N, X, Y, Z = map(int, input().split())

arr = np.empty(N * 3, dtype=int).reshape(3, N)

for i in range(N):
    arr[0, i] = i

arr[1] = input().split()
arr[2] = input().split()

arr = arr.T

if X > 0:
    math_rank = np.argsort(arr[:, 1])
    math_border_1 = arr[math_rank[N - X], 1]
    math_check_1 = arr[:, 1] >= math_border_1

    if arr[math_check_1].shape[0] > X:
        math_check_1 = np.argsort(arr[math_check_1][:, 0])

    passed_1 = arr[math_check_1[:X]]
    for p in passed_1:
        arr = np.delete(arr, p[0], 0)

print(arr)
print(passed_1)

if Y > 0:
    eng_rank = np.argsort(arr[:, 2])
    print(eng_rank)
    eng_border_1 = arr[eng_rank[N - X - Y], 2]
    print(eng_border_1)
    eng_check_1 = arr[:, 2] >= eng_border_1

    print(arr[eng_check_1])

    if arr[eng_check_1].shape[0] > Y:
        eng_check_1 = np.argsort(arr[eng_check_1][:, 0])

    passed_2 = arr[eng_check_1[:Y]]
    for p in passed_2:
        arr = np.delete(arr, p[0], 0)

print(arr)
print(passed_2)
