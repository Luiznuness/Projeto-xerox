from os import getenv
import pandas as pd 

def drop_all_colunms(df):
    for c in range(0, len(df)):
        df = df.drop(c)
    return df

def modificar_info(new, df):
    df = drop_all_colunms(df)
    df[['Ip', 'Modelos', 'Departamento', 'Andar']] = new
    if new.equals(df[['Ip', 'Modelos', 'Departamento', 'Andar']]) == True:
        return df

def salvar_datafreme(toner, cilindro, fusor, caminho):
    with pd.ExcelWriter(caminho) as writer:
        toner.to_excel(writer, sheet_name='Toner', index=False)
        cilindro.to_excel(writer, sheet_name='Cilindro', index=False)
        fusor.to_excel(writer, sheet_name='Fusor', index=False)

def abrir_datafremes(new, toner, caminho):
    toner = modificar_info(new, toner)

    cilindro = pd.read_excel(caminho, sheet_name=1)
    cilindro = modificar_info(new, cilindro)

    fusor = pd.read_excel(caminho, sheet_name=2)
    fusor = modificar_info(new, fusor)
    salvar_datafreme(toner, cilindro, fusor, caminho)

def verificar_datafreme(df1):
    caminho_df_percentual = getenv("PLANILHA_PERCENTUAL")
    toner = pd.read_excel(caminho_df_percentual)
    if df1[['Ip', 'Modelos', 'Departamento', 'Andar']].equals(toner[['Ip', 'Modelos', 'Departamento', 'Andar']]) == False:
        new = df1[['Ip', 'Modelos', 'Departamento', 'Andar']]
        lista = abrir_datafremes(new, toner, caminho_df_percentual)
        salvar_datafreme(lista[0], lista[1], lista[2], caminho_df_percentual)