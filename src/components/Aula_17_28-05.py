#Exercício de Estruturas: Lista, Tupla e Dicionário – Petshop


#1. Enunciado
#Crie um programa em Python que gerencie o atendimento de um petshop, seguindo estes passos:

#Lista: criar uma lista chamada pets com pelo menos 5 nomes de animais.
#Tupla: criar uma tupla chamada servicos contendo pares (nome_servico, preco).
#Dicionário: criar um dicionário chamado agenda onde:
#chave: nome do pet (reutilizar nomes de pets)
#valor: outro dicionário com as chaves "tutor", "servico", "preco" e "data". O programa deve: • - Imprimir todos os pets da lista. • - Imprimir cada serviço da tupla, mostrando nome e preço. • - Percorrer o dicionário agenda e gerar um relatório formatado. • - Calcular o total faturado somando todos os preços em agenda e exibir no final.




#2. Tabela de Síntese
#__________________________________________________________________________________________________________________________________________________________________________________________
#|  Estrutura	    |  Nome da variável  |	                              Exemplo de conteúdo	                                         |                              Uso                  |
#|_________________|____________________|_____________________________________________________________________________________________|___________________________________________________|
#|  Lista	        |       pets         | 	["Rex", "Luna", "Mingau", "Bolt", "Paçoca"]	                                               |      Armazenar nomes de pets para atendimento     |
#|  Tupla	        |      servicos	     |   (("Banho", 50.0), ("Tosa", 80.0), ("Vacina", 120.0))	                                     |        Serviços fixos e seus preços               |
#|  Dicionário     |     	agenda       |  { "Rex": {"tutor": "Ana", "servico": "Banho", "preco": 50.0, "data": "20/05/2025"}, ... }  |     	Relacionar cada pet ao seu atendimento       |
#|_________________|____________________|_____________________________________________________________________________________________|___________________________________________________|


#############################################################################################################################
#############################################################################################################################

#2.1 Minha Tentativa
# 1- Lista: criar uma lista chamada pets com pelo menos 5 nomes de animais.

pets = ["Rex", "Luna", "Mingau", "Bolt", "Paçoca"]

# 2- Tupla: criar uma tupla chamada servicos contendo pares (nome_servico, preco).
servicos =  (
    ("Banho", 50.0), 
    ("Tosa", 80.0), 
    ("Vacina", 120.0)
)

# 3- Dicionário: criar um dicionário chamado agenda onde:
agenda = {
    "Rex":    {"tutor": "Ana",   "servico": "Banho",  "preco": 50.0,  "data": "20/05/2025"},
    "Luna":   {"tutor": "Bruno", "servico": "banho",  "preco": 50.0,  "data": "20/05/2025"},
    "Mingau": {"tutor": "Carla", "servico": "Vacina", "preco": 120.0, "data": "21/05/2025"},
    "Bolt":   {"tutor": "Diego", "servico": "Banho",  "preco": 50.0,  "data": "21/05/2025"},
    "Paçoca": {"tutor": "Elaine","servico": "Tosa",   "preco": 80.0,  "data": "22/05/2025"},
}

print("Lista dos pets a serem atendidos:")
for pet in pets:
    print(f"{pet}")

print("\nServiços disponiveis no momento:")
for servico, preco in servicos:
    print(f"{servico}: R$ {preco:.2f}")



#############################################################################################################################
#############################################################################################################################



#2.2 Minha Tentativa --- (Melhorada)
pets = ["Nina","Zoe","Tipi","Lila","Luna","Thor","Mel","Bebel","Sadan","Bilu",]

servicos = (
    ("Banho", 50.0), 
    ("Tosa", 80.0), 
    ("Hidratação de Pelagem", 90.0),
    ("Vacina", 120.0),
    ("Consulta Veterinária", 150.0),
    ("Hotel para Pets (Diária)", 200.0)
)

agenda = {
    "Nina":   {"tutor": "Ana",     "servico": "Banho",                   "preco": 50.0,  "data": "20/05/2025"},
    "Zoe":    {"tutor": "Bruno",   "servico": "Tosa",                    "preco": 80.0,  "data": "20/05/2025"},
    "Tipi":   {"tutor": "Carla",   "servico": "Vacina",                  "preco": 120.0, "data": "21/05/2025"},
    "Lila":   {"tutor": "Diego",   "servico": "Hidratação de Pelagem",   "preco": 90.0,  "data": "21/05/2025"},
    "Luna":   {"tutor": "Elaine",  "servico": "Consulta Veterinária",    "preco": 150.0, "data": "22/05/2025"},
    "Thor":   {"tutor": "Fábio",   "servico": "Banho",                   "preco": 50.0,  "data": "22/05/2025"},
    "Mel":    {"tutor": "Gabriela","servico": "Hotel para Pets (Diária)","preco": 200.0, "data": "23/05/2025"},
    "Bebel":  {"tutor": "Henrique","servico": "Tosa",                    "preco": 80.0,  "data": "23/05/2025"},
    "Sadan":  {"tutor": "Isabela", "servico": "Vacina",                  "preco": 120.0, "data": "24/05/2025"},
    "Bilu":   {"tutor": "João",    "servico": "Hidratação de Pelagem",   "preco": 90.0,  "data": "24/05/2025"},
}


while True:
    print("\n=========== MENU PETSHOP ============")
    print("| 1 |     Ver lista de Pets         |")
    print("|___________________________________|")
    print("| 2 |    Ver serviços disponíveis   |")
    print("|___________________________________|")
    print("| 3 |     Ver agenda dos pets       |")
    print("|___________________________________|")
    print("| 4 |            Sair               |")
    print("=====================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n Lista de pets:")
        for pet in pets:
            print(f"- {pet}")

    elif opcao == "2":
        print("\n Serviços disponíveis:")
        for servico, preco in servicos:
            print(f"- {servico}: R$ {preco:.2f}")

    elif opcao == "3":
        print("\n Agenda dos pets:")
        for pet, dados in agenda.items():
            print(f"- {pet} | Tutor: {dados['tutor']} | Serviço: {dados['servico']} | Preço: R$ {dados['preco']:.2f} | Data: {dados['data']}")

    elif opcao == "4":
        print("\nSaindo do sistema.")
        break

    else:
        print("\nErro! Tente novamente.")



#############################################################################################################################
#############################################################################################################################


#3. Código Comentado --- (Professor)
# 👥 LISTA: nomes dos pets que serão atendidos
pets = ["Rex", "Luna", "Mingau", "Bolt", "Paçoca"]

# 🛠️ TUPLA: serviços fixos do petshop (nome, preço)
servicos = (
    ("Banho", 50.0),
    ("Tosa", 80.0),
    ("Vacina", 120.0)
)

# 📋 DICIONÁRIO: agenda de atendimentos
agenda = {
    "Rex":    {"tutor": "Ana",   "servico": "Banho",  "preco": 50.0,  "data": "20/05/2025"},
    "Luna":   {"tutor": "Bruno", "servico": "Tosa",   "preco": 80.0,  "data": "20/05/2025"},
    "Mingau": {"tutor": "Carla", "servico": "Vacina", "preco": 120.0, "data": "21/05/2025"},
    "Bolt":   {"tutor": "Diego", "servico": "Banho",  "preco": 50.0,  "data": "21/05/2025"},
    "Paçoca": {"tutor": "Elaine","servico": "Tosa",   "preco": 80.0,  "data": "22/05/2025"},
}

# 1️⃣ Imprimir todos os pets (LISTA)
print("Pets para atendimento:")
for pet in pets:
    print(f" - {pet}")

# 2️⃣ Imprimir serviços disponíveis (TUPLA)
print("\nServiços disponíveis:")
for nome_servico, preco in servicos:
    print(f" - {nome_servico}: R$ {preco:.2f}")

# 3️⃣ Gerar relatório de atendimentos (DICIONÁRIO)
print("\nAgenda de atendimentos:")
total_faturado = 0.0
for pet, info in agenda.items():
    tutor   = info["tutor"]
    servico = info["servico"]
    preco   = info["preco"]
    data    = info["data"]
    print(f"Pet: {pet}, Tutor: {tutor}, Serviço: {servico}, Preço: R$ {preco:.2f}, Data: {data}")
    total_faturado += preco

# 4️⃣ Calcular e exibir total faturado
print(f"\n💰 Total faturado: R$ {total_faturado:.2f}")
