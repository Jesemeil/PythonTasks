squared_numbers = [100, 400, 900, 1600, 2500]

minimum = squared_numbers[0]
maximum = squared_numbers[0]

for num in squared_numbers:
    if num < minimum:
        minimum = num
    elif num > maximum:
        maximum = num

difference = maximum - minimum

print(difference)
