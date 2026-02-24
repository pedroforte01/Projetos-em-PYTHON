nome = input('digite um nome:')
tamanho_nome = (len(nome))
####

print (f'nome: {nome}')
print (f'tamanho_nome: {tamanho_nome}')
print (f'ultima letra do nome: {nome [tamanho_nome-1]}')


rep = 0
while rep < tamanho_nome:
    for letra in nome:
        print (letra + '* ')
        rep += 1


rep = 0
novo_nome = ''
while rep < len(nome):
    letra = nome[rep]
    novo_nome += f'*{letra}'
    rep += 1 

print (novo_nome)

print ('fim do programa')
