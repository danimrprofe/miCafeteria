class Carta:
    
    def __init__ (self):
        self.precios = { 
            'limonada' : 1.00, 
            'cafe': 1.50,
            'bizcocho': 2.00,
            'magdalena': 1.00,
            'macarrones': 3.50,
            'bocadillo': 2.50,
            'escalope con patatas': 4.50
        }

    def mostrarCarta(self):
        print("--------------------------")
        print("Estos son los productos de la cafetería:")
        print("--------------------------")
        for producto in self.precios.keys():
            print(producto,"\t\t\t\t", self.precios[producto])
        input()