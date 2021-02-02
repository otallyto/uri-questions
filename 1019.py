entrada = int(input())
hora = 0
minuto = 0
segundo = 0
while 1:
    if(entrada >= 3600):
      entrada = entrada - 3600
      hora = hora + 1
    elif(entrada >= 60):
      entrada = entrada - 60
      minuto = minuto + 1
    elif(entrada < 60):
      segundo = entrada
      break
print('%d:%d:%d'%(hora,minuto,segundo))