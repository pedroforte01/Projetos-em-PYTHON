entrada = int(input('digite as horas em numeros inteiros:'))

try:
    horas = int(entrada)

    if horas >= 5 and horas <= 11:
        print ('Bom dia :)')
    elif horas >= 12 and horas <= 18:
        print ('Boa tarde!')    
    elif horas > 18:
        print ('Boa noite ;)')
    else:
        print ('não conheço este valor')
        print('carlos junior')
except:
    print ('digite apenas numeros inteiro')
              