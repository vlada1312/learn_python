Xmin, Ymin = -10, -20
Xmax, Ymax = 10, 20

for y in range(Ymax, Ymin - 1, -1):
    for x in range(Xmin, Xmax + 1):        
        if y == x**2 + 2*x:
            print(' * ', end='')
        elif y == 0:
            print('---', end = '')
        elif x == 0:
            print('|', end = '')
        else:
            print(' . ', end='')
    print('')
       
