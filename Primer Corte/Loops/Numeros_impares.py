try:
    times = int(input("Ingrese el número de veces que desea analizar: "))
    
    if times <= 0:
        print("Debe ingresar un número entero mayor a 0.")
    else:
        for i in range(1, times + 1):
            if i % 2 == 0:
                print("El número", i, "no es impar")
            else:
                print("El número", i, "es impar")
        print("Último valor de i =", i)

except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")