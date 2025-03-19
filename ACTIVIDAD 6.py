saldo = 3000
numeroIntentos = 3

while numeroIntentos > 0:
    print(f"Tu saldo actual es de Q{saldo}.")
    retiro = int(input("Ingrese monto a retirar: "))
    resultado = saldo - retiro
    if resultado < 0:
        print(f"Saldo insuficiente. Ingrese de nuevo, el numero de intentos es: {numeroIntentos}")
    elif resultado == 0:
        print(f"Retiro exitoso. Nuevo saldo: Q{resultado}")
        print("Retiro exitoso. Saldo agotado. Adiós.")
        break
    else:
        print(f"Retiro exitoso. Nuevo saldo: Q{resultado}")
        numeroIntentos -= 1
        saldo = resultado