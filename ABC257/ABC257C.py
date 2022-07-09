import numpy as np

highest = 0

N = input()

bodySize = np.array(list(map(lambda x: "{}".format(x), input())), np.int8)

human = np.array(input().split())

adults = np.empty(shape=)
children = np.empty()

for i in range(N):
    if bodySize(i) == 1:
        adults.append(human[i])
    if bodySize(i) == 0:
        children.append(human[i])

print(adults)
print(children)
