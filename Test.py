Nombre = str(input("Indique su nombre y apellido: "))
HorasT = int(input("Indique las horas trabajadas: "))
SueldoB = HorasT * 9500
print("1. Isapre");print("2. Fonasa")
IsOrFon = int(input("Seleccione un numero"))

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
else:
    SueldoB = SueldoB * 0.93
