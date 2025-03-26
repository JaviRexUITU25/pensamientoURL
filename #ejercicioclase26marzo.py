#ejercicio1
'''Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el 
esqueleto de abajo'''
'''for i in range (1,11):
    if i %2 != 0:
        print("Los numeros impares son: ", i)'''
        
'''Ejercicio 2
Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el 
esqueleto de abajo'''
'''x = 1
while x < 11:
    if x % 2 ==0:
        x += 1
        continue
    print(x)
    x += 1'''
'''Escenario 1
La instrucción break se implementa para salir/terminar un bucle.
Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese un
palabra a menos que ingrese "chupacabra" como la palabra de salida secreta, en cuyo caso el''' 
'''PalabraSecreta = "chupacabra"
while True:
    palabra = input("Ingrese la palabra secreta: ")
    if palabra == PalabraSecreta:
        break
print("palabra correcta!")'''