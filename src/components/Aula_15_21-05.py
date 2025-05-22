#/////////////////////////////////////////////////////////////

arquivo = open("numeros.txt", "w")

for linha in range (1, 101): #criaçõa de linhas numeradas até 100
  arquivo.write("%d\n" %linha)
arquivo.close()

#/////////////////////////////////////////////////////////////

arquivo = open("numeros.txt", "r")

for linha in arquivo.readlines(): #o método readlines, gera uma lista em que cada elemento
  print(linha)
arquivo.close()

#/////////////////////////////////////////////////////////////

nomeFile=input("Digite o nome do arquivo:")

try:
  file = open(nomeFile, "r")
  for linha in file:
    campos = linha.split(';')
    print(campos)
  file.close()
except IOError as error:
  print("ERRO: ", error)

#/////////////////////////////////////////////////////////////

#cirar um progama para gerar dois arquivos com 500 linhas cada.
#o progama distribui os numeros impares e pares em arquivos diferentes

Pares = open("Numeros_Pares.txt", "w")
Inpares = open("Numeros_Inpares.txt", "w")

for linha in range (1, 1001): #criaçõa de linhas numeradas até 500

  if linha % 2 == 0:
    Pares.write(f"{linha}\n")
  else:
    Inpares.write(f"{linha}\n")

Pares.close()
Inpares.close()

#/////////////////////////////////////////////////////////////

lista = [
    'banana', 'morango', 'laranja', 'abacaxi', 'sapoti',
    'maçã', 'pera', 'uva', 'melancia', 'melão',
    'kiwi', 'cereja', 'ameixa', 'figo', 'caqui',
    'pêssego', 'nectarina', 'framboesa', 'amora', 'jabuticaba',
    'graviola', 'caju', 'acerola', 'mamão', 'tamarindo',
    'carambola', 'pitanga', 'jaca', 'cupuaçu', 'umbu',
    'lichia', 'longan', 'rambutan', 'physalis', 'maracujá',
    'mirtilo', 'groselha', 'araticum', 'atemoia', 'camapu',
    'bacaba', 'bacuri', 'biribá', 'cambuci', 'jenipapo',
    'murici', 'pequi', 'umbu-cajá', 'santol', 'nêspera'
]

arq = open('frutas.txt', 'w')

for fruta in lista:
  arq.write('%s\n' % fruta)

arq.close()

#/////////////////////////////////////////////////////////////

#criando o arquivo memo.txt no diretório atual do colab
conteudo = '''Este arquivo foi criado para fins de exeplo didático
podemos adicionar linhas de texto aqui!
arquivo criado via python.'''

with open('memo.txt', 'w', encoding='uft-8') as arquivo:
  arquivo.write(conteudo)

print("Arquivo 'memo.txt' criado com sucesso!")

#/////////////////////////////////////////////////////////////



#/////////////////////////////////////////////////////////////



