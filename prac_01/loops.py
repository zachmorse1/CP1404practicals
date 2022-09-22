for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number_stars = int(input("Number of stars: "))
for i in range(1, number_stars + 1, 1):
    print('*', end='')
print()

# d.
lines = int(input("Number of lines: "))
for i in range(lines):
    for j in range(0, i+1):
        print('*', end="")
    print()