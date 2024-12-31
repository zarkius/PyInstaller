class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

    def multiplicacion(self):
        return self.a * self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: División por cero"

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
calculadora = Calculadora(a, b)

print("Suma:", calculadora.suma())
print("Resta:", calculadora.resta())
print("Multiplicación:", calculadora.multiplicacion())
print("División:", calculadora.division())
