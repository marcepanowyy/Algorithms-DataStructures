
y = int(input('input your number >>> '))
x = 1

xTable = []
yTable = []

while True:

    yTable += [y]
    xTable += [x]

    if y == 2 or y == 4 or y == 1:
        break

    if y % 2 == 0:
        y //= 2
    else:
        y = 3 * y + 1

    x += 1

import matplotlib.pyplot as plt

plt.plot(xTable, yTable)
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()

