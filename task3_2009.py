import random

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for number in numbers:
        if is_prime(number):
            count += 1
    return count

# Генеруємо список чисел
random_list = [random.randint(1, 100) for _ in range(10)]

# Знаходимо кількість простих чисел у рандомному списку
prime_count = count_primes(random_list)

print("Result:", prime_count)
