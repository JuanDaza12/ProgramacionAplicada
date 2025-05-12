from Calculator import Calculator  

class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()  

    def run(self):
        a = 10
        b = 0

        print("Suma:", self.calculator.add(a, b))
        print("Resta:", self.calculator.subtract(a, b))
        print("Multiplicación:", self.calculator.multiply(a, b))
        print("División:", self.calculator.divide(a, b))
        print("Módulo:", self.calculator.modulo(a, b))

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
