precios = { 
  'limonada' : 1.00, 
  'cafe': 1.50,
  'bizcocho': 2.00,
  'magdalena': 1.00,
  'macarrones': 3.50,
  'bocadillo': 2.50,
  'escalope con patatas': 4.50
  }

cesta = [] #Aqui guardaremos todos los productos pedidos

def pintar_comanda():
  print("--------------------------")
  print("Información de la comanda:")
  print("--------------------------")
  for elemento in cesta:
    print(elemento)
  print("--------------------------")

def factura():
  total = 0.0
  for producto in cesta:
    print(producto, precios[producto])
    total += precios[producto]
  print('Total: ',total, ' euros')

def mostrarCarta():
  print("--------------------------")
  print("Estos son los productos de la cafetería:")
  print("--------------------------")
  for producto in precios.keys():
    print(producto, precios[producto])

def realizarPedido():
  haTerminadoDePedir = False

  while not haTerminadoDePedir:
    alimento = input('¿Qué desea tomar?')  
    if alimento in precios.keys():
      print('De acuerdo')
      cesta.append(alimento)
    else:
      print('Lo lamento, no está en la carta')
  
    algoMas = input("¿desea algo mas?")
    if (algoMas == "si"):
      haTerminadoDePedir = False
    elif (algoMas == "no"):
      haTerminadoDePedir = True
      print('De acuerdo. ahora mismo se lo traigo')
    else:
      print('Perdone, no le he entendido')