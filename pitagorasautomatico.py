from random import randint
from math import hypot

co = randint(1, 10)
ca = randint(11, 50)
print('A hipotenusa é:{:.2f}'.format(hypot(co, ca)))