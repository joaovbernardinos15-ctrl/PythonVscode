
biblioteca = {
    "978-8535902778": {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis"
    },
    "978-8572326483": {
        "titulo": "O Cortiço",
        "autor": "Aluísio Azevedo"
    }
}


def consultar_livro(isbn):
    if isbn in biblioteca:
        livro = biblioteca[isbn]
        print(f"ISBN: {isbn}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
    else:
        print("Livro não encontrado no catálogo.")



isbn_consulta = input("Digite o ISBN do livro: ")
consultar_livro(isbn_consulta)
