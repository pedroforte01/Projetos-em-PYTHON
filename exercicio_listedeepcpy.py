import copy

#========== LIST/DADOS ===========#
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

###### COPIA COM O DEEP COPY 1 #######

#========== VARIAVEIS ===========#
produtos_copia = copy.deepcopy(produtos)
produtos_ordenados = copy.deepcopy(produtos)
novos_preços = []
QUEBRA_LINHA = '\n'


#========== MAIN ============#

    #=======> JUROS NO PREÇO <=======#

print (QUEBRA_LINHA + 50 * '=' + QUEBRA_LINHA * 2 + 'PRIMEIRA FORMA DE EXIBIR A LISTA.' )
for i in produtos_copia:
    i['preco'] *= 1.10 # ATRIBUI o resultado (multiplicação e atribuição)
    novos_preços.append(i['preco'])  # Guarda como float
    print (f"{i['preco']:.2f}")


print (QUEBRA_LINHA +'SEGUNDA FORMA DE EXIBIR A LISTA.')
print (*[f"{p:.2f}" for p in novos_preços] , sep= ', ')


print (f"""
TERCEIRA FORMA DE EXIBIR A LISTA (Opção especifica):
{novos_preços[0]:.2F}'
""") 

###############################
print (70 * '=' + QUEBRA_LINHA)
###############################


    #=======> PRODUTOS ORDENADOS <=========#

def ordenar_por_nome(produtos, crescente=True):
    produtos.sort (
        key=lambda p: p['nome'] ,
        reverse=not crescente
        )
    
    print (' TABELA COM OS PRODUTOS ORDENADOS & COM PREÇO ATUALIZADO : ')
    for p in produtos:
        print (
            f'{p["nome"]} : R$ {p["preco"]:.2f}', # EXIBIÇÃO SEM JUROS.
            ' | 10% JUROS => | ', f'{p["nome"]} : R$ {p["preco"] * 1.10:.2f}', # EXIBIÇÃO COM JUROS.            
            )
    
    print (QUEBRA_LINHA + 70 * '=' + QUEBRA_LINHA)

ordenar_por_nome(produtos_ordenados, crescente=True)

