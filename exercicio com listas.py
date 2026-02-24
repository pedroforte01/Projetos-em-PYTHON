lista = ['pedro','iva','maria']

lista_reps = len(lista)

rep_while = 0
while rep_while < lista_reps: 
    for nomes in lista:
        print (rep_while, lista[rep_while])
        rep_while += 1

