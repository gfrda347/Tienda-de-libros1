from tiendalibros.modelo.libro_error import LibroError

class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__(f"El libro con título {titulo} y ISBN {isbn} ya existe en el catálogo")

    def __str__(self):
        return f"El libro con título {self.args[0]} y ISBN: {self.args[1]} ya existe en el catálogo"

