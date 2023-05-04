from projetin_xerox.datafreme.verificar_datafreme import salvar_datafreme
from os import getenv
import pandas as pd

def select_atualizar_planilhas(lista, df):
    caminho_arquivo = getenv("PLANILHA_PERCENTUAL")
    toner = pd.read_excel(caminho_arquivo, sheet_name='Toner')
    cilindro = pd.read_excel(caminho_arquivo, sheet_name='Cilindro')
    fusor = pd.read_excel(caminho_arquivo, sheet_name='Fusor')
    atualizar_planilha_toner(toner, df, lista)
    atualizar_planilha_cilindro(cilindro, df, lista)
    atualizar_planilha_fusor(fusor, df, lista)
    salvar_datafreme(toner, cilindro, fusor, caminho_arquivo)
    

def atualizar_planilha_toner(arquivo, df, porcentagem):
    for indice in range(0, len(df)):
        if type(porcentagem[indice][0]) == list:
            if porcentagem[indice][0][0] == 'Inacessível':
                arquivo['preto'] = porcentagem[indice][0][0]
            else:
                arquivo['preto'].loc[indice] = porcentagem[indice][0][0]
                arquivo['amarelo'].loc[indice] = porcentagem[indice][0][1]
                arquivo['magenta'].loc[indice] = porcentagem[indice][0][2]
                arquivo['ciano'].loc[indice] = porcentagem[indice][0][3]
        elif porcentagem[indice] == 'Função em andamento':
            arquivo['preto'].loc[indice] = porcentagem[indice]
        else:
            arquivo['preto'].loc[indice] = porcentagem[indice][0]
            if porcentagem == 'Inacessível':
                arquivo['amarelo'].loc[indice] =  ''
                arquivo['magenta'].loc[indice] =  ''
                arquivo['ciano'].loc[indice] =  ''


def atualizar_planilha_cilindro(arquivo, df, porcentagem):
    for indice in range(0, len(df)):
        if type(porcentagem[indice][1]) == list:
            if porcentagem[indice][1][0] == 'Maquina inacessível':
                arquivo['preto'] = porcentagem[indice][1][0]
            else:
                arquivo['preto'].loc[indice] = porcentagem[indice][1][0]
                arquivo['amarelo'].loc[indice] = porcentagem[indice][1][1]
                arquivo['magenta'].loc[indice] = porcentagem[indice][1][2]
                arquivo['ciano'].loc[indice] = porcentagem[indice][1][3]
        elif porcentagem[indice] == 'Função em andamento':
            arquivo['preto'].loc[indice] = porcentagem[indice]        
        else:
            arquivo['preto'].loc[indice] = porcentagem[indice][1]
            if porcentagem == 'Inacessível':
                arquivo['amarelo'].loc[indice] =  ''
                arquivo['magenta'].loc[indice] =  ''
                arquivo['ciano'].loc[indice] =  ''


def atualizar_planilha_fusor(arquivo, df, porcentagem):
    for indice in range(0, len(df)):
        if porcentagem[indice] == 'Função em andamento':
            arquivo['Fusor'].loc[indice] = porcentagem[indice]
        elif len(porcentagem[indice]) == 3:
            arquivo['Fusor'].loc[indice] = porcentagem[indice][2]