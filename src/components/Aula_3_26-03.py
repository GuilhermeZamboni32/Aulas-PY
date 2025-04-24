#Exercício 11: Crie uma variável chamada “temperatura” e atribua a ela a temperatura atual em graus Celsius

'''temperatura = float(input("Qual é a temperatura atual em graus Celsius? "))
print("A temperatura atual é:", temperatura, "°C")'''



'''Outra forma mais elaborada com (if, else)'''
temperatura = float(input("Qual é a temperatura atual em graus Celsius? "))

if  0 <= temperatura <= 9:
    print("Hoje tá frio em kkk.")
elif 10 < temperatura <= 20:
    print("Tá fresquinho, do jeito que eu gosto .")
elif 21 <= temperatura <= 30:
    print("Hoje a temperatura está normal.")
elif 31 <= temperatura <=100:
    print("Tragão os ovos que eu vou fritár eles no asfalto.")
else:
    print("Meu deus kkkk.")




numero1 = int(input("digite um numero"))
numero2 = int(input("digite outro numero"))

if numero1 > numero2:
    print("o primeiro numero é o maior")
if numero1 < numero2:
    print("o segundo numero é o maior")