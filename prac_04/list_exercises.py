import statistics

numbers = []
for i in range(0, 5):
    number = int(input("Number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]} \nThe last number is {numbers[-1]} \nThe smallest number is {min(numbers)} \nThe largest number is {max(numbers)} \nThe average of the numbers is {statistics.mean(numbers)}")
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")