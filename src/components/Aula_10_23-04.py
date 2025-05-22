#///////////////////////////////////////////////////////

lista = [15, 7, 27, 39]
procurado=int(input("Digite o valor a ser procurado: "))

achou=False

x=0
while x<len(lista):
  if lista[x]==procurado:
    achou=True
    break
  x+=1
if achou:
  print("%d achado na posiçõa %d" % (procurado, x))
else:
  print("%d não foi encontrado na lista" % procurado)

#///////////////////////////////////////////////////////

lista=[1, 2, 3, 4, 5]

x=0

while x<len (lista):
  elemento=lista[x]
  print(elemento)
  x+=1

#///////////////////////////////////////////////////////

lista=[1, 2, 3, 4, 5, 6]

for elemento in lista:
  print(lista)

#///////////////////////////////////////////////////////

lista = [15, 7, 27, 39]
procurado=int(input("Digite o valor a ser procurado: "))

for elementos in lista:
  if elementos==procurado:
    print("Elemento encontrado")
    break
else:
  print("Elemento não encontrado!")

#///////////////////////////////////////////////////////

while True:
  lista = [15, 7, 27, 39]
  procurado = int(input("Digite o valor a ser procurado (ou 0 para sair): "))

  if procurado == 0:
    break
  x=0

  for elementos in lista:
    if elementos == procurado:
      print("O número %d foi achado na posiçõa %d" % (procurado, x))
      break
  else:
    print("%d não foi encontrado na lista" % procurado)

#///////////////////////////////////////////////////////

while True:
    lista = [15, 7, 27, 39]
    procurado = int(input("Digite o valor a ser procurado (ou 0 para sair): "))

    if procurado == 0:
        break

    x = 0  # Counter initialized here
    for i in range(len(lista)):
        x += 1
        if lista[i] == procurado:
            print("O número %d foi achado na posição %d" % (procurado, x))
            break
    else:
        print("%d não foi encontrado na lista" % procurado)

#///////////////////////////////////////////////////////

for valor in range(1,10):
  print(valor)

#///////////////////////////////////////////////////////

lista=[1,7,2,4,0]
max=lista[0]

for encontrar in lista:
  if encontrar> max:
    max=encontrar
print(max)

#///////////////////////////////////////////////////////

lista=[1,79,2,4,0,85,8,9,13,15,5,45,9,326,3]
max=lista[0]
min=lista[0]

for encontrar in lista:
  if encontrar > max:
    max=encontrar
  if encontrar < min:
    min=encontrar

print("Maior valor: ", max)
print("Menor valor :", min)

#///////////////////////////////////////////////////////

valores=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
pares=[]
impares=[]

for elementos in valores:
  if elementos % 2 == 0:
    pares.append(elementos)
  else:
    impares.append(elementos)

#print("Lista total dos números: ", valores)
print("Lista dos números Pares: ", pares)
print("Lista dos números Impares: ", impares)

#///////////////////////////////////////////////////////

lista=[1,2,3,4,5,6,7,8,9,10,]

valor = 4
removeu = False
temp = []

for i in range(len(lista)):
  if lista[i] != valor or removeu:
    temp.append(lista[i])
  else:
    removeu = True
lista = temp
print(lista)

##############

lista2=[1,2,3,4,5,6,7,8,9,10,]
lista2.remove(4)
print(lista2)

#///////////////////////////////////////////////////////