import random
NUMBERS_PER_LINE = 6
HIGHEST_NUMBER = 45
LOWEST_NUMBER = 1
lines_of_output = int(input("How many quick picks? "))
for i in range(lines_of_output):
    NUMBERS = []
    for j in range(NUMBERS_PER_LINE):
        new_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
        while new_number in NUMBERS:
            new_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
        NUMBERS.append(new_number)
    NUMBERS.sort()
    print(" ".join(f"{number:2}" for number in NUMBERS))
