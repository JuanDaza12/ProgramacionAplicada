class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("No se puede dividir entre cero.")
            return float('nan')
        return a / b

    def modulo(self, a, b):
        if b == 0:
            print("No se puede obtener módulo con divisor cero.")
            return 0
        return a % b

def main():
    my_calculator = Calculator()

    # Definimos a y b al inicio
    a = 10
    b = 2

    print("Suma:", my_calculator.add(a, b))
    print("Resta:", my_calculator.substract(a, b))
    print("Multiplicación:", my_calculator.multiply(a, b))

    resultado_division = my_calculator.divide(a, b)
    if str(resultado_division) == 'nan':
        print("Resultado: matemáticamente incorrecto")
    else:
        print("División:", resultado_division)

    resultado_modulo = my_calculator.modulo(a, b)
    if b == 0:
        print("Resultado: matemáticamente incorrecto")
    else:
        print("Módulo:", resultado_modulo)

if __name__ == "__main__":
    main()
