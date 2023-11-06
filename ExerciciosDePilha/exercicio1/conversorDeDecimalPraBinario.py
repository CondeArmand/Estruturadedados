def decimal_para_binario(decimal):
    from ExerciciosDePilha import pilha
    pilha = pilha.Pilha()

    if decimal == 0:
        pilha.Push(0)

    while decimal > 0:
        resto = decimal % 2
        pilha.Push(resto)
        decimal = decimal // 2

    binario = ''
    while pilha.Top() is not None:
        binario += str(pilha.Pop())

    return binario


decimal = int(input("Digite um número decimal: "))
binario = decimal_para_binario(decimal)
print(f'O número binário correspondente é: {binario}')
