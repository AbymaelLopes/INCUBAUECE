import pandas as pd

# Filtro para somar valores existentes passando o dataframe, a coluna e o filtro
def filtro_simples(dataframe, valor_filtrado, coluna):
    dataframe = dataframe[coluna].isin(valor_filtrado).sum()
    return dataframe

# Importação das bases de bases_de_dados
df_cerne_1 = pd.read_excel('bases_de_dados/Entradas - Cerne.xlsx')
df_trilha_empreendedor = pd.read_excel('bases_de_dados/Entradas - Trilha do Empreendedor.xlsx')
df_financeiro = pd.read_excel('bases_de_dados/Entradas - Financeiro.xlsx')
df_equipe = pd.read_excel('bases_de_dados/Entradas - Equipe.xlsx')

# Remoção de espaços laterais e remoção de valores nulos na coluna especificada
def tratamento(dataframe, coluna):
    dataframe.columns = dataframe.columns.astype(str).str.strip() # Remove espaços laterais dos nomes das colunas
    dataframe.drop(columns=['Eixo do CERNE 2', 
    'Eixo do CERNE 3', 
    'Prática Cerne 2',
    'Prática Cerne 3',
    'Evidência Cerne 2',
    'Evidência Cerne 3'
    ], inplace=True, errors='ignore') # Remove colunas desnecessárias para o relatório, se existirem
    dataframe[coluna] = dataframe[coluna].astype(str).str.strip() # Remove espaços laterais dos valores da coluna especificada
    if coluna == 'Eixo do CERNE 1':
        dataframe = dataframe.dropna(subset=[coluna])
        dataframe = dataframe[dataframe[coluna] != 'nan'] # Remove valores nulos ou 'nan' da coluna especificada
        dataframe[coluna] = dataframe[coluna].str.replace(r'\r?\n', '', regex=True) # Remove quebras de linha dos valores da coluna especificada
    return dataframe

# Dataframe Tratado Entrada - CERNE 1
df_cerne_1 = tratamento(df_cerne_1, 'Eixo do CERNE 1')

# Função que realiza filtros em diversas colunas ao mesmo tempo
def filtrar(df, filtros):
    
    resultado = df.copy()
    for coluna, valor in filtros.items():
        if isinstance(valor, list):
            resultado = resultado[resultado[coluna].isin(valor)]
        else:
            resultado = resultado[resultado[coluna] == valor]
    return resultado

# Contagem de empresas 'propostas submetidas'
df_propostas_submetidas = pd.read_excel('bases_de_dados/Entrada - Contagem de Empresas.xlsx', sheet_name='Propostas Submetidas', header=1)
df_propostas_submetidas.rename(columns={'Unnamed: 0': 'Ano'}, inplace=True)

# Contagem de empresas 'Empresas'

def empresas_tratado(sheet_planilha):
    df_empresas = pd.read_excel('bases_de_dados/Entrada - Contagem de Empresas.xlsx', sheet_name=sheet_planilha, header=1)

    df_empresas.rename(columns={'Unnamed: 0': 'Ano', 'Unnamed: 3': 'Pré-incubação', 'Unnamed: 4': 'Pré-incubação','Unnamed: 5': 'Pré-incubação','Unnamed: 6': 'Pré-incubação','Unnamed: 7': 'Pré-incubação','Unnamed: 8': 'Pré-incubação','Unnamed: 9': 'Pré-incubação','Unnamed: 10': 'Pré-incubação', 'Unnamed: 11': 'Incubação', 'Unnamed: 12': 'Incubação', 'Unnamed: 13': 'Incubação', 'Unnamed: 14': 'Incubação', 'Unnamed: 15': 'Incubação', 'Unnamed: 16': 'Associação', 'Unnamed: 17': 'Associação', 'Unnamed: 18': 'Associação'}, inplace=True)

    colunas = ['Pré-incubação', 'Incubação', 'Associação']

    df_long = df_empresas.melt(
        id_vars=['Ano', 'Mês'],
        value_vars=colunas,
        var_name='Modalidade',  # O nome da coluna que receberá os cabeçalhos ('Pré-incubação', 'Incubação', 'Associação')
        value_name='Empresa'   # O nome da coluna que receberá os valores (os nomes das empresas)
    )

    df_empresas_final = df_long.dropna(subset=['Empresa'])
    return df_empresas_final

empresas_tratado('Empresas')
empresas_tratado('Graduação')