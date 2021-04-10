from math import sqrt

for i in range(50, 55):
    max_num = int(sqrt(i))
    counter = 0
    for a in range(1, max_num):
        for b in range(1, max_num):
            if a <= b and a**2 + b**2 == i:
                counter += 1
    if counter == 1:
        print(a, b)

