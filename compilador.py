import pandas as pd
import os

with open('read_me.txt', 'r') as arq:
    print(arq.read())

print('Iniciando a rotina...')

print('Salva nome dos diretórios')
try:
    diretorio = {}
    diretorio['raiz'] = os.getcwd()
    diretorio['sources'] = os.getcwd() + '\\sources'
except:
    print('Erro ao salvar nome dos diretórios')


print('Alterando o endereço para o endereço dos arquivos de cotação')
try:
    os.chdir(diretorio['sources'])
except:
    print('Erro ao alterar o endereço para o endereço dos arquivos de cotação')


print('Cria DataFrame que vai comportar todos os arquivos extraídos')
try:
    dfs: tuple = []
except:
    print('Erro ao criar lista')

print('Incrementa todos os arquivos no DataFrame')
try:
    print('Arquivos:')
    for arquivo in os.listdir():
        print(f' - {arquivo}')
        if arquivo.endswith('.csv'):
            df = pd.read_csv(arquivo, sep=',')
            df['source'] = arquivo.replace(' - Dados Históricos.csv','')
            dfs.append(df)
except:
    print('Erro ao incrementar todos os arquivos no DataFrame')
       
print('Compila todos os DataFrames')
try:
    df_master = pd.concat(dfs)
except:
    print('Erro ao compilar todos os DataFrames')
        
print('Altera o endereço para o endereço mãe')
try:
    os.chdir(diretorio['raiz'])
except:
    print('Erro ao alterar o endereço para o endereço mãe')

print('Salva o arquivo no diretório')
try:
    df_master.to_csv('histórico ativos.csv')
except:
    print('Erro ao salvar o arquivo no diretório')
    
print('\a')
input('\nAperte ENTER para finalizar a rotina...')