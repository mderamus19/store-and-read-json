# use json.load() to read the list of numbers back into memory
import json
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)

