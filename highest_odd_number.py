def highest_odd_number(nums):
    highest_odd = None

    for num in nums:
        if num % 2 != 0:
            if highest_odd is None or num > highest_odd:
                highest_odd = num

    return highest_odd



numbers = [3, 7, 2, 9, 4, 6, 5]
result = highest_odd_number(numbers)
print(result)  # Output: 9
