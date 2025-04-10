a = 1

while a == 1:
    valor = input('Ingrese un número hasta el cual desea verificar los primos: ')
    
    try:
        valor = int(valor)
        
        for i in range(1, valor + 1):
            contador = 0
            for n in range(1, i + 1):
                residuo = i % n
                if residuo == 0:
                    contador += 1

            if contador == 2:
                print(f'{i} es un número primo\n')
            else:
                print(f'{i} NO es un número primo\n')

        # Preguntar si desea continuar
        continuar = input('¿Desea continuar? Presione 1 para continuar o cualquier otra tecla para salir: ')
        if continuar != '1':
            print("Programa finalizado.")
            break

    except ValueError:
        print("Por favor, ingrese un número válido.")