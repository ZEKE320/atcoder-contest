#%%

import collections

l = input()

c = collections.Counter(l)

for idx, i in enumerate(c):
    if c[i] == 1:
        print(i)
        exit()

print(-1)
