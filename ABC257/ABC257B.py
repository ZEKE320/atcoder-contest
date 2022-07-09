import numpy as np

N, K, Q = map(int, input().split())


def operate(operation, pieces):
    operation -= 1
    if pieces[operation] == N or (
        operation + 1 < K and pieces[operation] + 1 == pieces[operation + 1]
    ):
        return
    pieces[operation] += 1


pieces = np.array(input().split(), int)
operations = np.array(input().split(), int)
for i in range(Q):
    operate(operations[i], pieces)

for i in range(K):
    print(pieces[i], end="")
    if i < K - 1:
        print(" ", end="")

print()
