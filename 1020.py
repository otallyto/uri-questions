entrada = int(input())
ano = 0
mes = 0
dia = 0
while 1:
    if(entrada >= 365):
        entrada = entrada - 365
        ano = ano + 1
    elif(entrada >= 30):
        entrada = entrada - 30
        mes = mes + 1
    elif(entrada < 30):
        dia = entrada
        break

print('%d ano(s)' % ano)
print('%d mes(es)' % mes)
print('%d dia(s)' % dia)
