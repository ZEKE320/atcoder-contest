#%%

import numpy as np
from sys import stdin


def set_arr(s):
    arr = list()
    j = -1
    for i in range(len(s)):
        if j >= 0 and s[i] == s[i - 1]:
            arr[j][1] += 1
        else:
            j += 1
            arr.append([s[i], 1])
    return arr


S = input()
T = input()

arr_s = np.array(set_arr(S))
arr_t = np.array(set_arr(T))

# print(arr_s)
# print(arr_t)

if arr_s.shape[0] != arr_t.shape[0]:
    print("No")
    exit()

for i in range(arr_s.shape[0]):
    if (
        (arr_s[i][0] != arr_t[i][0])
        or (int(arr_s[i][1]) < 2 and int(arr_t[i][1]) >= 2)
        or int(arr_s[i][1]) > int(arr_t[i][1])
    ):
        print("No")
        exit()

print("Yes")

# %%
