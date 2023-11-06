import fila

# Exercício 1
fila1 = fila.Fila()

fila1.entrar(1)
fila1.entrar(2)
fila1.entrar(3)
fila1.entrar(4)

print(fila1.eCrescente())

# Exercício 2
fila2 = fila.Fila()

fila2.entrar(4)
fila2.entrar(3)
fila2.entrar(2)
fila2.entrar(1)

print(fila2.eCrescente())

fila2.invert()

print(fila2.eCrescente())


# Exercício 3
fila3 = fila.FilaGenerica()

fila3.entrar(1)
fila3.entrar(2)
fila3.entrar("três")
fila3.entrar(4)

print(fila3.estaCheia())
print(fila3.printar())
