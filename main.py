import os
from funciones import *

print('Bienvenido a mi cafetería\n\n')

clienteFinalizado = False

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
    realizarPedido()
  elif (accion == 2):
    pintar_comanda()
  elif (accion == 3):
    factura()
  elif (accion == 4):
    print('pagar')
  elif (accion == 5):
    print('adios')
    clienteFinalizado = True

