sum_1 = 0
sum_2 = 0
for number in range(5):
    result_1 = 4 ** (number + 1)
    sum_1 = sum_1 + result_1

for number in range(5):
    result_2 = 8 ** (number + 1)
    sum_2 = sum_2 + result_2

total = sum_1 + sum_2

print(total)
