#  Se achar necessario, faça import de outras bibliotecas





def cumulativo(lista):
    soma_cumulativa = 0
    lista_cumulativa = []

    for numero in lista:
        soma_cumulativa += numero
        lista_cumulativa.append(soma_cumulativa)

    return lista_cumulativa

# Exemplo de uso da função
lista = [2, 3, 4, 5]
resultado = cumulativo(lista)
print(resultado)

# Teste a sua função aqui (caso ache necessário)











