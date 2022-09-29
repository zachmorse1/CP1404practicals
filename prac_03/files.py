"""
CP1404/CP5632 - Practical
Files
"""
# 1.
OUTPUT_FILE = "name.txt"
name = input("Name: ")
out_file = open(OUTPUT_FILE, 'w')
print(f"{name}", file=out_file)
out_file.close()

# 2.
FILE = "name.txt"
names = open(FILE, 'r')
print(f"Your name is {names.readline()}")
out_file.close()

# 3.
FILE = "numbers.txt"
numbers = open(FILE, 'r')
number1 = int(numbers.readline())
number2 = int(numbers.readline())
total = number1 + number2
out_file.close()
print(total)

# 4.
FILE = "numbers.txt"
numbers = open(FILE, 'r')
total = 0
for number in numbers:
    total += int(number)
out_file.close()
print(total)
