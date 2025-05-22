from datetime import date
hj = date.today()
print('A data de hoje é;', hj)

#/////////////////////////////////////////////////////////////

from datetime import date

Data_Atual = date.today()
print('A data atual é;', Data_Atual)

Data_em_texto = ("A data atual fomatada é: {}/{}/{}".format(Data_Atual.day, Data_Atual.month, Data_Atual.year))
print(Data_em_texto)

#/////////////////////////////////////////////////////////////

from datetime import date

Data_Atual = date.today()
print('A data atual é;', Data_Atual)

Data_em_texto = ("A data atual fomatada é: {}/{}/{}".format(Data_Atual.day, Data_Atual.month, Data_Atual.year))
print(Data_em_texto)

Data_em_texto = Data_Atual.strftime("A data atual formatada é: %d/%m/%y")
print(Data_em_texto)

#/////////////////////////////////////////////////////////////

from datetime import datetime
from pytz import timezone

data_e_hora_atual = datetime.now()
fuso_horario = timezone("America/Sao_Paulo")
data_e_hora_sao_paulo = data_e_hora_atual.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

print(data_e_hora_sao_paulo_em_texto)

#/////////////////////////////////////////////////////////////

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
  print("O primeiro número é maior")
else:
  if num1 == num2:
    print("Os números são igual ")
  else:
   print("O segundo número é maior")

#/////////////////////////////////////////////////////////////

rg = input("Entre com o RG de um aluno: ")

if rg == "155446":
  print("Guilherme Zamboni")
elif rg == "192804":
  print("Alexsandro Alexandrino")
elif rg == "209823":
  print("Ana paula Dantas")
elif rg == "188948":
  print("Klairton brito")

# . . .
elif rg == "9999999":
  print("...")
else:
  print("aaaaaaaa")

#/////////////////////////////////////////////////////////////

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if (num1 <= num2) and (num1 <= num3):
 print(num1)
if (num2 <= num1) and (num2 <= num3):
  print(num2)
if (num3 <= num1) and (num3 <= num3):
  print(num3)