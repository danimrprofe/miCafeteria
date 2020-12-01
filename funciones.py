import datetime

def mostrarHora():
  now = datetime.datetime.now()
  print ("Fecha : ",now.strftime("%Y-%m-%d %H:%M:%S"))


precios = { 
  'limonada' : 1.00, 
  'cafe': 1.50,
  'bizcocho': 2.00,
  'magdalena': 1.00,
  'macarrones': 3.50,
  'bocadillo': 2.50,
  'escalope con patatas': 4.50
  }

cesta = {} #Aqui guardaremos todos los productos pedidos





def mostrarCarta():
  print("--------------------------")
  print("Estos son los productos de la cafetería:")
  print("--------------------------")
  for producto in precios.keys():
    print(producto,"\t\t\t\t", precios[producto])

