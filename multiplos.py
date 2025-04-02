'''Ejercicio 1
Solicita al usuario el tamaño del arreglo (array) unidimensional e inicialízalo con dicho tamaño.
Pide al usuario un número base para generar los múltiplos.
Crea una función que rellene el arreglo con los primeros múltiplos del número ingresado por el 
usuario.
Por ejemplo, si el tamaño del arreglo es 6 y el número base es 8, el contenido del arreglo debe 
ser: [8, 16, 24, 32, 40, 48].'''
#numero = "6"
#m = "8"
#salida = ["8", "16", "24", "32", "40", "48"]#vector
#for i in range (0,9):
#    salida.append (i * m)
#print(salida)'''

#Ejercicio 2
'''Crea 2 vectores (Arrays unidimensionales) que tengan el mismo tamaño ingresado por el usuario, 
en uno de ellos almacenarás nombres de persona, en el otro vector va almacenando la longitud de 
los nombres.'''

'''nombres = ("Mario", "Luis")
nombres = []
longitudes = []
for i in range (nombres):
        nombre = input(f"Ingrese el nombre {i + 1}:")
longitudes.append(nombres)
longitudes.append(len(nombre))
while True:
        tamaño = int(input("Ingrese el tamaño del arreglo: "))
        if tamaño > 0:
             break
        else:
             print("ingrese un numero positivo")
print("Lista de nombres: ", nombres)
print("Longitud de los nombres: ", longitudes)'''








'''Escenario 1
En el restaurante de la universidad, el cliente luego de ser atendido evalúa la atención recibida 
presionando un botón entre las 5 opciones mostradas.
Opciones:
5. Excelente
4. Muy Buena
3. Buena
2. Regular
1. Malo
Realice un algoritmo que registre en un arreglo la evaluación para n clientes atendidos, luego 
deberá tabular las respuestas para mostrar:
a) Total de respuestas por tipo
b) La respuesta más frecuente
c) ¿Cuáles clientes respondieron con valores menores al promedio?
entrada
Ejemplo: n=15
proceso
Cliente 1 2 3 4 5 … n
Atención 5 2 4 5 3 … 4
Salida
Respuestas
a) Excelente: 10
Muy Buena: 20
Buena: 15
Regular: 3
Malo: 2
b) Más frecuente: 4
c) Promedio: 3.66
Porcentaje menor al promedio.:
15%'''
n = int(input("Ingrese el numero de clientes encuestados : "))
answer = []
print("Ingrese las evaluaciones(1= Malo, 2=regular, 3=buena, 4=muy buena, 5=excelente): ")
for i in range(n):
    while True:
        valor = int(input("Cliente: "))
        if valor >=1 and valor >=5:
            answer.append(valor)
            break
        else: 
            print("Ingrese unicamente entre el 1 y el 5.")
conteo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for r in answer:
    conteo[r] +=1
print("Resultados")
print("TOTAL DE RESPUESTAS: ")
print("Excelente (5): ", conteo[5])
print("Muy bueno (4): ", conteo[4])
print("Bueno (3): ", conteo[3])
print("Regular (2): ", conteo[2])
print("Malo (1): ", conteo[1])

masfrecuente = max(conteo, key = conteo.get)





