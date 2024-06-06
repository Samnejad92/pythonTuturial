age = 12
height = 178.5
isMale = True
print(f'Age : {age}, Height : {height}, Gender : {isMale}, Age : 12, Height : 178.5, Gender : True')

variable = 5
print(f"{variable=}")

greeting = "Hello %s!"
name = input("Please enter your name:\n")
print(greeting % name)

greeting = "Hello %s with %d years old!"
name = input("Please enter your name:\n")
age = int(input("Please enter your age:\n"))
print(greeting % (name, age))

greeting = "Hello {} with {} years old!"
name = input("Please enter your name:\n")
age = int(input("Please enter your age:\n"))
print(greeting.format(name, age))