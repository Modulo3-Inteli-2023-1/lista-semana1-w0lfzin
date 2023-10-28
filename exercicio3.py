#  Se achar necessario, faça import de outras bibliotecas





def soma_dos_aninhados(lista_de_listas):
    soma_total = 0
    for lista in lista_de_listas:
        soma_total += sum(lista)
    return soma_total

lista = [[11, 22], [33], [44, 55, 66]]
outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]

resultado_lista = soma_dos_aninhados(lista)
resultado_outra_lista = soma_dos_aninhados(outra_lista)

print("Resultado da primeira lista aninhada:", resultado_lista)
print("Resultado da segunda lista aninhada:", resultado_outra_lista)








# Teste a sua função aqui (caso ache necessário)











