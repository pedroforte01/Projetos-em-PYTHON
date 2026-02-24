print ('CALCULADORA 2025')
''''''
while True:
    num1 = input ('Digite um numero: ')
    num2 = input ('Digite outro numero: ')
    oper = input ('Qual será a operação: ')

    num1_float = 0
    num2_float = 0
    num_valid = None
    
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_valid = True
    except:
        num_valid = None

    if num_valid is None:
        print ('Algum numero foi digitado incorretamente!')
        continue

    oper_valid = '+-/*'
    
    if oper not in oper_valid:
        print ('Operador invalido!')
        continue

    if len(oper) > 1:
        print ('Digite apenas 1 operador!')
        continue
    
    
    if oper == '+':
        print (f'{num1_float} + {num2_float} = ', num1_float + num2_float)
    
    elif oper == '/':
        print (f'{num1_float} / {num2_float} = ', num1_float / num2_float)
    
    elif oper == '*':
        print (f'{num1_float} * {num2_float} = ', num1_float * num2_float)
    
    elif oper == '-':
        print (f'{num1_float} - {num2_float} = ', num1_float - num2_float)
 
    else:
        print('deu ruim')

    sair = input ('deseja sair? [s]im! ').lower().startswith('s')
    
    if sair is True:
        break