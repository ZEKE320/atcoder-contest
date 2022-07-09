#%%
import numpy as np
from sys import stdin


def rotate(vec, t):

    t = np.deg2rad(t)

    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

    return np.dot(R, vec)


x, y, t = map(int, stdin.readline().rstrip().split())

vec = np.array([x, y])
# print(vec)


r_vec = rotate(vec, t)

# print(r_vec)

print(f"{r_vec[0]} {r_vec[1]}")