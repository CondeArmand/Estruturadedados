class Pilha:
    def __init__(self):
        self.dados = []

    def Empty(self):
        self.dados = []

    def IsEmpty(self):
        return not bool(self.dados)

    def IsFull(self):
        return False

    def Push(self, elemento):
        self.dados.append(elemento)

    def Pop(self):
        if not self.IsEmpty():
            return self.dados.pop()
        else:
            return None

    def Top(self):
        if not self.IsEmpty():
            return self.dados[-1]
        else:
            return None

    def IsEquals(self, pilha):
        if len(self.dados) != len(pilha.dados):
            return False

        for i in range(len(self.dados)):
            if self.dados[i] != pilha.dados[i]:
                return False

        return True

    def invert(self):
        aux = Pilha()
        while not self.IsEmpty():
            aux.Push(self.Pop())
        self.dados = aux.dados
