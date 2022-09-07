
from random import randint

# time complexity O(n)
# space complexity O(1) (except for the given array)


def shuffle(arr):
    last_index = len(arr)-1
    while last_index > 0:
        rand_index = randint(0, last_index)
        arr[rand_index], arr[last_index] = arr[last_index], arr[rand_index]
        last_index -= 1

    rand_index = randint(0, len(arr)-1)
    arr[0], arr[rand_index] = arr[rand_index], arr[0]


arr = []

for i in range(1000):
    arr.append(i)

print("arr before shuffle:")
print(arr)
print('')

shuffle(arr)

print('shuffled arr:')
print(arr)
