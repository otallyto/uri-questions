import math

x1, y1 = input().split(' ')
x2, y2 = input().split(' ')

a = (float(x2) - float(x1)) ** 2
b = (float(y2) - float(y1)) ** 2

result = math.sqrt(a + b)

print('%.4f' % result)
