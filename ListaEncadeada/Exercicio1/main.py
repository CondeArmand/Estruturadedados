import ListaLinear

lista = ListaLinear.ListaLinear()

for i in range(10):
    lista.inserir(i)

print(lista.lista)

lista.retirar(5)

print(lista.lista)

print(lista.localizar(5))
print(lista.localizar(4))

lista2 = ListaLinear.ListaLinear()

for i in range(10, 20):
    lista2.inserir(i)

print(lista2.lista)

# Concatenando duas listas
lista3 = lista.concatenar(lista2)
print(lista3)

# Dividindo uma lista em duas
lista4, lista5 = lista.dividir_lista(5)
print(lista4)

print(lista5)

# Copiando uma lista
lista6 = lista.copiar_lista()
print(lista6)


# Pesquisando um elemento na lista
print(lista.pesquisar_elemento(5))
