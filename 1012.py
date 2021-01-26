A, B, C = input().split(' ')

def areaTrianguloRetangulo(base, altura):
    return (float(base) * float(altura))/2

def areaCirculo(raio):
    pi = 3.14159
    return pi * float(raio) ** 2

def areaTrapezio(baseMaior, baseMenor, altura):
    return ((float(baseMaior) + float(baseMenor)) / 2) * float(altura)

def areaQuadrado(lado):
    return float(lado) ** 2

def areaRetangulo(base, altura):
    return float(base) * float(altura)

triangulo = areaTrianguloRetangulo(A, C)
circulo = areaCirculo(C)
trapezio = areaTrapezio(A, B, C)
quadrado = areaQuadrado(B)
retangulo = areaRetangulo(A, B)

print('TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f' %
      (triangulo, circulo, trapezio, quadrado, retangulo))
