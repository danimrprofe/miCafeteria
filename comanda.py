class comanda{{
  def __init__ (self, numeroMesa):
    mesa = numeroMesa
    cesta = {}
    fecha = datetime.datetime.now()
    factura_cambio = 0.0
    factura_cantidadPagada = 0.0
    factura_pagada = False
  
  def imprimirFecha():
    print ("Fecha : ",self.fecha.strftime("%Y-%m-%d %H:%M:%S"))

  def imprimir():
    print("--------------------------")
    print("Información de la comanda:")
    mostrarHora()
    print("--------------------------")
    if not cesta:
      print("No hay elementos en la comanda")
    else:
      for elemento in cesta.keys():
        print(cesta[elemento], "\t\t ", elemento)
    print("--------------------------")

  def realizarPedido():
    haTerminadoDePedir = False

    while not haTerminadoDePedir:
      alimento = input('¿Qué desea tomar?')  
      if alimento in precios.keys():
        print('De acuerdo')
        if alimento in cesta.keys():
          cesta[alimento] += 1
        else:
          cesta[alimento] = 1
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

  def factura():
    total = 0.0
    print("--------------------------")
    print("Factura:")
    print("--------------------------")
    for producto in cesta.keys():
      print(producto, "\t\t ", cesta[producto], " ", cesta[producto]*precios[producto])
      total += cesta[producto]*precios[producto]
    print('Total: ',total, ' euros')

  def pagar():
    self.factura_pagada = True

}