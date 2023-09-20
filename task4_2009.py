import random

def remove_element(lst, num):
    count_removed = 0

    while num in lst:
        lst.remove(num)
        count_removed += 1

    return count_removed


# Створюємо список
random_list = [random.randint(1, 10) for _ in range(10)]

# Генеруємо число для видалення
number_to_remove = random.randint(1, 10)

removed_count = remove_element(random_list, number_to_remove)
print("Number of removed elements:", removed_count)
print("List after removal:", random_list)