#/////////////////////////////////////////////////////////////

# Importa a biblioteca random para gerar números aleatórios
import random
# Função para escrever 'n' números aleatórios em um arquivo de texto
def escreverNumerosAleatorios(n, nomeArquivo):
    with open(nomeArquivo, "w") as arquivo:
        for _ in range(n):
            numero = random.randint(1, 100) # Gera número aleatório entre 1 e 100
            arquivo.write(str(numero) + "\n") # Escreve o número no arquivo


escreverNumerosAleatorios(100, "aleatorios.txt")


# Função para copiar o conteúdo de um arquivo para outro
def copiaArquivo(velhoArquivo, novoArquivo):
    f1 = open(velhoArquivo, "r") # Abre o arquivo original para leitura
    f2 = open(novoArquivo, "w") # Abre/cria o novo arquivo para escrita
    for texto in f1:
         f2.write(texto) # Copia cada linha do arquivo antigo para o novo
    f1.close() # Fecha o arquivo original
    f2.close() # Fecha o novo arquivo


   copiaArquivo("aleatorios.txt", "novo_aleatorio.txt") 


# Exibindo o início do arquivo copiado para conferência
with open("novo_aleatorio.txt", "r") as f:
    for i in range(10): # Mostra só as 10 primeiras linhas
        print(f.readline().strip())



