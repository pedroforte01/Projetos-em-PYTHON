word = 'A vida só pode ser compreendida olhando-se para trás' \
'; mas só pode ser vivida olhando-se para frente'

i = 0
rep = 0
posi_maior = 0
while i < len(word):
    word_letra = word[i]

    if word_letra == ' ':
        i += 1
        continue

    word_maior = word.count(word_letra)
    
    if rep < word_maior:
        rep = word_maior
        letra = word_letra

    print (word_letra, word_maior)
    i += 1

print (f'a letra mais repeitdo foi "{letra}" e foi repetido {rep} vezes')