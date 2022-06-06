cont = 0
for aumento in range(4):
    cad1 = input("Ingrese cadena :")
    for letra in cad1:
     if letra in "a e i o u":
        cont += 1
print("el total de vocales es: ", cont)
