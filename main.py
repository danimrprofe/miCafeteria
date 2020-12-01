import os
from comanda import *
from funciones import *
from carta import *

print('Bienvenido a mi cafetería\n\n')

clienteFinalizado = False

carta = Carta()
comanda = Comanda(1, carta)

while not clienteFinalizado:  

  print('¿Qué desea?:\n')

  print('[0] Mostrar la carta')
  print('[1] Realizar un pedido')
  print('[2] Mostrar mi comanda')
  print('[3] Pedir factura')
  print('[4] Pagar')
  print('[5] Irme a mi casa')
  
  
  accion = int(input('\n Enter para volver al menu\n'))

  _ = os.system('cls')


  if (accion == 0):
    carta.mostrarCarta()
  elif (accion == 1):
    carta.mostrarCarta()
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

