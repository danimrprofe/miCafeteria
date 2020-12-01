import datetime
from carta import *

class Comanda:

  def __init__ (self, numeroMesa, cartaPasada):
    self.cartaRestaurante = cartaPasada
    self.mesa = numeroMesa
    self.cesta = {}
    self.fecha = datetime.datetime.now()
    self.factura_cambio = 0.0
    self.factura_cantidadPagada = 0.0
    self.factura_pagada = False
    self.haTerminadoDePedir = False
  
  def imprimirFecha(self):
    print ("Fecha : ",self.fecha.strftime("%Y-%m-%d %H:%M:%S"))

  def imprimir(self):
    print("--------------------------")
    print("Información de la comanda:")
    self.imprimirFecha()
    print("--------------------------")
    if not self.cesta:
      print("No hay elementos en la comanda")
    else:
      for elemento in self.cesta.keys():
        print(self.cesta[elemento], "\t\t ", elemento)
    print("--------------------------")

  def realizarPedido(self):
    

    while not self.haTerminadoDePedir:
      alimento = input('¿Qué desea tomar?')  
      if alimento in self.cartaRestaurante.precios.keys():
        print('De acuerdo')
        if alimento in self.cesta.keys():
          self.cesta[alimento] += 1
        else:
          self.cesta[alimento] = 1
      else:
        print('Lo lamento, no está en la carta')
    
      algoMas = input("¿desea algo mas?")
      if (algoMas == "si"):
        self.haTerminadoDePedir = False
      elif (algoMas == "no"):
        self.haTerminadoDePedir = True
        print('De acuerdo. ahora mismo se lo traigo')
      else:
        print('Perdone, no le he entendido')

  def factura(self):
    total = 0.0
    print("--------------------------")
    print("Factura:")
    print("--------------------------")
    for producto in self.cesta.keys():
      print(producto, "\t\t ", self.cesta[producto], " ", self.cesta[producto]*self.cartaRestaurante.precios[producto])
      total += self.cesta[producto]*self.cartaRestaurante.sprecios[producto]
    print('Total: ',total, ' euros')

  def pagar():
    self.factura_pagada = True

