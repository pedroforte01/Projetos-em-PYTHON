#terminar
lista = []
posição = 0

while True:
    print ('selecionar uma opção:')
    resposta = input ('[i]nserir [a]pagar [l]istar [e]ncerrar ').lower()

    if 'i' in resposta:
        item = input('escreva o item que deseja inserir: ')
        lista.append (item)
        posição += 1

    elif 'a' in resposta:
        indice_str = input ('Qual o indice da lista apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        
        except TypeError:
            print ('digite apenas numeros inteiros.')

        except ValueError:
            print ('apenas numeros inteiros.')
  
        except IndexError:
            print ('indice não existe na lista')

    elif 'l' in resposta:
       
        if len(lista) == 0:
           print ('Não há nada na lista.')

        for i, lista in enumerate(lista):
            print (i, lista)

