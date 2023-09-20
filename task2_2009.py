import random

def find_minimum(numbers):
    if not numbers:
        return None

    minimum = numbers[0]

    for element in numbers:
        if element < minimum:
            minimum = element

    return minimum

# Генеруємо рандомний список цілих чисел
random_list = [random.randint(1, 10) for _ in range(5)]

result = find_minimum(random_list)

print("Result:", result)