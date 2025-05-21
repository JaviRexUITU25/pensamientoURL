# Matriz inicial
matriz = [
    [0,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
]

def imprimir_tablero(matriz):
    for fila in matriz:
        print(' '.join(str(c) for c in fila))
    print()

def contar_vecinos_vivos(matriz, fila, col):
    vecinos = 0
    filas = len(matriz)
    columnas = len(matriz[0])
    pass
    if col > 0:
        vecinos += matriz[fila][col - 1]
    if col < columnas - 1:
        vecinos += matriz[fila][col + 1]
    
    return vecinos

def siguiente_generacion(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    nueva_matriz = [[0]*columnas for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos_vivos(matriz, i, j)
            if matriz[i][j] == 1:
                pass
                if vecinos == 1 or vecinos == 2:
                    nueva_matriz[i][j] = 1
                else:
                    nueva_matriz[i][j] = 0
            else:
                if vecinos == 1:
                    nueva_matriz[i][j] = 1
                else:
                    nueva_matriz[i][j] = 0
    return nueva_matriz
pass
print("Generación 0:")
imprimir_tablero(matriz)

generacion_1 = siguiente_generacion(matriz)
print("Generación 1:")
imprimir_tablero(generacion_1)

generacion_2 = siguiente_generacion(generacion_1)
print("Generación 2:")
imprimir_tablero(generacion_2)
