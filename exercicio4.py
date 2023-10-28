#  Se achar necessario, faça import de outras bibliotecas





def tem_duplicados(lista):
    if len(lista) == len(set(lista)):
        return False
    else:
        return True

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 3, 4, 5]

print("A lista 1 tem duplicados?", tem_duplicados(lista1))
print("A lista 2 tem duplicados?", tem_duplicados(lista2))



# Teste a sua função aqui (caso ache necessário)











