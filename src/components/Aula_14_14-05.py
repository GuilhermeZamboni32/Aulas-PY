#/////////////////////////////////////////////////////////////

vendas = ('lira', '25/08/2020', '15/02/1994', 2000, 'estagiario')
print(vendas)

nomes=vendas[0]
dataContrattacao = vendas[1]
dataNascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(nomes)
print(dataContrattacao)
print(dataNascimento)
print(salario)
print(cargo)


#/////////////////////////////////////////////////////////////

vendas = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)

funcionario = ('João', 'Maria', 'José', 'Carlos', 'Ana', 'marcos', 'Guilhetme', 'Marta', 'Veroni', 'Gustavo')

# Primeira forma
for item in enumerate(vendas):
  print(item)
print('\n')

# Segunda forma
for item in (vendas, funcionario):
  print(item)
print('\n')

# Tertceira forma
for i, item in enumerate(vendas):
  print(i, item, funcionario[i])
print('\n')

# Quarta forma
for i in enumerate(zip(vendas, funcionario)):
  print(i)

#/////////////////////////////////////////////////////////////

vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('21/08/2020', 'lg', 'prata', '128gb', 1500, 4000),
    ('22/08/2020', 'nokia', 'preto', '256gb', 500, 4500),
    ('23/08/2020', 'iphone x', 'preto', '64gb', 300, 3800),
    ('23/08/2020', 'lg', 'dourado', '64gb', 1000, 3200),
    ('24/08/2020', 'nokia', 'azul', '128gb', 450, 4200),
    ('25/08/2020', 'iphone x', 'branco', '256gb', 500, 4700),
    ('25/08/2020', 'lg', 'azul', '256gb', 1400, 4100),
    ('26/08/2020', 'nokia', 'cinza', '64gb', 350, 3000),
    ('27/08/2020', 'iphone x', 'vermelho', '128gb', 400, 3900),
]


faturamento = 0

for item in vendas:
  data, produto, cor, capacidade, unidades, valor_unitario = item
  if produto == 'iphone x' and data == '20/08/2020':
    faturamento += unidades * valor_unitario

print('O faturamento do Iphone no dia 20/08/2020 foi de {}'.format(faturamento))



#/////////////////////////////////////////////////////////////

vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('21/08/2020', 'lg', 'prata', '128gb', 1500, 4000),
    ('22/08/2020', 'nokia', 'preto', '256gb', 500, 4500),
    ('23/08/2020', 'iphone x', 'preto', '64gb', 300, 3800),
    ('23/08/2020', 'lg', 'dourado', '64gb', 1000, 3200),
    ('24/08/2020', 'nokia', 'azul', '128gb', 450, 4200),
    ('25/08/2020', 'iphone x', 'branco', '256gb', 500, 4700),
    ('25/08/2020', 'lg', 'azul', '256gb', 1400, 4100),
    ('26/08/2020', 'nokia', 'cinza', '64gb', 350, 3000),
    ('27/08/2020', 'iphone x', 'vermelho', '128gb', 400, 3900),
]

faturamento = 0

for item in vendas:
  data, produto, cor, capacidade, unidades, valor_unitario = item
  if (produto == 'iphone x') and (data == '20/08/2020', '21/08/2020'):
    faturamento += unidades * valor_unitario

print('O faturamento do Iphone no dia 20/08/2020 e 21/08/2020 foi de {}'.format(faturamento))


#/////////////////////////////////////////////////////////////

#######################################################
#      Exercícios com Python – Análise de Vendas      #
#######################################################

vendas = [
 ('05/09/2020', 'iPhone 13', 'preto', '256GB', 12, 6000),
 ('05/09/2020', 'iPhone 13', 'azul', '256GB', 8, 6000),
 ('05/09/2020', 'Samsung Galaxy S21', 'preto', '128GB', 15, 4000),
 ('05/09/2020', 'Xiaomi 12', 'preto', '256GB', 20, 3000),
 ('05/09/2020', 'Xiaomi 12', 'azul', '256GB', 10, 3000),
 ('05/09/2020', 'Motorola Edge', 'preto', '128GB', 9, 2800),
 ('05/09/2020', 'LG Wing', 'rosa', '128GB', 7, 2500),
 ('05/09/2020', 'Nokia 6.2', 'preto', '64GB', 11, 1600),
 ('05/09/2020', 'iPhone 11', 'verde', '128GB', 10, 4000),
 ('05/09/2020', 'iPhone SE', 'vermelho', '64GB', 6, 3200),
]

#Exercício 1 – Faturamento total de produtos pretos
#Calcule o faturamento total apenas dos produtos com a cor 'preto'.

faturamento = 0

for item in vendas:
  data, produto, cor, capacidade, unidades, valor_unitario = item
  if cor == 'preto':
    faturamento += unidades * valor_unitario

print('O total de faturamento dos produtos da cor preta são de: {}'.format(faturamento))



#/////////////////////////////////////////////////////////////

#Exercício 2 – Total de unidades vendidas por um modelo
#Calcule o total de unidades vendidas do modelo 'Xiaomi 12'.

vendas = [
 ('05/09/2020', 'iPhone 13', 'preto', '256GB', 12, 6000),
 ('05/09/2020', 'iPhone 13', 'azul', '256GB', 8, 6000),
 ('05/09/2020', 'Samsung Galaxy S21', 'preto', '128GB', 15, 4000),
 ('05/09/2020', 'Xiaomi 12', 'preto', '256GB', 20, 3000),
 ('05/09/2020', 'Xiaomi 12', 'azul', '256GB', 10, 3000),
 ('05/09/2020', 'Motorola Edge', 'preto', '128GB', 9, 2800),
 ('05/09/2020', 'LG Wing', 'rosa', '128GB', 7, 2500),
 ('05/09/2020', 'Nokia 6.2', 'preto', '64GB', 11, 1600),
 ('05/09/2020', 'iPhone 11', 'verde', '128GB', 10, 4000),
 ('05/09/2020', 'iPhone SE', 'vermelho', '64GB', 6, 3200),
]

faturamento = 0

for item in vendas:
  data, produto, cor, capacidade, unidades, valor_unitario = item
  if produto == 'Xiaomi 12':
    faturamento += unidades * valor_unitario

print('O total de faturamento do produto do produto "Xiaomi 12" foi de: {}'.format(faturamento))



#/////////////////////////////////////////////////////////////

#Exercício 3 – Faturamento de um modelo com cor e capacidade
#específicas
#Calcule o faturamento total do modelo 'iPhone 13', na cor 'preto' e com '256GB'.

vendas = [
 ('05/09/2020', 'iPhone 13', 'preto', '256GB', 12, 6000),
 ('05/09/2020', 'iPhone 13', 'azul', '256GB', 8, 6000),
 ('05/09/2020', 'Samsung Galaxy S21', 'preto', '128GB', 15, 4000),
 ('05/09/2020', 'Xiaomi 12', 'preto', '256GB', 20, 3000),
 ('05/09/2020', 'Xiaomi 12', 'azul', '256GB', 10, 3000),
 ('05/09/2020', 'Motorola Edge', 'preto', '128GB', 9, 2800),
 ('05/09/2020', 'LG Wing', 'rosa', '128GB', 7, 2500),
 ('05/09/2020', 'Nokia 6.2', 'preto', '64GB', 11, 1600),
 ('05/09/2020', 'iPhone 11', 'verde', '128GB', 10, 4000),
 ('05/09/2020', 'iPhone SE', 'vermelho', '64GB', 6, 3200),
]


faturamento = 0

for item in vendas:
  data, produto, cor, capacidade, unidades, valor_unitario = item
  if (produto == 'iPhone 13') and (cor == 'preto') and (capacidade == '256GB'):
    faturamento += unidades * valor_unitario

print('O faturamento total do modelo iPhone 13 na cor preta e com 256GB de memoria foi de: {}'.format(faturamento))

#/////////////////////////////////////////////////////////////

#Exercício 4 – Produto mais vendido (em unidades)
#Identifique o produto com maior número de unidades vendidas.

vendas = [
 ('05/09/2020', 'iPhone 13', 'preto', '256GB', 12, 6000),
 ('05/09/2020', 'iPhone 13', 'azul', '256GB', 8, 6000),
 ('05/09/2020', 'Samsung Galaxy S21', 'preto', '128GB', 15, 4000),
 ('05/09/2020', 'Xiaomi 12', 'preto', '256GB', 20, 3000),
 ('05/09/2020', 'Xiaomi 12', 'azul', '256GB', 10, 3000),
 ('05/09/2020', 'Motorola Edge', 'preto', '128GB', 9, 2800),
 ('05/09/2020', 'LG Wing', 'rosa', '128GB', 7, 2500),
 ('05/09/2020', 'Nokia 6.2', 'preto', '64GB', 11, 1600),
 ('05/09/2020', 'iPhone 11', 'verde', '128GB', 10, 4000),
 ('05/09/2020', 'iPhone SE', 'vermelho', '64GB', 6, 3200),
]

faturamento = 0

for item in vendas:
  data, produto, cor, capacidade, unidades, valor_unitario = item
  if ( unidades == 20):
    faturamento += unidades * valor_unitario

print('O faturamento do produto com maior número de unidades vendidas foi de: {}'.format(faturamento))


#