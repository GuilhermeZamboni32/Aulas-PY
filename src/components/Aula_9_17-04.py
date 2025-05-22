#           0         1      2    3    posição
lista = ["o carro", "peixe", 123, 111]
#           1         2      3    4   quantidade de elementos
len(lista)

#///////////////////////////////////////////////////////

#           0         1      2    3    posição
lista = ["o carro", "o peixe", 123, 111]
#           1         2      3    4   quantidade de elementos
lista2 = ["a carro", "a peixe", 456, 222]
lista3 = lista + lista2
len(lista3)
print(lista3)

#///////////////////////////////////////////////////////

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

min = numeros[0]
max = numeros[0]

for numero in numeros:
  if numero < min:
    min = numero
  if numero > max:
    max = numero
print(numero)
print(min)
print(max)

#///////////////////////////////////////////////////////

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(numeros))
print(max(numeros))

#///////////////////////////////////////////////////////

livros = ['Java', 'Sql', 'Php', 'python',]
livros.append('android')
print(livros)

#///////////////////////////////////////////////////////

livros = ['Java', 'Sql', 'Php', 'python']
livros.append('android')
print(livros)

livros.pop(0)
print(livros)

livros.remove('Java')
print(livros)

livros.sort()
print(livros)

livros.revers()
print(livros)

livros.remove('java')
print(livros)

print(livros.cout('Html'))

