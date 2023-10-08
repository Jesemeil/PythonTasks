def check_duplicates(input_list):
    duplicates = set()
    seen = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)


result = check_duplicates([1, 2, 2, 2, 3, 4, 4, 4, 5])
print(result)
