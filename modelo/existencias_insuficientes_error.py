from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):

    def __init__(self, titulo, isbn, cantidad_a_comprar, existencias):
        super().__init__(f"El libro con título {titulo} y ISBN {isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {cantidad_a_comprar}, existencias: {existencias}")
        self.cantidad_a_comprar = cantidad_a_comprar

    def __str__(self):
        return f"El libro con título {self.titulo} y ISBN {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"
    