Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.

number1 = int(input("First number"))
number2 = int(input("Second number"))
if number2 == 0:
  print("Error, divisor is 0")
else:
  total = number1/number2
  print(total)
