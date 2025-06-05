import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
#Plotly express auxilia na criação de dashboards (utilizando plotly express), que é uma forma mais simples de trabalhar com o Plotly
# quando temos os dados em um DataFrame.
import plotly.express as px



##############################################################################

# Supress Scientific Notation
#np.set_printoptions(suppress=True) é usado para suprimir a exibição de valores pequenos de ponto flutuante em notação científica
#quando utilizamos funções do numpy. Ao definir suppress=True, quaisquer números muito pequenos serão exibidos como 0 em vez de notação científica.
np.set_printoptions(suppress=True)
#pd.set_option('display.float_format', '{:.2f}'.format) é usado para definir o formato de exibição dos
#números de ponto flutuante em um DataFrame do pandas. Ao definir '{:.2f}'.format, os números serão exibidos com duas casas decimais.'''
pd.set_option('display.float_format', '{:.2f}'.format)

##############################################################################


# Carregando os dados na memória
data = pd.read_csv( '/content/kc_house_data.csv' )
##############################################################################

data