from heapq import nlargest, nsmallest
l = [1, 2, 3]

i = l.__iter__()

print(next(i))
next(i)
print(next(i))
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']

print(sorted(ids, key=lambda x: int(x[2:])))


print(nlargest(3, ids, key=lambda x: int(x[2:])))
print(nsmallest(3, ids, key=lambda x: int(x[2:])))
