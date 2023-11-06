def interpretar_expressao_posfixa(expressao):
    from ExerciciosDePilha import pilha
    pilha = pilha.Pilha()
    operadores = set("+-*/")

    for token in expressao.split():
        if token not in operadores:
            # Se o token não for um operador, empilhe na pilha
            pilha.Push(float(token))
        else:
            # Se o token for um operador, retire os operandos, calcule e empilhe o resultado
            operando2 = pilha.Pop()
            operando1 = pilha.Pop()
            if token == "+":
                resultado = operando1 + operando2
            elif token == "-":
                resultado = operando1 - operando2
            elif token == "*":
                resultado = operando1 * operando2
            elif token == "/":
                resultado = operando1 / operando2
            pilha.Push(resultado)

    # O resultado final deve estar no topo da pilha
    return pilha.Top()


expressao_posfixa = input("Digite a expressão posfixa: ")
resultado = interpretar_expressao_posfixa(expressao_posfixa)
print("Resultado da expressão:", resultado)
