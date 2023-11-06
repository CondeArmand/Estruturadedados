import SistemaDaBiblioteca
# Exemplo de uso

biblioteca = SistemaDaBiblioteca.Biblioteca()
biblioteca.cadastrar_livro("Harry Potter")
biblioteca.cadastrar_livro("Senhor dos Anéis")

biblioteca.retirar_livro("Harry Potter", "Alice")
biblioteca.retirar_livro("Harry Potter", "Bob")

biblioteca.devolver_livro("Harry Potter")

biblioteca.retirar_livro("Harry Potter", "Charlie")

biblioteca.printar()