# Ejercicio 9: Imprimir los números primos entre 0 y 30
print("== PRIMOS DEL 0 AL 30 (sin optimizar) ==")
tope_rango = 30

for n in range(tope_rango):
    if n < 2:
        continue  # Los números menores que 2 no son primos
    primo = True
    for div in range(2, n):
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n, end=" ")
print("\n")

# Ejercicio 10: Optimización con break
print("== PRIMOS DEL 0 AL 30 (con break) ==")
for n in range(tope_rango):
    if n < 2:
        continue
    primo = True
    for div in range(2, n):
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n, end=" ")
print("\n")

# Ejercicio 11: Medición de ciclos con y sin optimización
print("== MEDICIÓN DE CICLOS ==")
ciclos_sin_break = 0
ciclos_con_break = 0

# Sin break
for n in range(tope_rango):
    if n < 2:
        continue
    primo = True
    for div in range(2, n):
        ciclos_sin_break += 1
        if n % div == 0:
            primo = False
    # No se imprimen los primos aquí porque no es necesario

# Con break
for n in range(tope_rango):
    if n < 2:
        continue
    primo = True
    for div in range(2, n):
        ciclos_con_break += 1
        if n % div == 0:
            primo = False
            break

print(f"Ciclos SIN break: {ciclos_sin_break}")
print(f"Ciclos CON break: {ciclos_con_break}")
eficiencia = (ciclos_con_break / ciclos_sin_break) * 100
print(f"Optimización: {eficiencia:.2f}% de los ciclos usados con break\n")

# Ejercicio 12: Evaluar con un rango mayor
print("== MEDICIÓN DE CICLOS CON TOPE 100 ==")
tope_rango = 100
ciclos_sin_break = 0
ciclos_con_break = 0

# Sin break
for n in range(tope_rango):
    if n < 2:
        continue
    primo = True
    for div in range(2, n):
        ciclos_sin_break += 1
        if n % div == 0:
            primo = False

# Con break
for n in range(tope_rango):
    if n < 2:
        continue
    primo = True
    for div in range(2, n):
        ciclos_con_break += 1
        if n % div == 0:
            primo = False
            break

print(f"Ciclos SIN break (tope 100): {ciclos_sin_break}")
print(f"Ciclos CON break (tope 100): {ciclos_con_break}")
eficiencia = (ciclos_con_break / ciclos_sin_break) * 100
print(f"Optimización al usar break: {eficiencia:.2f}% de los ciclos\n")