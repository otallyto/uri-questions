entrada = float(input())
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
moeda50 = 0
moeda25 = 0
moeda10 = 0
moeda5 = 0
moeda1 = 0
aux = entrada
while 1:
    print('%f'%entrada)
    if(entrada >= 100):
        entrada -= 100
        cem = cem + 1
    elif(entrada >= 50):
        entrada = entrada - 50
        cinquenta = cinquenta + 1
    elif(entrada >= 20):
        entrada = entrada - 20
        vinte = vinte + 1
    elif(entrada >= 10):
        entrada = entrada - 10
        dez = dez + 1
    elif(entrada >= 5):
        entrada = entrada - 5
        cinco = cinco + 1
    elif(entrada >= 2):
        entrada = entrada - 2
        dois = dois + 1
    elif(entrada >= 1):
        entrada = entrada - 1
        um = um + 1
    elif(entrada >= 0.50):
        entrada = entrada - 0.50
        moeda50 = moeda50 + 1
    elif(entrada >= 0.25):
        entrada = entrada - 0.25
        moeda25 = moeda25 + 1
    elif(entrada >= 0.10):
        entrada = entrada - 0.10
        moeda10 = moeda10 + 1
    elif(entrada >= 0.05):
        entrada = entrada - 0.05
        moeda5 = moeda5 + 1
    elif(entrada >= 0.01):
        print("%f"%entrada)
        entrada = entrada - 0.01
        moeda1 = moeda1 + 1
    else:
      break
print('NOTAS:')
print('%d nota(s) de R$ 100.00' % cem)
print('%d nota(s) de R$ 50.00' % cinquenta)
print('%d nota(s) de R$ 20.00' % vinte)
print('%d nota(s) de R$ 10.00' % dez)
print('%d nota(s) de R$ 5.00' % cinco)
print('%d nota(s) de R$ 2.00' % dois)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % um)
print('%d moeda(s) de R$ 0.50' % moeda50)
print('%d moeda(s) de R$ 0.25' % moeda25)
print('%d moeda(s) de R$ 0.10' % moeda10)
print('%d moeda(s) de R$ 0.05' % moeda5)
print('%d moeda(s) de R$ 0.01' % moeda1)
print()