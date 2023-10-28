#  Se achar necessario, faça import de outras bibliotecas





def multiplas_operacoes(a, b):
    # Soma
    soma = a + b

    # Subtração
    subtracao = a - b

    # Multiplicação
    multiplicacao = a * b

    if b != 0:
        divisao = a / b
    else:
        divisao = 0

    return soma, subtracao, multiplicacao, divisao

resultado = multiplas_operacoes(10, 5)
print("Soma:", resultado[0])
print("Subtração:", resultado[1])
print("Multiplicação:", resultado[2])
print("Divisão:", resultado[3])

# Teste a sua função aqui (caso ache necessário)











