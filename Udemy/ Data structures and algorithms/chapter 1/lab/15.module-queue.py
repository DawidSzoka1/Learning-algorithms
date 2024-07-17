import queue


q = queue.Queue()

for i in range(1, 5):
    q.put(i)

print(q.qsize())

while not q.empty():
    print(f"element: {q.get()}, size: {q.qsize()}")

lifo = queue.LifoQueue()

for i in range(1, 5):
    lifo.put(i + 10)

print(lifo.qsize())

while not lifo.empty():
    print(f"element: {lifo.get()}, size: {lifo.qsize()}")


prioritized_q = queue.PriorityQueue()

prioritized_q.put((1, 'Task pri 1'))
prioritized_q.put((3, 'Task pri 3'))
prioritized_q.put((2, 'Task pri 2'))
prioritized_q.put((2, 'Task pri 2 again'))

while not prioritized_q.empty():
    print(f"element: {prioritized_q.get()}, size: {prioritized_q.qsize()}")

