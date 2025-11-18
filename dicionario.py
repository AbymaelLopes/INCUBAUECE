import pandas as pd
import dados
from num2words import num2words
import os
os.system('cls')

# Gerar número por extenso
def extenso(numero):
    try:
        return num2words(numero, lang='pt_BR')
    except Exception as e:
        return f"Erro ao converter: {e}"

# Importação e tratamento das bases de dados
dados.tratamento(dados.df_cerne_1, 'Tipo de Entrada')
dados.tratamento(dados.df_cerne_1, 'Observação')
dados.df_cerne_1['Prática Cerne 1'] = dados.df_cerne_1['Prática Cerne 1'].str.replace('x', 'X')

df_trilha_empreendedor = dados.df_trilha_empreendedor
df_trilha_empreendedor['Semestre de Entrada'] = df_trilha_empreendedor['Semestre de Entrada'].str.replace('º', '')

df_financeiro = dados.df_financeiro
df_financeiro = df_financeiro.dropna()
df_financeiro = df_financeiro.copy()  # Adicione isto antes de modificar
df_financeiro['Semestre'] = df_financeiro['Semestre'].str.replace('º', '')

df_contagem_graduacao = dados.empresas_tratado('Graduação')
df_contagem_graduacao['Semestre'] = df_contagem_graduacao['Mês'].apply(lambda x: 1 if x <= 6 else 2)
df_contagem_empresas = dados.empresas_tratado('Empresas')
df_contagem_propostas = dados.df_propostas_submetidas
df_contagem_propostas['Semestre'] = df_contagem_propostas['Mês'].apply(lambda x: 1 if x <= 6 else 2)

dados.df_equipe['Semestre'] = dados.df_equipe['Semestre'].str.replace('º', '')

# Pegar apenas digito da coluna de tempo de execução
def digito(texto):
    digito = texto
    numeros = digito.str.split(' ').str[0].astype(int).tolist()
    soma = sum(numeros)
    return soma

# Criação do dicionário com as variáveis base
variaveis = {
    'varSemestre': 1,
    'varAno': 2024,
}

# Implementação das demais variáveis 
variaveis['var1'] = variaveis['varSemestre']

variaveis['var2'] = (dados.filtrar(dados.df_cerne_1, {'Eixo do CERNE 1': 'Sensibilização'}).shape[0])

variaveis['var3'] = (dados.filtrar(dados.df_cerne_1, {'Eixo do CERNE 1': 'Sensibilização'})['Pessoas Impactadas'].sum())

variaveis['var4'] = 'valor 2'

variaveis['var5'] = dados.filtrar(dados.df_cerne_1, {'Eixo do CERNE 1': 'Prospecção'}).shape[0]

variaveis['var6'] = dados.filtrar(dados.df_cerne_1, {'Eixo do CERNE 1': 'Sensibilização / Qualificação de Potenciais Empreendedores', 'Tipo de Entrada': 'Oficina'}).shape[0]

variaveis['var7'] = digito(dados.filtrar(dados.df_cerne_1, {'Eixo do CERNE 1': 'Sensibilização / Qualificação de Potenciais Empreendedores', 'Tipo de Entrada': 'Oficina'})['Tempo de Execução'])

variaveis['var8'] = int(dados.filtrar(dados.df_cerne_1, {'Eixo do CERNE 1': 'Sensibilização / Qualificação de Potenciais Empreendedores', 'Tipo de Entrada': 'Oficina'})['Pessoas Impactadas'].sum())

variaveis['var9'] = dados.filtrar(df_trilha_empreendedor, {'Semestre de Entrada': str(variaveis['varSemestre']), 'Ano': variaveis['varAno']}).shape[0]

variaveis['var10'] = variaveis['varSemestre']

variaveis['var11'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Pré-incubação'].sum() + dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Incubação'].sum() + dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Associação'].sum()

variaveis['var12'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Pré-incubação'].sum()

variaveis['var13'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Incubação'].sum()

variaveis['var14'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Associação'].sum()

variaveis['var15'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Termo de Compromisso Assinado'].sum() + dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Contrato de Incubação Assinado'].sum() + dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Contrato de Associação Assinado'].sum()

variaveis['var16'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Termo de Compromisso Assinado'].sum()

variaveis['var17'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Contrato de Incubação Assinado'].sum()

variaveis['var18'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Contrato de Associação Assinado'].sum()

variaveis['var19'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Contrato de Incubação Assinado'].sum()

variaveis['var20'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Contrato de Associação Assinado'].sum()

variaveis['var21'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Termo de Compromisso Assinado'].sum()

variaveis['var22'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Contrato de Incubação Assinado'].sum()

variaveis['var23'] = dados.filtrar(df_contagem_propostas, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno']})['Termo de Compromisso Assinado'].sum()

variaveis['var24'] = dados.filtrar(dados.df_cerne_1, {'Prática Cerne 1': 'X', 'Tipo de Entrada': ['Oficina', 'Curso', 'Aula']}).shape[0]

variaveis['var25'] = dados.filtrar(dados.df_cerne_1, {'Prática Cerne 1': 'X', 'Tipo de Entrada': 'Mentoria'}).shape[0]

variaveis['var26'] = dados.filtrar(dados.df_cerne_1, {'Prática Cerne 1': 'X', 'Tipo de Entrada': 'Reunião'}).shape[0]

variaveis['var27'] = dados.filtrar(dados.df_cerne_1, {'Prática Cerne 1': 'X', 'Tipo de Entrada': 'Atendimento'}).shape[0]

variaveis['var28'] = dados.filtrar(dados.df_cerne_1, {'Prática Cerne 1': 'X'}).shape[0]

variaveis['var29'] = dados.filtrar(dados.df_cerne_1, {'Prática Cerne 1': 'X', 'Tipo de Entrada': 'Mentoria', 'Observação': ['Incubação', 'Pré-incubação']}).shape[0]

variaveis['var30'] = 'valor 2'
variaveis['var31'] = 'valor 2'
variaveis['var32'] = 'valor 2'
variaveis['var33'] = 'valor 2'

variaveis['var34'] = variaveis['varSemestre']

variaveis['var35'] = dados.filtrar(df_contagem_graduacao, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno'], 'Modalidade': ['Incubação', 'Associação']}).shape[0]

variaveis['var36'] = dados.filtrar(df_contagem_graduacao, {'Semestre': variaveis['varSemestre'], 'Ano': variaveis['varAno'], 'Modalidade': 'Pré-incubação'}).shape[0]

variaveis['var37'] = dados.filtrar(dados.df_cerne_1, {'Prática Cerne 1': 'X', 'Tipo de Entrada': 'Mentoria'}).shape[0]

variaveis['var38'] = 'valor 2'

variaveis['var39'] = dados.filtrar(dados.df_cerne_1, {'Prática Cerne 1': 'X', 'Observação': ['Incubação']}).shape[0]

variaveis['var49'] = 'valor 2'
variaveis['var41'] = 'valor 2'
variaveis['var42'] = dados.filtrar(dados.df_equipe, {'Semestre': str(variaveis['varSemestre']), 'Ano': variaveis['varAno']})['Equipe Total'].sum()

variaveis['var43'] = variaveis['varSemestre']

variaveis['var44'] = dados.filtrar(df_financeiro, {'Ano': variaveis['varAno'], 'Semestre': str(variaveis['varSemestre'])})['Receitas com Programas de Incubação'].sum() + dados.filtrar(df_financeiro, {'Ano': variaveis['varAno'], 'Semestre': str(variaveis['varSemestre'])})['Outras receitas advindas da UECE'].sum()

variaveis['var45'] = extenso(variaveis['var44'])

variaveis['var46'] = dados.filtrar(df_financeiro, {'Ano': variaveis['varAno'], 'Semestre': str(variaveis['varSemestre'])})['Despesas'].sum()

variaveis['var47'] = extenso(variaveis['var46'])
variaveis['var48'] = 'valor 2'
variaveis['var49'] = 'valor 2'
variaveis['var50'] = 'valor 2'
variaveis['var51'] = 'valor 2'
variaveis['var52'] = 'valor 2'
variaveis['var53'] = dados.filtrar(dados.df_cerne_1, {'Eixo do CERNE 1': 'Sensibilização / Qualificação de Potenciais Empreendedores', 'Tipo de Entrada': 'Oficina'})['Entrada']

variaveis['var54'] = 'Valor 2'

variaveis['var55'] = dados.filtrar(dados.df_cerne_1, {'Prática Cerne 1': 'X', 'Tipo de Entrada': 'Mentoria'})['Entrada']

print(variaveis)