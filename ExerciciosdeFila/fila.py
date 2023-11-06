class Fila:
    def __init__(self):
        self.fila = []

    def esvaziar(self):
        self.fila = []

    def estaVazia(self):
        return self.fila == []

    def estaCheia(self):
        return len(self.fila) == 10

    def entrar(self, item):
        if not self.estaCheia():
            self.fila.append(item)
        else:
            print("A fila está cheia!")

    def sair(self):
        if not self.estaVazia():
            self.fila.pop(0)
        else:
            print("A fila está vazia!")

    def eCrescente(self):
        if not self.estaVazia():
            for i in range(len(self.fila)-1):
                if self.fila[i] > self.fila[i+1]:
                    return False
            return True
        else:
            print("A fila está vazia!")

    def invert(self):
        if not self.estaVazia():
            aux = []
            for i in range(len(self.fila)):
                aux.append(self.fila.pop())

            self.fila = aux
        else:
            print("A fila está vazia!")


class FilaGenerica:
    def __init__(self):
        self.fila = []

    def esvaziar(self):
        self.fila = []

    def estaVazia(self):
        return len(self.fila) == 0

    def estaCheia(self, tamanho_maximo=None):
        if tamanho_maximo is not None:
            return len(self.fila) == tamanho_maximo
        else:
            return False

    def entrar(self, item, tamanho_maximo=None):
        if tamanho_maximo is not None and self.estaCheia(tamanho_maximo):
            print("A fila está cheia!")
        else:
            self.fila.append(item)

    def sair(self):
        if not self.estaVazia():
            element = self.fila[0]
            self.fila.pop(0)
            return element
        else:
            print("A fila está vazia!")

    def printar(self):
        print(self.fila)

    def eCrescente(self):
        if not self.estaVazia():
            for i in range(len(self.fila)-1):
                if self.fila[i] > self.fila[i+1]:
                    return False
            return True
        else:
            print("A fila está vazia!")

    def invert(self):
        if not self.estaVazia():
            aux = []
            for i in range(len(self.fila)):
                aux.append(self.fila.pop())

            self.fila = aux
        else:
            print("A fila está vazia!")


