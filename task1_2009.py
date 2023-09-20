import random

def calculate_product(numbers):
    product = 1

    for element in numbers:
        product *= element

    return product


number_list = [random.randint(1, 10) for _ in range(5)]
result = calculate_product(number_list)

print("Result:", result)