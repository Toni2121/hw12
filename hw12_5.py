import random

list1 = []
for i in range(50):
    rnd_list = random.randint(100, 500)
    list1.append(rnd_list)

count_unique = len(set(list1))
print(list1, end=' ')
print()
print(f"Unique numbers: {count_unique}")