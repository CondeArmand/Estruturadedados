from ExerciciosdeFila import fila


class Livro:
    def __init__(self, nome, disponibilidade=True):
        self.nome = nome
        self.disponibilidade = disponibilidade
        self.fila_espera = fila.FilaGenerica()

    def solicitar_livro(self, pessoa):
        if self.disponibilidade:
            self.disponibilidade = False
            print(f"{pessoa} retirou o livro '{self.nome}'.")
            return None
        else:
            print(f"{pessoa} entrou na fila de espera para o livro '{self.nome}'.")
            self.fila_espera.entrar(pessoa)
            return pessoa

    def devolver_livro(self):
        if not self.disponibilidade:
            self.disponibilidade = True
            if not self.fila_espera.estaVazia():
                proximo_na_fila = self.fila_espera.sair()
                print(f"O livro '{self.nome}' foi devolvido a {proximo_na_fila}.")
                return proximo_na_fila
            else:
                print(f"O livro '{self.nome}' foi devolvido.")
                return None




class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, nome):
        if nome in self.livros:
            print(f"O livro '{nome}' já está cadastrado.")
        else:
            self.livros[nome] = Livro(nome)
            print(f"O livro '{nome}' foi cadastrado com sucesso.")

    def retirar_livro(self, nome, pessoa):
        if nome in self.livros:
            livro = self.livros[nome]
            livro.solicitar_livro(pessoa)
        else:
            print(f"O livro '{nome}' não está cadastrado na biblioteca.")

    def devolver_livro(self, nome):
        if nome in self.livros:
            livro = self.livros[nome]
            livro.devolver_livro()
        else:
            print(f"O livro '{nome}' não está cadastrado na biblioteca.")

    def printar(self):
        for livro in self.livros:
            print(f"{livro}: {self.livros[livro].disponibilidade}")
