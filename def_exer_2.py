x = (10)
y = (5)  

def virus(x, y):
    resul_soma = x + y
    resul_sub = x - y
    resul_multi = x * y
    resul_divi = x / y
    
    print (f"{x} + {y} = {resul_soma:.0f}")
    print (f"{x} - {y} = {resul_sub:.0f}")
    print (f"{x} * {y} = {resul_multi:.0f}")
    print (f"{x} / {y} = {resul_divi:.0f}") 
    
   
virus(x, y)   

'''
def ordenar_por_nome(produtos, crescente=True):
    produtos.sort (
        key=lambda p: p['nome'] ,
        reverse=not crescente
        )
    return produtos

ordenar_por_nome(produtos_ordenados, crescente=True)

print (produtos_ordenados)
'''