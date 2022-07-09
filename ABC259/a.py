#%%

from sys import stdin

# stdin.readline().rstrip()
N, M, X, T, D = map(int, stdin.readline().rstrip().split())

if M < X:
    print(T - (X - M) * D)
else:
    print(T)
