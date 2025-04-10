import csv
import random

# Lista de nombres de ejemplo
nombres = ["Ana", "Luis", "Carlos"]

# Crear y escribir el archivo CSV
with open("nombres_identificadores.csv", mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    
    # Escribir la cabecera
    escritor.writerow(["Nombre", "Identificador"])
    
    # Escribir cada nombre con un número aleatorio entre 0 y 1
    for nombre in nombres:
        identificador = round(random.random(), 6)  # 6 decimales para más precisión
        escritor.writerow([nombre, identificador])