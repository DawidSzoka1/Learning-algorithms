from functools import reduce

numbers = [1, 45, 672, 7265, 16]
print(sorted(numbers, key=lambda x: x % 10))

codes = ['JPID', 'JJJPPP', 'XXX', 'JDU']

print(len(reduce(lambda x, y: x if len(x) > len(y) else y, codes)))

capitals = ['Rome', 'Paris', 'Madrid']
cities = ['Rome', 'Napoli', 'Rimini', 'Paris', 'Barcelona', 'Madrid', 'Marceille']
print(list(filter(lambda x: x not in capitals, cities)))
