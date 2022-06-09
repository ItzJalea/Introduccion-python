Nombre = str(input("Indique su nombre y apellido: "))
HorasT = int(input("Indique las horas trabajadas: "))
SueldoB = HorasT * 9500
SueldoIn = SueldoB
print("1. Isapre");print("2. Fonasa")
IsOrFon = int(input("Seleccione un numero: "))
if IsOrFon == 1:
    print("1. Mas vida");print("2. Consalud");print("3. Colmena");print("4. Banmedica");print("5. Cruz Blanca");print("6. Vida Tres")
    NumIs = int(input("Seleccione Su Isapre:"))
    if NumIs == 1:
        DesIsapre = 32500 * 2
        SueldoB= SueldoB - DesIsapre
        Isapre = "Mas vida"
    elif NumIs == 2:
        DesIsapre = 32500 * 2
        SueldoB= SueldoB - DesIsapre
        Isapre = "Consalud"
    elif NumIs == 3:
        DesIsapre = 32500 * 2.11
        SueldoB= SueldoB - DesIsapre
        Isapre = "Colmena"
    elif NumIs == 4:
        DesIsapre = 32500 * 2.34
        SueldoB= SueldoB - DesIsapre
        Isapre = "Banmedica"
    elif NumIs == 5:
        DesIsapre = 32500 * 2.76
        SueldoB= SueldoB - DesIsapre
        Isapre = "Cruz Blanca"
    elif NumIs == 6:
        DesIsapre = 32500 * 2.78
        SueldoB= SueldoB - DesIsapre
        Isapre = "Vida Tres"
elif IsOrFon == 2:
    fonasa = SueldoIn * (7 / 100)
    SueldoB -= fonasa

else:
    print("Inicie de nuevo el programa")

desAFP = SueldoIn * 0.12
SueldoB -= desAFP
DesAFC = SueldoIn * (3 / 100)
SueldoB -= DesAFC
print("El Sueldo del Sr/a",Nombre," Es:")
print("Sueldo Bruto es: ",SueldoIn)
print("Su Sueldo es: ", SueldoB)
print("Descuento afp: ", desAFP)
print("Descuento afc: ", DesAFC)
if IsOrFon == 1:
    print("El descuento de isapre es: ",DesIsapre)
else:
    print("El descuento de fonasa es:",fonasa )
