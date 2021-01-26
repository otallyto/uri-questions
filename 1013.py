a, b, c = input().split()

def maiorAB(a, b):
    A = int(a)
    B = int(b)
    return ((A+B) + abs(A-B))/2

maior= maiorAB(a,b)
maiorTotal = maiorAB(maior,c)

print('%d eh o maior' %maiorTotal)
