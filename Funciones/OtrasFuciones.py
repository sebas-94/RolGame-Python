import os
import sys
import time


def escritura(mensaje, limpiar=False, tiempo=0.05):
    if limpiar:
        os.system('clear')

    for char in mensaje:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != ".":
            time.sleep(tiempo)
        else:
            time.sleep(1)

    sys.stdout.write('\n')

    if limpiar:
        time.sleep(1)
        os.system('clear')


def cabeceraMenu(nombre):
    os.system('clear')
    print('{:*^50}'.format('*'))
    print('{:*^50}'.format('  ' + nombre + '  '))
    print('{:*^50}'.format('*'))
    print()
