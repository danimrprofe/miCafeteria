import os
import comanda import *
from funciones import *

print('Bienvenido a mi cafetería\n\n')

clienteFinalizado = False

comanda = Comanda()

while not clienteFinalizado:  

  print('¿Qué desea?:\n')

  print('[0] Mostrar la carta')
  print('[1] Realizar un pedido')
  print('[2] Mostrar mi comanda')
  print('[3] Pedir factura')
  print('[4] Pagar')
  print('[5] Irme a mi casa')
  
  
  accion = int(input())

  _ = os.system('clear')

  if (accion == 0):
    mostrarCarta()
  elif (accion == 1):
    mostrarCarta()
    comanda.realizarPedido()
  elif (accion == 2):
    comanda.imprimir()
  elif (accion == 3):
    comanda.factura()
  elif (accion == 4):
    comanda.pagar()
  elif (accion == 5):
    print('adios')
    clienteFinalizado = True

