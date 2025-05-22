lista = [-12, 50, 25, 0 ,45, 9]
print(lista)
type(lista)

#/////////////////////////////////////////////////////////////

lista1 = [-12, 50, 25, 0 ,45, 9]
print(lista)

lista2 = {10, 'coco', 1002.55,'05/01/2000'}
print(lista2)

print(lista1[0])

print(lista2[0])

#/////////////////////////////////////////////////////////////

notas = [5, 10, 7]
somanotas = notas[0] + notas[1] + notas[2]
print(somanotas)

#/////////////////////////////////////////////////////////////

cidades = []

cidade = input("digite o nome da cidade: ")
cidades.append(cidade)

cidades.append(input("Digite o nome da segunda cidade:"))
cidades.append(input("Digite o nome da terceira cidade:"))
print(cidades)

#/////////////////////////////////////////////////////////////

cidades = []
contador = 1

while contador <= 3:
  contador += 1

  cidade = input("digite o nome de uma cidade:")
  cidades.append(cidade)

  print(cidades)

#/////////////////////////////////////////////////////////////

cidades = []

while True:
    if len(cidades) <= 2:
      nome_cidade = input("digite o nome de alguma cidade: ")
      cidades.append(nome_cidade)
    else:
      print(cidades)
      break

#/////////////////////////////////////////////////////////////

unidades =['Newton', 'Joule', 'Kelvin', 'Pascal']
print(unidades)
print("No indice =3 temos: ", unidades[-1])
print("No indice =2 temos: ", unidades[-2])
print("No indice =1 temos: ", unidades[-3])
print("No indice =0 temos: ", unidades[-4])

#/////////////////////////////////////////////////////////////

unidades =['Newton', 'Joule', 'Kelvin', 'Pascal']
print(unidades)
x = len(unidades)

for i, elemento in enumerate (unidades):
  print("No indice =", (x - 1), "temos:", unidades[x -1])
  x = x - 1

#/////////////////////////////////////////////////////////////

lista1=[1,2,3,4,5]
lista2=[6,7,8,9]
lista3=[10,11,12,13,14]
todaslistas = {lista1,lista2,lista3}
print(todaslistas)

#/////////////////////////////////////////////////////////////



