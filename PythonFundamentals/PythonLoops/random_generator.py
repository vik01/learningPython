import random

def sum(sum_list):
    int_sum = 0
    for i in sum_list:
        int_sum += i
    return int_sum

random_values = [random.randint(75, 100) for _ in range(49)]
random_values_2 = [random.randint(70, 95) for _ in range(42)]

print(f"Yes: {random_values}")

print(f"No: {random_values_2}")
