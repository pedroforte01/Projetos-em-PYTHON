import os
palavra_chave = 'perfume'
rsave = ''
tentativas = 0
#"nao pode ser 2 ou + letras."
#"nao pode ser numero"
# eu sei que tem o while e o for/in 

while True:

    r = input("digite uma letra: ").lower()

    if len(r) > 1:
        print ("nao pode ser 2 ou + letras.")
        continue

    if r in palavra_chave:
        rsave += r

    palavra_formada = ''
    for r in palavra_chave:
        if r in rsave:
            palavra_formada += r
        else:
            palavra_formada += '*'
    print ('palavra formada: ', palavra_formada)
    
    tentativas += 1

    if palavra_formada == palavra_chave:
        os.system('cls')
        print ('VOCE ACERTOU A PALAVRA, PARABENS!')
        print ('A palavra secreta era: ', palavra_formada)
        print ('seu numero de tentativas foram ', tentativas)
        break

   