from itertools import count
from math import factorial

def fibogen():
    for el in count(1):
        yield factorial(el)

gen = fibogen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break
# завершено