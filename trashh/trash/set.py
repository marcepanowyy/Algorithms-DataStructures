
example = set()

# print(*dir(example), sep='\n')
# print(help(example.add))

example.add(42)
example.add(False)
example.add(3.14159)
example.add('Thorium')
# print(example)

example.add(42)

# print(example)
# print(len(example))


odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

# print(odds.union(evens))
# print(odds.intersection(primes))
# print(primes.intersection(evens))
# print(primes.intersection(odds))
# print(evens.intersection(odds))
# print(primes.union(composites))