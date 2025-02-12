numero= int(input("Ingrese un número, para convertirlo en romano:"))
resultado = ""

if numero <=3:
    resultado=numero*"I"

if numero ==4:
    resultado="IV"

elif numero >=5 and numero <=8:
    resultado= "V" + (numero-5)*"I"

if numero ==9:
    resultado="IX"

if numero >=10:
    resultado= "X" + (numero-10)*"I"

if numero ==14:
        resultado="XIV"

if numero >=15:
     resultado= "XV" + (numero-15)*"I"

elif numero >=16:
     resultado= "XVI"
    
if numero ==19:
     resultado= "XIX"   

if numero >=20:
     resultado= "XX" + (numero-20)*"I"

if numero ==24:
     resultado= "XIV"

if numero >=25:
     resultado= "XV" + (numero-25)*"I"

if numero ==29:
     resultado= "XXIX"

if numero ==30:
     resultado=("XXX")
print(resultado)