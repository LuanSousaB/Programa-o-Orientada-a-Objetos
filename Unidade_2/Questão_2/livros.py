class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco

livro1 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 49.90)
livro2 = Livro("Arsène Lupin, o Ladrão de Casaca", "Maurice Leblanc", 1907, 39.90)

print("Título:", livro1.titulo, ", Autor:", livro1.autor, ", Ano:", livro1.ano_publicacao, ", Preço: R$", livro1.preco)
print("Título:", livro2.titulo, ", Autor:", livro2.autor, ", Ano:", livro2.ano_publicacao, ", Preço: R$", livro2.preco)
