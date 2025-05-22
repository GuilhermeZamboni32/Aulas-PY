categoria = int(input("informe a categoria do produto"))
preco = 0

if categoria == 1:
  preco= 10
else:
  if categoria == 2:
   preco= 18
  else:
    if categoria == 3:
      preco = 23
    else:
      if categoria == 4:
        preco = 26
      else:
        if categoria == 5:
          preco = 31

print("O valor do produto é R$:%3.2f" %preco)

# #///////////////////////////////////////////////////////////
meta = 20000
vendas = 50000

if vendas < meta:
   print("Não ganhou bônus")
elif vendas > (meta*2):
   bonus= 0.07 * vendas
   print("ganhou {} de bônus" .format(bonus))
else:
  bonus = 0.03 * vendas
  print("ganhou {} de bônus" .format(bonus))

  # #///////////////////////////////////////////////////////////
vendas = int(input("informe quanto você ganhou em vendas esse mês: "))
meta = 20000

if vendas < meta:
  print("você não vai ganhar seu bônus")
else:
  if vendas > (meta*2):
    bonus = 0.07 * vendas
    print("você ganhou {} de bônus" .format(bonus))
  else:
    bonus = 0.03 * vendas
    print("você ganhou {} de bônus" .format(bonus))
  # #///////////////////////////////////////////////////////////
if not "#" in "lira@hastagtreinamento.com.br":
   print('não tem #')
else:
  print('tem #')

###########################################################

if "@" in "lira@hastagtreinamento.com.br":
   print(' tem @')
else:
  print('não tem @')
  # #///////////////////////////////////////////////////////////
voce = input("Você tem está com fome ? ")

if voce == 'não':
  print("blz então")
else:
  if voce == 'sim':
   comida = input("Você tem comida em casa ? ")
   if comida == "não":
    print("Então vai para o mercado e compre comida, volte para casa e prepare uma refeição e coma a sua refeição.")
   if comida == 'sim':
    print("Então prepare uma refeiçõa")
  # #///////////////////////////////////////////////////////////
fome = input("Você tem está com fome ? ")

if fome == 'não':
  print("blz então")
else:
  if voce == 'sim':
   comida = input("Você tem comida em casa ? ")
  # #///////////////////////////////////////////////////////////