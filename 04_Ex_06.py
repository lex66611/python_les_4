from itertools import count, cycle

# итератор 1
print("*" * 20, "Iterator 1")
start = 7

for el in count(start):
    if el > 10:
        break

    print(el)

# итератор 2
print("*" * 20, "Iterator 2")
cycling_list = [4, 8, 15, 16, 23, 42]
max_iterations = 12
iteration_count = 0

for el in cycle(cycling_list):
    print(el)
    iteration_count += 1

    if iteration_count >= max_iterations:
        break
# завершено
