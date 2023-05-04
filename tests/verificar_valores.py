import pandas as pd
from os import getenv

df1 = pd.read_excel(getenv("PLANILHA_TESTE"))
df1 = df1.drop(1)
df2 = df1.copy()

with pd.ExcelWriter(getenv("PLANILHA_TESTE")) as writer: 
    df1.to_excel(writer, sheet_name=0, index=False)
    df2.to_excel(writer, sheet_name=1, index=False)