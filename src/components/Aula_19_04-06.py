'''
Quantas imóveis/casas estão disponíveis para compra?
Quantos atributos as casas possuem?
Quais são os atributos das casas?
Qual a casa mais cara ( casa com o maior valor de venda )?
Qual a casa com o maior número de quartos?
Qual a soma total de quartos do conjunto de dados?
Quantas casas possuem 2 banheiros?
Qual o preço médio de todas as casas no conjunto de dados?
Qual o preço médio de casas com 2 banheiros?
Qual o preço mínimo entre as casas com 3 quartos?
Quantas casas possuem mais de 300 metros quadrados na sala de estar?
Quantas casas tem mais de 2 andares?
Quantas casas tem vista para o mar?
Das casas com vista para o mar, quantas tem 3 quartos?
Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?'''


#############################################################################################################

# Eu vou considerar que a coluna "id" representa a identificação única do imóvel
num_houses_unique = data['id'].nunique()
# Resultado
print( 'Estão disponíveis {} imóveis'.format( num_houses_unique ) )


'''O método nunique() devolve o número de valores únicos para cada coluna. Ao especificar o eixo da
coluna ( axis='columns' ), o método nunique() pesquisa por coluna e devolve o número de valores únicos
para cada linha.'''

#############################################################################################################

# O número de colunas representam os atributos do apartamento.
# id e date - não são atributos do apartamento
num_attributes = len(data.columns) - 2
# Resultado
print( 'Os imóveis posseum {} atributos'. format( num_attributes ) )


#############################################################################################################

# Estratégia: Excluir as colunas "id", "date" e mostrar os atributos restantes.
df = data.drop( ['id', 'date'], axis=1 )
print( df.columns.tolist() )

'''O parâmetro axis define se a comparação vai ser entre linhas ou entre colunas. Se axis = 0 ele irá
comparar os valores presentes nas linhas, já se axis = 1 ele irá comparar os valores presentes em
colunas.'''



# dicionario de dados

price = 'preço'  # quantidade de preço da casa
bedrooms = 'quartos'  # quantidade de quartos da casa
bathrooms = 'banheiros'  # quantidade de banheiros da casa
sqft_living = 'm²_sala'  # metragem da área interna da sala da casa
sqft_lot = 'm²_lote'  # metragem total do terreno da casa
floors = 'andares'  # quantidade de andares da casa
waterfront = 'beira-mar'  # se a casa é beira-mar (1) ou não (0)
view = 'vista'  # índice de qualidade da vista (0 a 4)
condition = 'condição'  # estado geral da casa (1 = ruim, 5 = excelente)
grade = 'nível'  # qualidade do material e acabamento da construção (1 a 13)
sqft_above = 'm²_acima'  # área construída acima do nível do solo
sqft_basement = 'm²_porão'  # área do porão da casa
yr_built = 'ano_construído'  # ano em que a casa foi construída
yr_renovated = 'ano_renovado'  # ano da última reforma (0 se nunca foi reformada)
zipcode = 'CEP'  # código postal da localização da casa
lat = 'latitude'  # coordenada geográfica de latitude
long = 'longitude'  # coordenada geográfica de longitude
sqft_living15 = 'm²_sala_15'  # média da área interna das 15 casas vizinhas mais próximas
sqft_lot15 = 'm²_lote15'  # média da metragem do terreno das 15 casas vizinhas mais próximas



dicionario_dados = {
    'price': 'preço',
    'bedrooms': 'quartos',
    'bathrooms': 'banheiros',
    'sqft_living': 'm²_sala',
    'sqft_lot': 'm²_lote',
    'floors': 'andares',
    'waterfront': 'beira-mar',
    'view': 'vista',
    'condition': 'condição',
    'grade': 'nível',
    'sqft_above': 'm²_acima',
    'sqft_basement': 'm²_porão',
    'yr_built': 'ano_construído',
    'yr_renovated': 'ano_renovado',
    'zipcode': 'CEP',
    'lat': 'latitude',
    'long': 'longitude',
    'sqft_living15': 'm²_sala_15',
    'sqft_lot15': 'm²_lote15'
}

#############################################################################################################

# Estratégia: Selecionar a coluna "id", "price", ordenar as casas pela coluna␣,"price" em ordem decrescente e
# escolher o imóvel do primeiro id.
house_expensive = data[['id', 'price']].sort_values( 'price', ascending=False).loc[0,'price']

print( 'Casa mais cara em o seguinte ID: {}'.format( house_expensive ) )

#############################################################################################################

# Estratégia:
# 1. Selecionar a coluna "id", "bedroom"
# 2. Ordenar os imóveis pelo número de quartos de ordem decrescente
# 3. Selecionar a primeira coluna "id"
df = data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False)
print('A casa com maior número de quartos: {}'.format(df.iloc[0,0]))

#############################################################################################################

# Estratégia:
# 1. Somar a coluna "bedrooms"
print(' Soma total de quartos: {}'.format( data['bedrooms'].sum()))

#############################################################################################################

# Estratégia:
# 1. Filtrar linhas (imóveis) que possuem 2 banheiros.
# 2. Contar o número de linhas do dataset
df = data.loc[data['bathrooms'] == 2, :]
num_houses = len( df )
print('Quantidade de casas que possuem 2 banheiros: {}'.format( num_houses ) )

#############################################################################################################

# Estratégia:
# 1. Selecionar imóveis com 2 banheiros.
# 2. Calcular o preço médio da coluna "price" do novo conjunto de dados
#mean (), 2 = duas casas após a vírgula
avg_price = np.round( data.loc[data['bathrooms'] == 2, 'price'].mean(), 2 )
print('Preço médio das casa com 2 banheiros: U${}'.format( avg_price ) )

#############################################################################################################

# Estratégia:
# 1. Selecionar imóveis com 3 bathrooms.
# 2. Calcular o menor preço da coluna "price" do novo conjunto de dados
min_price = np.round( data.loc[data['bedrooms'] == 3, 'price'].min(), 2 )
print( 'Preço mínimo entre as casa com 3 quartos: U${}'.format( min_price) )

#############################################################################################################

# Estratégia:
# 1. Selecionar imóveis com mais de 300 sqft_living.
# 2. Contar o número de imóveis nesse novo conjunto de dados.
houses = data.loc[data['sqft_living'] > 300, 'id'].shape[0]
print( 'Há {} casa que possuem mais de 300 metros quadrados de sala de estar'.format( houses ) )

#############################################################################################################

# Estratégia:
# 1. Selecionar imóveis com a coluna 'floors' maior que 2.
# 2. Contar o número de imóveis nesse novo conjunto de dados.
houses = data.loc[data['floors'] > 2, 'id'].shape[0]
print( 'Há {} casa com mais de 2 andares'.format( houses ) )

#############################################################################################################

# Estratégia:
# 1. Selecionar imóveis com a coluna 'waterfront' igual a 1.
# 2. Contar o número de imóveis nesse novo conjunto de dados.
houses = data.loc[data['floors'] == 1, 'id'].shape[0]
print( 'Há {} casa com vistas para o mar'.format( houses ) )

#############################################################################################################

# Estratégia:
# 1. Selecionar imóveis com a coluna 'waterfront' igual a 1 e a coluna 'bedrooms' maior que 3.
# 2. Contar o número de imóveis nesse novo conjunto de dados.
houses = data.loc[(data['waterfront'] == 1) & (data['bedrooms']> 2), 'id'].shape[0]
print( 'Há {} casa com vista para o mar e com 3 quartos'.format( houses ) )

#############################################################################################################

# Estratégia:
# 1. Selecionar imóveis com a coluna 'sqft_living' maior que 300 e a coluna 'bathrooms' maior que 2.
# 2. Contar o número de imóveis nesse novo conjunto de dados.
houses = data.loc[(data['sqft_living'] > 300) & (data['bathrooms'] > 2), 'id'].shape[0]
print( 'Há {} casa com mais de 300 metros quadrados de sala de estar e com mais de 2 banheiros'.format( houses ) )

#############################################################################################################



#############################################################################################################