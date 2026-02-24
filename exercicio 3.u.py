entrada = input("digite seu nome:")

nome = len(entrada)

if nome >= 1 and nome <= 4:
    print ('seu nome é curto.')
elif nome > 4 and nome < 6:
    print ('seu nome é médio.')
elif nome >= 6:
    print ('seu nome é grande.')
else:
    print ('ouve um erro, verifique sua resposta.')