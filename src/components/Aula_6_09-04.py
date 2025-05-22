# CÁLCULO DE IMC
'IMC = 80/1,80 x1,80 = 24,69 Kg/m2'

genero = (input("Qual é o seu gênero? "))
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura em centimetros: "))
largura = float(input("Digite a sua largura abdominal: "))

imc =( peso/(altura * altura))
print("{:.1f}".format(imc))

if imc < 18.5:
  print('Peso baixo')
  print('Risco de comorbidade baixo')
else:
  if 18.5 <= imc <= 24.9:
    print('Peso normal')
    print('Risco de comorbidade médio')
  else:
    if 25 <= imc <= 29.9:
        print('Sobrepeso')
        print('Risco de comorbidade aumentando')
    else:
      if 30 <= imc <= 34.9:
          print('Obesidade grau I')
          print('Risco de comorbidade moderado')
      else:
        if 35 <= imc <= 39.9:
            print('Obesidade grau II')
            print('Risco de comorbidade grave')
        else:
          if  imc >= 40:
              print('Obesidade grau III')
              print('Risco de comorbidade muito grave')
          else:
            print('ERRO')


if genero == "masculino":
    if largura > 102:
        print("Risco abdominal aumentado ")
    else:
        print("Risco abdominal normal ")
else:
    if largura > 88:
        print("Risco abdominal aumentado ")
    else:
        print("Risco abdominal normal ")



#////////////////////////////////////////////////////////////

import math

print("Escolha uma figura geométrica para calcular:")
print("1 - Quadrado")
print("2 - Retângulo")
print("3 - Triângulo")
print("4 - Círculo")
print("5 - Trapézio")
print("6 - Paralelogramo")
print("7 - Losango")
print("8 - Elipse")

escolha = input("Digite o número ou o nome da figura: ").lower()


if escolha == "1" or escolha == "quadrado":
  lado = float(input("Digite o lado do quadrado: "))
  area = lado ** 2
  print("A área do quadrado é:", area)
else:
  if escolha == "2" or escolha == "retangulo" or escolha == "retângulo":
    comprimento = float(input("Digite o comprimento: "))
    largura = float(input("Digite a largura: "))
    area = comprimento * largura
    print("A área do retângulo é:", area)
  else:
    if escolha == "3" or escolha == "triangulo" or escolha == "triângulo":
      base = float(input("Digite a base: "))
      altura = float(input("Digite a altura: "))
      area = (base * altura) / 2
      print("A área do triângulo é:", area)
    else:
      if escolha == "4" or escolha == "círculo" or escolha == "círculo":
        raio = float(input("digite o raio: "))
        area = raio **2
        print("a area do circulo é:",area)
      else:
       print("ERRO")

#////////////////////////////////////////////////////////////

nome = input("Digite um nome: ")
while nome != 'fim':
  nome = input("Insira um nome")

#////////////////////////////////////////////////////////////

numeros = 1

while (10 >= numeros):
  print(numeros)
  numeros=numeros + 1

#////////////////////////////////////////////////////////////

numero = int(input("Tabuada de: "))
x = 1

while( x <= 10):
   print(x * numero)
   x = x + 1

#////////////////////////////////////////////////////////////

numero = 1
soma = 0

while numero <= 10:
  x = int(input("Digite o $d nummero: " %numero))
  soma = soma + x
  numero = numero + 1
  print("soma: %d" %soma)

#////////////////////////////////////////////////////////////

tabuada = 1

while tabuada <= 10:
  numero = 1
  while numero <=10:
    print("%d X %d= %d" % (tabuada, numero, tabuada*numero))
    numero += 1

    print("====================")
    tabuada += 1

#////////////////////////////////////////////////////////////

import random

numero_aleatorio = random.randint(1, 100)
tentativa = int(input("Adivinhe o número entre 1 e 100: "))

while tentativa != numero_aleatorio:
  if tentativa < numero_aleatorio:
     print("Muito baixo !")
  else:
    print("muito alto !")
  tentativa = int(input("Tente novamente: "))

print(f"Parabens! Você adivinhou o número {numero_aleatorio}.")