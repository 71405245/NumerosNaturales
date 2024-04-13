class CalculadoraMCD:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def gcd(self):
        """
        Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.

        Returns:
        int: El máximo común divisor de self.num1 y self.num2.
        """
        a, b = self.num1, self.num2
        while b != 0:
            a, b = b, a % b
        return a

# Ejemplo de uso
num1 = 48
num2 = 18

calculadora = CalculadoraMCD(num1, num2)
print(f"El máximo común divisor de {num1} y {num2} es: {calculadora.gcd()}")
k