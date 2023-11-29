import listaDuplamenteEncadeada as lista

lista = lista.ListaDuplamenteEncadeada()

for i in range(5):
    lista.inserir_inicio(i)

lista.inserir_depois_de(2, 10)

lista.inserir_final(20)

lista.remover_inicio()

lista.remover_apos_elemento(10)

lista.imprimir_lista()

print(lista.head.data)
print(lista.tail.data)