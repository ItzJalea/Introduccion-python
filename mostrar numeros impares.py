

num2=0
numero = int(input("Digite un numero: "))
while numero <0:
  numero = int(input("Digite un numero positivo: "))
while num2 < numero:
  num2= num2+1
  if num2%2:
    print(num2,end=",")
