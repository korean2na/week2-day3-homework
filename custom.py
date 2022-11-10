def houseArea():
    l = input('Length of house in feet? ')
    w = input('Width of house in feet? ')
    a = int(l) * int(w)
    print(f'The area of the house is {a} sq ft.')
    return a

from math import pi

def circle():
    r = input('Radius of the circle? ')
    circ = 2 * pi * int(r)
    area = pi * int(r) ** 2
    print(f'Circumfrence of the circle is {circ} \nand area of the circle is {area}.')
    return circ, area