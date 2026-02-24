perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


alternativas = ['a)', 'b)', 'c)', 'd)']

for pergunta in perguntas:
    print (pergunta['Pergunta'])
    
    opcoes = pergunta['Opções']
    resposta = pergunta['Resposta']

    reps = 0

    for repete in opcoes:
            print (alternativas[reps], opcoes[reps])
            reps += 1                 

    retorno = input ('qual a resposta?')

    reps = 0
    def verificacao(retorno):
        for esta_dentro in opcoes:
                
            if retorno == esta_dentro:
                if retorno == resposta:
                    print ('Você acertou👍')
                else:
                    print ('Você errou❌')
                
            else:
                reps += 1
            if reps == 4:
                retorno = input('Digite um numero que está nas altenativas.')
                verificacao (retorno)
    verificacao(retorno)

    
    
