# vai dar (ZeroDivisionError)
x=12
y=0
z=x/y

#/////////////////////////////////////////////////////////////

# Agora não vai dar (ZeroDivisionError)

x=12
y=0
try:
  z=x/y
except ZeroDivisionError:
  print("Não é possível dividir por zero meu CUUUmpadre")

#/////////////////////////////////////////////////////////////

def ler_int(mesegem, mesegem_de_erro):
  while True:
    try:
      entrada=int(input(mesegem))
      return entrada
    except ValueError:
      print(mesegem_de_erro)

#===================================

MSG = 'Digite um número inteiro: '
MSG_ERRO = "Número invalido !!!"
x = ler_int(MSG, MSG_ERRO)
y = ler_int(MSG, MSG_ERRO)
print(x+y)

#/////////////////////////////////////////////////////////////

print("Vamos dividir dois número inseridos por você\n")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = int(num1) / int(num2)
print("O resultado é " + str(resultado))

#/////////////////////////////////////////////////////////////

print("Vamos dividir dois número inseridos por você\n")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

try:
  resultado = int(num1) / int(num2)
  print("O resultado é " + str(resultado))
except ZeroDivisionError:
  print("Não é possível dividir por zero")


#/////////////////////////////////////////////////////////////

print("Vamos dividir dois número inseridos por você\n")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

try:
  resultado = int(num1) / int(num2)
  print("O resultado é " + str(resultado))
except ZeroDivisionError:
  print("Não é possível dividir por zero")

#/////////////////////////////////////////////////////////////

print("Vamos dividir dois número inseridos por você\n")
num1 = (input("Digite o primeiro número: "))
num2 = (input("Digite o segundo número: "))

try:
  resultado = int(num1) / int(num2)
  print("O resultado é " + str(resultado))

except ZeroDivisionError:
  print("Não é possível dividir por zero")

except ValueError:
  print("Você não digitou um número")

except Exception as erro:
  print("Erro desconhecido")
  print(erro)

#/////////////////////////////////////////////////////////////

# Erro personalizado ||  ValueError: Erro de entrada: A idade deve ser um número positivo.

try:
  idade = int(input("Digite sua idade: "))
  if (idade <= 0) or (idade>= 110):
    raise ValueError("A idade deve ser um número positivo.")
except ValueError as erro:
  raise ValueError(f"Erro de entrada: {erro}")

