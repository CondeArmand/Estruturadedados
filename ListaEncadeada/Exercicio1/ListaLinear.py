class ListaLinear:
    def __init__(self):
        self.lista = []

    def inserir(self, item):
        self.lista.append(item)

    def retirar(self, item):
        if item in self.lista:
            self.lista.remove(item)
        else:
            print("Item não encontrado na lista.")

    def localizar(self, item):
        if item in self.lista:
            return self.lista.index(item)
        else:
            return -1  # Retorna -1 se o item não estiver na lista

    def combinar(self, *listas):
        nova_lista = self.lista.copy()
        for l in listas:
            nova_lista.extend(l.lista)
        return nova_lista

    def dividir(self, tamanho):
        return [self.lista[i:i + tamanho] for i in range(0, len(self.lista), tamanho)]

    def copiar(self):
        return self.lista.copy()

    def ordenar(self, campo=None):
        if campo:
            self.lista.sort(key=lambda x: x[campo])
        else:
            self.lista.sort()

    def pesquisar(self, valor):
        return valor in self.lista

    def concatenar(self, outra_lista):
        return self.lista + outra_lista.lista

    def dividir_lista(self, indice):
        return self.lista[:indice], self.lista[indice:]

    def copiar_lista(self):
        return self.lista.copy()

    def pesquisar_elemento(self, elemento):
        return elemento in self.lista
