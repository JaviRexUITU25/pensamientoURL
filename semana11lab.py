from abc import ABC, abstractmethod
import math
class CaidaLibre(ABC):
    def __init__(self, altura, gravedad):
        self.altura = altura
        self.gravedad = gravedad

    @abstractmethod
    def realizar_experimento(self):
        pass
class CaidaLibreExperimento(CaidaLibre):
    def realizar_experimento(self):
        if self.altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        if self.gravedad <= 0:
            raise ValueError("La gravedad no puede ser cero o negativa.")
        tiempo_caida = math.sqrt(2 * self.altura / self.gravedad)
        return tiempo_caida
altura = 10
gravedad = 9.81
experimento = CaidaLibreExperimento(altura, gravedad)
try:
    tiempo = experimento.realizar_experimento()
    print(f"El tiempo de caída es: {tiempo:.2f} segundos")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
# Fin del programa
import math
class OperacionCientifica:
    def calcular(self):
        pass
class RaizCuadrada(OperacionCientifica):
    def calcular(self, numero):
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(numero)
class Potencia(OperacionCientifica):
    def calcular(self, base, exponente):
        return base ** exponente
class Logaritmo(OperacionCientifica):
    def calcular(self, numero, base=math.e):
        if numero <= 0:
            raise ValueError("No se puede calcular el logaritmo de un número no positivo.")
        return math.log(numero, base)
class Factorial(OperacionCientifica):
    def calcular(self, numero):
        if numero < 0 or not isinstance(numero, int):
            raise ValueError("El factorial solo está definido para números enteros no negativos.")
        return math.factorial(numero)
raiz = RaizCuadrada()
potencia = Potencia()
logaritmo = Logaritmo()
factorial = Factorial()
try:
    print(f"Raíz cuadrada de 16: {raiz.calcular(16)}")
    print(f"2 elevado a la 3: {potencia.calcular(2, 3)}")
    print(f"Logaritmo natural de 10: {logaritmo.calcular(10)}")
    print(f"Factorial de 5: {factorial.calcular(5)}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
# Fin del programa
