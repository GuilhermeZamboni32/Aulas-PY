#/////////////////////////////////////////////////////////////

#código base
nome1 = input("Digite o nome do primeiro aluno: ")
nome2 = input("Digite o nome do segundo aluno: ")
nome3 = input("Digite o nome do terceiro aluno: ")

nota1 = float(input('Informe a nota de ' + nome1 + ': '))
nota2 = float(input('Informe a nota de ' + nome2 + ': '))
nota3 = float(input('Informe a nota de ' + nome3 + ': '))

media = (nota1 + nota2 + nota3) / 3
print("A média da turma é: ", media)

if nota1 > media:
  print('Parabéns ' + nome1 + ' Você está acima da média')
if nota2 > media:
  print('Parabéns ' + nome2 + ' Você está acima da média')
if nota3 > media:
  print('Parabéns ' + nome3 + ' Você está acima da média')


#/////////////////////////////////////////////////////////////

#código aprimorado
nomes=[]
notas=[]

while True:
  nome = input("Informe o nome do aluno: ")

  nota = float(input(f'Informe a nota de {nome} : '))

  nomes.append(nome)
  notas.append(nota)

if len(notas) == 0:
  print("Nenhuma nota foi adicionada")

else:
    soma = 0
    for nota in notas:
      soma += nota
    media = soma / len(notas)
    print("\n A média da turma foi: ", media)

    for i in range(len(notas)):
      if notas[i] > media:
        print('Parabéns ' + nomes[i] + ' Você está acima da média')

#/////////////////////////////////////////////////////////////

alunos_idade=[]

for i in range(5):
  linha=[]
  linha.append(input('Digite o nome do aluno: ' + str(i) + ':'))
  linha.append(int(input('Digite a idade do aluno: ' + linha[0] + ':')))
  alunos_idade.append(linha)

#print(alunos_idade)

menor = alunos_idade[0][1]
pos = 0

for i in range(5):
  if alunos_idade[i][1] < menor:
    menor = alunos_idade[i][1]
    pos = i

for i in range(5):
  print(alunos_idade[i])
print('A pessoa mais nova é ', alunos_idade[pos][0])

#/////////////////////////////////////////////////////////////

a=(3, 'maio', 9.5, 'fabio')
print(a[2])

print(a[1:3])

#/////////////////////////////////////////////////////////////

tupla=('a','b','c')
tupla[0]="a"

#/////////////////////////////////////////////////////////////

###################################################
#    Cadastro de Itens em uma Lista
###################################################

#criar um programa simples que cadastra nomes de frutas informadas pelo usuário.

#Objetivo do exercício
#Praticar os seguintes conceitos de forma isolada e didática:

#Uso do laço while
#Condicionais com if e else
#Armazenamento de dados em lista
#Validação de entrada (não aceitar strings vazias)
#Encerramento do loop com uma palavra-chave



###################################################
#O que o programa deve fazer:

#Criar uma lista vazia chamada frutas.
#Pedir ao usuário para digitar nomes de frutas até que ele digite "sair".
#Se o nome digitado for vazio (""), mostrar a mensagem: " Nome inválido. Tente novamente."
#Se o nome for válido, adicionar à lista.
#Ao final, exibir todas as frutas cadastradas.


###################################################

frutas = []
print('Você foi ao mercado para fazer a conpra das frutas da semana,porque você é uma pessoa saúdavel kkkk.\nColoque no seu carrinho de compras ,quantas frutas você quiser\n')

while True:
    fruta = input("Digite o nome de uma fruta para colocar no seu carrinho: ")
    fruta = fruta.strip()
    print("Digite 'sair' para encerrar as suas compras\n")

    if fruta == "sair":
        break
    else:
      if fruta == "":
        print("Nome inválido. Tente novamente.")
      else:
        frutas.append(fruta)

print(f'Vocêc colocou as frutas {frutas} no seu carrinho de compras. ')

