def verifica_parenteses(equacao):
    from ExerciciosDePilha import pilha

    pilha = pilha.Pilha()
    abertos = 0  # Contador de parênteses abertos
    fechados = 0  # Contador de parênteses fechados

    for caractere in equacao:
        if caractere == '(':
            pilha.Push(caractere)
            abertos += 1
        elif caractere == ')':
            fechados += 1
            if pilha.IsEmpty():
                return False, abertos, fechados
            pilha.Pop()

    return pilha.IsEmpty(), abertos, fechados


equacao = input("Digite a equação matemática: ")
equilibrio, abertos, fechados = verifica_parenteses(equacao)

if equilibrio:
    print("Os parênteses estão equilibrados.")
    print(f"Quantidade de parênteses abertos: {abertos}")
    print(f"Quantidade de parênteses fechados: {fechados}")
else:
    print("Os parênteses não estão equilibrados.")
    print(f"Quantidade de parênteses abertos: {abertos}")
    print(f"Quantidade de parênteses fechados: {fechados}")
