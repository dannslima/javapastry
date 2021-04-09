import pandas as pd
from tkinter.filedialog import askopenfile
from tkinter import Tk, filedialog
import numpy as np
import pyodbc
from tkinter import *
from tkinter import ttk , messagebox
import win32con
import sys
import ctypes
from ctypes import wintypes
import win32con
byref = ctypes.byref
user32 = ctypes.windll.user32
import os.path
import os
from datetime import date

#FAZENDO A CONEXÃO COM BANDO DE DADOS
server = 'TERMINAL-19'
database = 'Producao_JavaPastry'
username = 'grupopi'
password = 'grupopi'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor ()

#criar Nossa Janela
jan=Tk()
jan.title('DANILO VASCONCELOS')
jan.geometry('500x300')
jan.configure(background = 'White')
jan.resizable(width=False, height=False)
#jan.iconbitmap(default='iconBeakt.png')

# CARREGANDO IMAGENS
#ogo = PhotoImage(file='iconBeakt.png')
#logo2 = PhotoImage(file='fundo.png')
#fundodireito = PhotoImage(file='fundodireito.png')

LeftFrame = Frame(jan, width=500, height=300, bg='#483D8B', relief='raise')
LeftFrame.pack (side=LEFT)

LogoLabel = Label(LeftFrame, image='', bg='BLACK')
LogoLabel.place(x=60, y=30)

#FUNÇÕES PARA OS BOTOES

def importar_arquivo():
    filename = filedialog.askopenfilename()
    df = pd.read_csv(str(filename), sep=';')
    df.columns = df.columns.str.lstrip()  # TIRANDO OS ESPAÇOS NA ESQUERDA
    df.columns = df.columns.str.rstrip()  # TIRANDO OS ESPAÇOS NA DIREITA
    print(f' {filename}  caminho do arquivo')
    messagebox.showinfo(title='Sucesso' , message='CARREGADO COM SUCESSO')
    lb= Label(jan , text= filename)
    lb.place(x=170, y=260)
    return df

def criar_banco():
    cursor.execute( '''
        CREATE TABLE sicar_info (car varchar(200) , area varchar(50), uf varchar(15) ,
         mun varchar(20), modulo_fiscal varchar (100),tipo_imovel varchar (100),
         situacao varchar(200), condicao varchar(500) , data_importacao datetime)''')
    conn.commit()

def popular_banco():
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')
    print(data_em_texto)
    df = importar_arquivo()
    for index, row in df.iterrows():
        print('insert do banco')
        print(index, row)
        cursor.execute('''
                          INSERT INTO Producao_JavaPastry.dbo.sicar_info (
                          car, area, uf, mun, modulo_fiscal, tipo_imovel, situacao,condicao,data_importacao )                
                          VALUES (?,?,?,?,?,?,?,?,?)
                                      ''',
                          row.car, row.area, row.uf, row.mun, row.modulo_fiscal, row.tipo_imovel, row.situacao,
                          row.condicao,
                          data_em_texto)
    conn.commit()
    cursor.close()
    messagebox.showinfo(title='SUCESSO' , message='INSERIDO NO BANCO')


#Botoes

ImportButton = ttk.Button(LeftFrame, text='IMPORTAR PLANILHA',width=24,command=importar_arquivo)
ImportButton.place(x=170, y=200)
SalvarButton = ttk.Button(LeftFrame, text='SALVAR',width=24,command=popular_banco)
SalvarButton.place(x=170, y=150)


print('fim')
#FAZENDO A LEITURA DO ARQUIVO CSV



# CRIANDO O BANCO DE DADOS , DEVE SER RODADO APENAS UMA VEZ
#

#PERCORRENDO TODAS AS COLUNAS E LINHAS INDEX > COLUNAS  E ROWS > A LINHA (CELULA)

jan.mainloop()
