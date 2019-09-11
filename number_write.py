import json
# f is a file object, store the set of numbers
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
# open the file in write mode
with open(filename, 'w') as f:
#store numbers in numbers.json using json.dump()
    json.dump(numbers, f)

username = input("What is your name?")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

