    #LER NUMERO INT 

entrada = input('Digite um numero inteiro:')

try:
    entrada_int = int(entrada)
    print ('Numero inteiro')
except:
    print ('seu numero não é inteiro')

if entrada.isdigit():
    entrada_int = int(entrada)
    resto = entrada_int % 2 == 0

    if resto is True:
        print (f'O numero {entrada_int} é Par.')
    else:
        print (f'O numero {entrada_int} é impar.')



