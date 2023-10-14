from tiendalibros.modelo.item_compra import ItemCompra

class CarroCompras:
    def __init__(self):
        self.items = []  

    def agregar_item(self, libro, cantidad):
        item = ItemCompra(libro, cantidad)  
        self.items.append(item) 
        return item 

    def calcular_total(self):
        total = 0.0  
        for item in self.items:
            subtotal = item.calcular_subtotal()  
            total += subtotal 

        return total 
    
    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]

