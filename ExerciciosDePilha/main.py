from ExerciciosDePilha import pilha

pilha1 = pilha.Pilha()
pilha2 = pilha.Pilha()

pilha1.Push(1)
pilha1.Push(2)
pilha1.Push(3)

pilha2.Push(1)
pilha2.Push(2)
pilha2.Push(3)

print(pilha1.IsEquals(pilha2))

pilha1.invert()
print(pilha1.dados)

