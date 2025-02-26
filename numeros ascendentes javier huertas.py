digitos = int(input("Ingrese el numero que desea ordenar: "))

if digitos <10000 or digitos >99999:
    print("El digito no es aceptado")
else: 
    digito1 = digitos // 10000
    digito2 = (digitos // 1000)%10  
    digito3 = (digitos // 1000)%10
    digito4 = (digitos // 1000)%10  
    digito5 = digitos %10

    if digito1 > digito2:
        digito1, digito2 = digito2, digito1
    if digito1 > digito3:
        digito1, digito3 = digito3, digito1
    if digito1 > digito4:
        digito1, digito4 = digito4, digito1
    if digito2 > digito3:
        digito2, digito3 = digito3, digito2
    if digito2 > digito4:
        digito2, digito4 = digito4, digito2
    if digito3 > digito4:
        digito3, digito4 = digito4, digito3
    forma_ascendente = digito1 * 10000 + digito2 * 1000 + digito3* 100 + digito4 * 10 + digito5
    forma_descendente = digito5 * 10000 + digito4 *1000 + digito3 * 100 + digito2 * 10 + digito1
    print("Forma ascendente de ", digitos, "es:" , forma_ascendente)
    print("Forma descendente de ", digitos, "es:" , forma_descendente)