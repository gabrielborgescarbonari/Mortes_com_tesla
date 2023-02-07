import pandas as pd
import seaborn as srn
import matplotlib.pyplot as plt

# importar dados
dataset = pd.read_csv("Tesla Deaths - Deaths.csv")
# visulizar
dataset.head()
# tamanho
dataset.shape
# primeiro problema é dar nomes as colunas
dataset.columns = ["Caso", "Ano",
                   "Data", "Pais", "Estado",
                   "Descrição", "Mortes", "Motorista",
                   "Ocupante", "Outro", "Pedestre",
                   "TSLA", "Modelo", "Alegado Piloto Automático",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# deletar colunas insignificantes
dataset.drop(['1', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'TSLA', 'Ano', 'Caso'], axis=1, inplace=True)
# deletar linhas insignificantes
dataset.drop([294, 295, 296, 297, 298, 299, 300, 301,
             302, 303, 304, 305, 306], inplace=True)

# EXPLORAR DADOS CATEGÓRICOS
# País (Agrupar mesmos) AGRUPAR OS QUE TEM 1 EM OUTROS
pais = dataset['Pais'].value_counts()
pais

# Estado (Agrupar mesmos) ARRUMAR NOMES E RENOMEAR "-"
est = dataset['Estado'].value_counts()
est

# Modelo do Tesla  ARRUMAR (TIRAR O ESPAÇO) NOMES E RENOMEAR "-"
mod = dataset['Modelo'].value_counts()
mod

# EXPLORAR COLUNAS NUMÉRICAS
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

# Quantas pessoas alegaram Piloto Automático #ajustar valores errados "-" e NANs
dataset['Alegado Piloto Automático'].describe()
srn.boxplot(dataset['Alegado Piloto Automático']
            ).set_title('Alegado Piloto Automático')
srn.histplot(dataset['Alegado Piloto Automático']
             ).set_title('Alegado Piloto Automático')

# procurar valores nulos (0)
dataset.isnull().sum()

# TRATAMENTO DE DADOS CATEGÓRICOS
# País. Agrupando os demais em outros e removendo os espaços
dataset['Pais'] = dataset['Pais'].str.strip()
dataset.loc[dataset['Pais'].isin(['Portugal', 'South Korea', 'Finland', 'Slovenia', 'Austria',
                                  'Ukraine', 'Spain', 'Mexico']), 'Pais'] = "Others"
pais = dataset['Pais'].value_counts()
pais
pais.plot.bar(color='gray')

# Estado. Agrupando os demais em outros e removendo os espaços e os '-'
dataset['Estado'] = dataset['Estado'].str.strip()
dataset.loc[dataset['Estado'] == '-', 'Estado'] = "Unknown"
est = dataset['Estado'].value_counts()
est
est.plot.bar(color='gray')

# Modelo do carro. Agrupando os demais em outros e removendo os espaços e os '-'
dataset['Modelo'] = dataset['Modelo'].str.strip()
dataset.loc[dataset['Modelo'] == '-', 'Modelo'] = "Unknown"
mod = dataset['Modelo'].value_counts()
mod
mod.plot.bar(color='gray')

# TRATAMENTO DE DADOS NUMERICOS
# Data. Transformando de String em Data
dataset['Data'] = pd.to_datetime(dataset['Data'].astype('datetime64[D]'))
dataset['Data'] = dataset['Data'].dt.date.astype('datetime64[D]')

# Motorista.
dataset['Motorista'] = dataset['Motorista'].str.strip()
dataset.loc[dataset['Motorista'] == '-', 'Motorista'] = "0"
dataset['Motorista'].fillna('0', inplace=True)

# Ocupante foi morto.
dataset['Ocupante'] = dataset['Ocupante'].str.strip()
dataset.loc[dataset['Ocupante'] == '-', 'Ocupante'] = "0"
dataset['Ocupante'].fillna('0', inplace=True)

# Em outro veiculo foi morto.
dataset['Outro'] = dataset['Outro'].str.strip()
dataset.loc[dataset['Outro'] == '-', 'Outro'] = "0"
dataset['Outro'].fillna('0', inplace=True)

# Pedestre foi morto
dataset['Pedestre'] = dataset['Pedestre'].str.strip()
dataset.loc[dataset['Pedestre'] == '-', 'Pedestre'] = "0"
dataset['Pedestre'].fillna('0', inplace=True)

# Alegado Piloto Automático
dataset['Alegado Piloto Automático'] = dataset['Alegado Piloto Automático'].str.strip()
dataset.loc[dataset['Alegado Piloto Automático']
            == '-', 'Alegado Piloto Automático'] = "0"
dataset['Alegado Piloto Automático'].fillna('0', inplace=True)

# ANÁLISE DOS DADOS
# Análise das mortes por direção automática da Tesla nos últimos 10 anos
plt.figure(figsize=(20, 8))
x = pd.DatetimeIndex(dataset['Data']).year.value_counts().sort_index().index
y = pd.DatetimeIndex(dataset['Data']).year.value_counts().sort_index().values
for i in range(len(x)):
    height = y[i]
    plt.text(x[i], height + 0.5, '%.1f' %
             height, ha='center', va='bottom', size=12)
plt.title("Número de acidentes por ano")
plt.xlabel("Anos")
plt.ylabel("Número de acidentes")
plt.bar(x, y, color='#e35f62')

# Análise das mortes por direção automática da Tesla por mes em 10 anos
plt.figure(figsize=(20, 8))
x = pd.DatetimeIndex(dataset['Data']).month.value_counts().sort_index().index
y = pd.DatetimeIndex(dataset['Data']).month.value_counts().sort_index().values
for i in range(len(x)):
    height = y[i]
    plt.text(x[i], height + 0.5, '%.1f' %
             height, ha='center', va='bottom', size=12)
plt.title("Número de mortes por mês durante 10 anos")
plt.xlabel("Meses")
plt.ylabel("Acidentes")
plt.bar(x, y, color='#e35f62')

# Análise das mortes por direção automática da Tesla por país
x = dataset["Pais"].value_counts().index
y = dataset["Pais"].value_counts().values
plt.figure(figsize=(20, 8))
for i in range(len(x)):
    height = y[i]
    plt.text(x[i], height + 0.25, '%.1f' %
             height, ha='center', va='bottom', size=12)
plt.bar(x, y, color='#e35f62')

# Análise das mortes por direção automática da Tesla por estado americano
x = dataset["Estado"].value_counts().index[1:]
y = dataset["Estado"].value_counts().values[1:]
plt.figure(figsize=(20, 8))
for i in range(len(x)):
    height = y[i]
    plt.text(x[i], height + 0.25, '%.1f' %
             height, ha='center', va='bottom', size=12)
plt.bar(x, y, color='#e35f62')

# Análise dos percentuais de mortes
x = dataset["Mortes"].astype('int').sum()
y = dataset["Motorista"].astype('int').sum()
z = dataset["Ocupante"].astype('int').sum()
a = dataset["Outro"].astype('int').sum()
b = dataset["Pedestre"].astype('int').sum()
c = x - (y+z+a+b)
labels = 'Carona', 'Motorista', 'Outro Carro', 'Pedestre', 'Desconhecido'
sizes = [z, y, a, b, c]
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
colors = ['#de4777', '#de4747', '#ae47de', '#de47ca', '#de47a7']
plt.figure(figsize=(9, 9))
plt.axis("equal")
plt.rc("font", family="Malgun Gothic")
plt.pie(sizes, labels=labels,  autopct="%.1f%%",
        pctdistance=0.85, colors=colors)
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.rc('legend', fontsize=11)
plt.legend()
plt.title("Total de mortes: " + str(x), fontsize=18)
plt.show()

# Análise dos modelos de tesla
x = dataset["Modelo"].value_counts().index[1:]
y = dataset["Modelo"].value_counts().values[1:]
plt.figure(figsize=(9, 7))
for i in range(len(x)):
    height = y[i]
    plt.text(x[i], height + 0.25, '%.1f' %
             height, ha='center', va='bottom', size=12)
plt.bar(x, y, color='#e35f62')
plt.title("Modelos de Tesla mais envolvidos", fontsize=15)

# Análise do número de pessoas que alegaram o piloto automatico ligado
size = dataset["Alegado Piloto Automático"].value_counts().values
color = ["darkmagenta", "deeppink", "hotpink"]
label = dataset["Alegado Piloto Automático"].value_counts().index
plt.figure(figsize=(12, 12))
plt.axis("equal")
plt.rc("font", family="Malgun Gothic")
plt.pie(size, labels=label, autopct="%.1f%%",
        pctdistance=0.85, colors=color, explode=(0, 0, 0.05))
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.rc('legend', fontsize=15)
plt.legend()
plt.title("Total de pessoas que alegaram Piloto Automático: " +
          str(len(dataset["Alegado Piloto Automático"])), fontsize=17)
plt.show()
