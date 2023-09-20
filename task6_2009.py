def calculate_degree(numbers, degree):
    results = []

    for element in numbers:
        result = element ** degree
        results.append(result)

    return results

number_list = [2, 3, 4, 5]
degree = 2

results = calculate_degree(number_list, degree)
print("Result:", results)
