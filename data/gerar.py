import pandas as pd
import os 


data = {
    'tituloProduto':['furadeira', 'parafusadeira'],
    'preco':[500, 250],
    'descricao':['Furar paredes', 'Parafusar coisas'],
    'imgProduto':['/images','/images'],
    'catProduto':['Ferramentas', 'Ferramentas'],
    'classProduto':['Manual','Manual'],
    'exibirHome':[True, False]
  }

data_frame = pd.DataFrame(data)

caminho_atual = os.getcwd()
caminho_final = caminho_atual.replace('\\', '/')

data_frame.to_csv(caminho_final+'/data/ferramentas.csv', index=False)