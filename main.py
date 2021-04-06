import pandas as pd
import numpy as np
import pyodbc
import tkinter

#FAZENDO A CONEXÃO COM BANDO DE DADOS
server = 'azuredanilo.database.windows.net'
database = 'Producao_JavaPastry'
username = 'naruto'
password = 'Dann@0309'
conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor ()

#FAZENDO A LEITURA DO ARQUIVO CSV

df = pd.read_csv ('D:/Downloads/teste.csv', sep=';')
print(df.head())
df.columns = df.columns.str.lstrip()  # TIRANDO OS ESPAÇOS NA ESQUERDA
df.columns = df.columns.str.rstrip()  # TIRANDO OS ESPAÇOS NA DIREITA

# CRIANDO O BANCO DE DADOS , DEVE SER RODADO APENAS UMA VEZ
#cursor.execute ('CREATE TABLE sicar_info (car varchar(200) , area varchar(50), uf varchar(15) , mun varchar(20), modulo_fiscal varchar (100), tipo_imovel varchar (100), situacao varchar(200), condicao varchar(500))')

#PERCORRENDO TODAS AS COLUNAS E LINHAS INDEX > COLUNAS  E ROWS > A LINHA (CELULA)
for index, row in df.iterrows():
        print(index, row)

        cursor.execute('''
                        INSERT INTO Producao_JavaPastry.dbo.sicar_info (
                        car, 
                        area, 
                        uf,
                        mun,
                        modulo_fiscal,
                        tipo_imovel,
                        situacao,
                        condicao
                                     )                
                        VALUES (?,?,?,?,?,?,?,?)
                        ''',
                       row.car,
                       row.area,
                       row.uf,
                       row.mun,
                       row.modulo_fiscal,
                       row.tipo_imovel,
                       row.situacao,
                       row.condicao
                       )

conn.commit()
cursor.close()

