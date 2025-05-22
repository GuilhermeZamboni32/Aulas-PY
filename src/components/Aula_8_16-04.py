#/////////////////////////////////////////////////////////////

gastos = 0
valor_gasto = 0
while gastos < 1000:
    valor_gasto = int(input("Digite o valor do novo gasto"))
    gastos = gastos + valor_gasto
print(gastos)

#/////////////////////////////////////////////////////////////

login = input("Login: ")
senha = input("Senha: ")
while login == senha:
    print("Sua senha deve ser diferente do login: ")
    senha = input("Senha: ")
print("Cadastro aprovado")

#/////////////////////////////////////////////////////////////

for i in [1, 2, 3, 4]:
  print(i, end=", ")

#/////////////////////////////////////////////////////////////

for i in [1, 3, 5, 7, 9]:
  x = i**2 - (i-1)*(i+1)
print(x, end=", ")

#/////////////////////////////////////////////////////////////

for i in range(5):
  print(i, end=", ")

#/////////////////////////////////////////////////////////////

lojas = ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Curitiba', 'Florianópolis']
for loja in lojas:
  print(loja, end=" ")
print()
print("Acabou o FOR")

#/////////////////////////////////////////////////////////////

l = ['hello', 'world', 'hi', 'earth']
for word in l:
 print (word )

#/////////////////////////////////////////////////////////////

lojas=['Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Curitiba', 'Florianópolis']
for i,loja in enumerate (lojas):
 print("A loja ",i+1, "está em ", loja)
print("Acabou o FOR")

#/////////////////////////////////////////////////////////////

lojas=['Rio de Janeiro','São Paulo','Belo Horizonte','Curitiba','Florianópolis']
for i,loja in enumerate(lojas, 1):
  print("A loja ",i,"está em ",loja)
print("Acabou o FOR")

#/////////////////////////////////////////////////////////////

tarefas = ['Reunião com equipe', 'Responder e-mails', 'Gerar relatórios', 'Atualizar planilhas']
#O número 1 indica que queremos começar a contagem a partir de 1 (em vez do padrão que é 0).
for i, tarefa in enumerate(tarefas, 1):
  print(f"{i}. {tarefa}")

#/////////////////////////////////////////////////////////////

language = 'Python'
match language: # a variável que iremos avaliar
  case 'R': # caso a variável tenha esse valor executa o código abaixo
    print('You are using R')
  case 'Julia':
    print('You are using Julia')
  case 'Python':
    print('Yes, you are using Python ')

#/////////////////////////////////////////////////////////////

dia=int(input("Digite o dia da semana (1 - 7) : "))
if dia ==1:
  print ("Domingo")
elif dia ==2:
  print ("Segunda")
elif dia ==3:
  print ("Terça")
elif dia ==4:
  print ("Quarta")
elif dia ==5:
  print ("Quinta")
elif dia==6:
  print("Sexta")
elif dia==7:
  print("Sábado")
else:
  print("Valor inválido")

#/////////////////////////////////////////////////////////////

dia=input("Digite o dia da semana (Segunda, Terça, Quarta, Quinta, Sexta, Sábado, Domingo) : ")
match dia:
  case 'Domingo' | 'Sábado':
    print("Final de Semana")
  case _:
    print("Dia útil")

#/////////////////////////////////////////////////////////////

for i in range(1,10):
  print(i)
else:
  print("fim do loop")

#/////////////////////////////////////////////////////////////

for i in range(0,10):
  print(i+1)
else:
  print("fim do loop")

#/////////////////////////////////////////////////////////////

estoque = ['mouse', 'teclado', 'monitor', 'webcam']
busca = input("Digite o produto desejado: ")
for item in estoque:
  if item == busca:
    print(" Produto disponível em estoque.")
    break
else:
  print(" Produto não encontrado. Favor solicitar ao fornecedor.")

#/////////////////////////////////////////////////////////////

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

print(RED + "ERROR!" + RESET + "Algo de errado ocorreu...")

#Características e Funcionalidades

#Cores e Estilos

#Fore: Para definir cores de primeiro plano (texto).
#Back: Para definir cores de fundo.
#Style: Para aplicar estilos como brilho, atenuação (DIM), etc.

#/////////////////////////////////////////////////////////////

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.CYAN + 'and with a green background')
print(Style.DIM + 'and in dim text') #aparecerá menos brilhante em comparação com o outro texto em verde
print(Style.RESET_ALL)
print(Fore.GREEN +'back to normal now')

#/////////////////////////////////////////////////////////////

nomes=[]
notas=[7, 6, 10]
print(notas[0], notas[1], notas[2])
print((notas[0] + notas[1] + notas[2])/3)

notas2=[6, 5, 9]
somalista=notas+notas2
print(somalista)

#/////////////////////////////////////////////////////////////

produtos = ['tv','celulart','tablet','mouse','teclado','geladira','forno',]
print(produtos)
produtos.append('ipad')
print(produtos)

#/////////////////////////////////////////////////////////////

produtos = ['tv','celulart','tablet','mouse','teclado','geladira','forno',]
print(produtos)
produtos.remove('forno')
print(produtos)

#/////////////////////////////////////////////////////////////

produtos = ['tv','celulart','tablet','mouse','teclado','geladira','forno',]
print(produtos)
aux = produtos.pop(2)
print(produtos)
print(aux)

#/////////////////////////////////////////////////////////////

produtos = ['tv','celulart','tablet','mouse','teclado','geladira','forno',]
print(produtos)

aux = produtos.append('ipad')
print(produtos)

produtos.remove('ipad')
print(produtos)

aux = produtos.pop(2)
print(produtos)
print(aux)




