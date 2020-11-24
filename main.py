
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

for producto in precios.keys():
  print(producto, precios[producto])

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
  





#0 - cafe
#1 - donut
#2

for elemento in cesta:
  print(elemento)

