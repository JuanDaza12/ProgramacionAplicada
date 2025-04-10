import time

cadena = 'Programacion Aplicada'

for letra in cadena:
    if letra == 't':
        continue
    print(letra)
    time.sleep(0.5)
   