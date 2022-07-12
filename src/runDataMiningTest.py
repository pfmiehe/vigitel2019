

from posixpath import sep
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import xlrd
import os
import numpy as np

def funcRead(parametro):

    a ={ 1:"masculino", 2:"feminino"}
    b = {0: "sim", 1:"não"}
    parametro['sexo'] = parametro['sexo'].map(a)
    parametro['hipertensão arterial'] = parametro['hipertensão arterial'].map(b)

    #amostra de dados
    # print(parametro)

    # firsts information about dataframe
    # print(parametro.head())

    # print(parametro.describe())

    # print(parametro.groupby(['sexo']).agg(['max','min','median']))

    print(parametro[['hipertensão arterial', 'sexo']].value_counts())

    #novo com só o sexo
    print(parametro[['sexo']].value_counts())

    print(parametro[parametro['sexo']=='2'])

    print(parametro[['hipertensão arterial', 'sexo']].value_counts())

    print(parametro.columns.tolist())

    ## Manipulação de dados a partir de um dataframe
    parametro.rename(columns = {'Unnamed: 3':'cidade'}, inplace = True)
    parametro2 = parametro[['hipertensão arterial', 'sexo', 'cidade']]
    parametro2.fillna(0)

    ## Porto Alegre
    print(parametro2.loc[parametro['cidade']==17])

    ## Criação de arquivo a partir de manipulação de um dataframe 
    parametro2.to_csv('././output/teste.csv', sep=';')

    ## Plotar graficos 
    val1 = parametro2['hipertensão arterial'].value_counts()['sim']
    val2 = parametro2['hipertensão arterial'].value_counts()['não']

    X = ['HA Sim','HA Nao']
    Y = [val1, val2]

    y_pos = np.arange(len(X))

    # Create bars
    plt.bar(y_pos, Y)

    # Create names on the x-axis
    plt.xticks(y_pos, X)

    # Show graphic
    # plt.show()
    plt.savefig('././output/hipertensão_arterial.png')

    return 'ok'

if __name__ == '__main__':

    ## Carregamento de arquivo xls
    ##   - otimiza o tempo de carregamento do arquivo
    ##   - facilita o processo de impressão de dados
    df = pd.read_excel(r"././data/vigitel 2019 com colunas traduzidas.xls", skiprows=[0]) 

    x = funcRead(df)

    print(x)

