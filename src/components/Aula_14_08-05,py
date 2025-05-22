#/////////////////////////////////////////////////////////////

from pickle import TRUE
#=================================================#
#     sistema de cadastro de nomes de alunos
#=================================================#


resposta_inicial = print('''
==============================================
  bem vindo ao sistema de cadastro de alunos
==============================================

  Digite 1 para começar o cadastro.
  Digite 0 para sair do sistema.

==============================================
''')

nomes=[]
if resposta_inicial == 1:

  while True:
    nomes = print('digite o nome de um aluno: ')
    #nome = nome.strip()
    print(nomes)

    if nome == "":
      print("Nome inválido. Tente novamente.")
    else:
      nome.append(nome)

  print(f'blablabla {nomes} blablabla ')

else:
  resposta_inicial == 0:


#/////////////////////////////////////////////////////////////

#=================================================#
#     sistema de cadastro de nomes de alunos
#=================================================#
'''
1)
1 inicia o cadastro
0 sair sistema , 0 encerrar imediatamente.

2)
se digitado 1 inicia o processo de cadastro
exibir mansegam (digite o nome de um aluno ou sair para encerar o progama)
utilize while para permitir varios cadastros

3)
digitar 'sair' o progama encerar o cadastro e exibe um relatorio
nome vazio da mensegem de erro
se o nome já estiver cadastrado recusar duplicidade
se for um nome valido solicite confirmação(Sim/Não) antes de cadastrar
se confirmar com 'sim' adicione a lista e informe suseso
se responde com 'não' exibar o cadastro foi cancelado
se for resposta invalida regeite o cadastro

4)ao final ,exibir um relatorio com formação estilizada contendo
1-lista dos nomes cadastrados
2-quantidade de nomes validos
3-quantidade de cadastros rejeitados'''


################################################################################

resposta_inicial = input('''
==============================================
  bem vindo ao sistema de cadastro de alunos
==============================================

  Digite 1 para começar o cadastro.
  Digite 0 para sair do sistema.

==============================================



''')


nomes=[]

while True:
  try:
    if resposta_inicial == '0': #encerar o progama.
      print('Sistema de cadastro encerrado.')
      break
    else:
      nome = input("digite o nome de um aluno ou 'sair' para encerar o cadastro. ") #informa nome.
      nome = nome.strip()#não deixa o nome ser vazio.

      if nome == 'sair': #encerar o progama.
        print('Sistema de cadastro encerrado.')
        break

      if nome == "": #verifica se o nome é valido ou invalido.
        print('nome invalido.')
      else:
        if nome in nomes:  #verifica se o nome já foi cadastrado.
           print('Este nome já exite tem outro.')
           continue
        else:
          confirmar = input(f"Confirma com (Sim/Não) se {nome} foi o que você digitou.")

        if confirmar == 'sim': #confirma o cadastro
          print(f'O nome {nome} foi ca]dastrado com sucesso')
          nomes.append(nome)

        else:
          if  confirmar == 'nao': #recusa o cadastro
              print('O cadastro foi canselado.')
              nomes.append(nome)



  except:
   print('Erro Toallll')


print(f'''


########################################################
#                 Nomes Cadastrados                    #
########################################################

  {nomes}




########################################################
''')





#/////////////////////////////////////////////////////////////

#=================================================#
#     sistema de cadastro de nomes de alunos      #
#=================================================#

'''
1)
1 inicia o cadastro
0 sair sistema , 0 encerrar imediatamente.

2)
se digitado 1 inicia o processo de cadastro
exibir mensagem (digite o nome de um aluno ou sair para encerrar o programa)
utilize while para permitir vários cadastros

3)
digitar 'sair' o programa encerra o cadastro e exibe um relatório
nome vazio dá mensagem de erro
se o nome já estiver cadastrado recusar duplicidade
se for um nome válido, solicite confirmação (Sim/Não) antes de cadastrar
se confirmar com 'sim' adicione à lista e informe sucesso
se responder com 'não' exibir que o cadastro foi cancelado
se for resposta inválida rejeite o cadastro

4)
ao final, exibir um relatório com formatação estilizada contendo:
1 - lista dos nomes cadastrados
2 - quantidade de nomes válidos
3 - quantidade de cadastros rejeitados
'''

################################################################################

resposta_inicial = input('''
==============================================
  Bem-vindo ao sistema de cadastro de alunos
==============================================

  Digite 1 para começar o cadastro.
  Digite 0 para sair do sistema.

==============================================

''')

nomes = []
rejeitados = 0

if resposta_inicial == '0':
    print('Sistema de cadastro encerrado.')

if resposta_inicial == '1':
    while True:
        nome = input("Digite o nome de um aluno ou 'sair' para encerrar o cadastro: ").strip()

        if nome.lower() == 'sair':
            print('Encerrando cadastro...')
            break

        if nome == "":
            print("Nome inválido. Tente novamente.")
            rejeitados += 1
        else:
            if nome in nomes:
                print("Este nome já está cadastrado. Evite duplicidade.")
                rejeitados += 1
            else:
                confirmar = input(f"Confirma que deseja cadastrar o nome '{nome}'? (Sim/Não): ").strip().lower()

                if confirmar == 'sim':
                    nomes.append(nome)
                    print(f"O nome '{nome}' foi cadastrado com sucesso!")
                if confirmar == 'não':
                    print("Cadastro cancelado.")
                    rejeitados += 1
                if confirmar != 'sim' and confirmar != 'não':
                    print("Resposta inválida. Cadastro rejeitado.")
                    rejeitados += 1

if resposta_inicial != '0' and resposta_inicial != '1':
    print("Opção inválida. Sistema encerrado.")

# Relatório final
print(f'''

########################################################
#               RELATÓRIO FINAL DO SISTEMA            #
########################################################

Nomes cadastrados:
''')

for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")

print(f'''
--------------------------------------------------------
Total de nomes cadastrados com sucesso : {len(nomes)}
Total de cadastros rejeitados           : {rejeitados}
########################################################
''')


