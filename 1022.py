a, b, c, d = input().split(' ')
somaAB = a + b
somaCD = c + d
if(b > c and d > a and somaAB > somaCD and somaAB > 0 and somaCD > 0 and a % 2 == 0):
  print('Valores aceitos')
else:
  print('Valores nao aceitos')
