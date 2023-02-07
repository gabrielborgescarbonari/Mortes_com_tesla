import pandas as pd
import seaborn as srn
import statistics as sts
import numpy as np
import matplotlib.pyplot as plt

# importar dados
dataset = pd.read_csv("Tesla Deaths - Deaths.csv")
# visulizar
dataset.head()
# tamanho
dataset.shape
# primeiro problema é dar nomes as colunas
dataset.columns = ["Caso", "Ano",
                   "Data", "País", "Estado",
                   "Descrição", "Mortes", "Motorista",
                   "Ocupante", "Outro", "Pedestre",
                   "TSLA", "Modelo", "Alegado Piloto Automático",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# deletar colunas insignificantes
dataset.drop(['1', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'TSLA'], axis=1, inplace=True)
# deletar linhas insignificantes
dataset.drop([294, 295, 296, 297, 298, 299, 300, 301,
             302, 303, 304, 305, 306], inplace=True)

# EXPLORAR DADOS CATEGÓRICOS
# País (Agrupar mesmos) AGRUPAR OS QUE TEM 1 EM OUTROS
pais = dataset['País'].value_counts()
pais
pais.plot.bar(color='gray')

# Estado (Agrupar mesmos) ARRUMAR NOMES E RENOMEAR "-"
est = dataset['Estado'].value_counts()
est
est.plot.bar(color='gray')

# Modelo do Tesla  ARRUMAR (TIRAR O ESPAÇO) NOMES E RENOMEAR "-"
mod = dataset['Modelo'].value_counts()
mod
mod.plot.bar(color='gray')

# EXPLORAR COLUNAS NUMÉRICAS
# Ano #ajustar valores errados 202 e os anos de 2023
dataset['Ano'].describe()
srn.boxplot(dataset['Ano']).set_title('Ano')
srn.histplot(dataset['Ano']).set_title('Ano')

# Mortes Totais
dataset['Mortes'].describe()
srn.histplot(dataset['Mortes']).set_title('Mortes')

# Motorista foi morto #ajustar valores errados "-" e NANs
dataset['Motorista'].describe()
srn.boxplot(dataset['Motorista']).set_title('Motorista')
srn.histplot(dataset['Motorista']).set_title('Motorista')

# Ocupante foi morto #ajustar valores errados "-" e NANs
dataset['Ocupante'].describe()
srn.boxplot(dataset['Ocupante']).set_title('Ocupante')
srn.histplot(dataset['Ocupante']).set_title('Ocupante')

# Em outro veiculo foi morto #ajustar valores errados "-" e NANs
dataset['Outro'].describe()
srn.boxplot(dataset['Outro']).set_title('Outro')
srn.histplot(dataset['Outro']).set_title('Outro')

# Pedestre foi morto #ajustar valores errados "-" e NANs
dataset['Pedestre'].describe()
srn.boxplot(dataset['Pedestre']).set_title('Pedestre')
srn.histplot(dataset['Pedestre']).set_title('Pedestre')

# Alegado Piloto Automático #ajustar valores errados "-" e NANs
dataset['Alegado Piloto Automático'].describe()
srn.boxplot(dataset['Alegado Piloto Automático']
            ).set_title('Alegado Piloto Automático')
srn.histplot(dataset['Alegado Piloto Automático']
             ).set_title('Alegado Piloto Automático')

# procurar valores nulos (0)
dataset.isnull().sum()
