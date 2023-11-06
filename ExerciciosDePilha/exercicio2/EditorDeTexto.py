def editor_de_texto():
    from ExerciciosDePilha import pilha
    pilha_de_texto = pilha.Pilha()

    while True:
        comando = input("Digite um caractere ou comando (# para backspace, @ para apagar tudo, ou Q para sair): ")

        if comando == "Q" or comando == "q":
            break
        elif comando == "#":
            pilha_de_texto.Pop()  # Apaga o último caractere digitado
        elif comando == "@":
            pilha_de_texto.Empty()  # Apaga todo o texto
        else:
            pilha_de_texto.Push(comando)  # Adiciona o caractere à pilha

    texto_final = ""
    while not pilha_de_texto.IsEmpty():
        texto_final = pilha_de_texto.Pop() + texto_final

    print("Texto final: ", texto_final)


editor_de_texto()