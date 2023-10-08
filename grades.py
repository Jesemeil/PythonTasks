import statistics

grades = [85, 93, 45, 89, 85]

result_1 = statistics.mean(grades)

result_2 = statistics.median(grades)

result_3 = statistics.mode(grades)

result_4 = sorted(grades)

print(" The mean is", result_1, ", median is", result_2, "and the mode is ", result_3, ".", )

print("The sorted grades are", result_4, end =' ')


