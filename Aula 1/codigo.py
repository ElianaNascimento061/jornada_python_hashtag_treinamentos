# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui
import time
import pandas
from pathlib import Path

#Dá uma pausa de 1 segundo entre os comandos para evitar travamento
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#Passo 1: Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

#Passo 2: Abrir o sistema da empresa
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4) #Dá uma pausa maior para o site carregar

#Passo 3: Fazer o login
pyautogui.click(x=772, y=407) #Seleciona o campo do email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #Tab pra ir pro próximo campo
pyautogui.write("minha senha muito muito dificil")
time.sleep(2)
pyautogui.doubleClick(x=673, y=568) #Clica no botao de login
time.sleep(4)

#Passo 4: Abrir a base de dados
pasta = Path(__file__).parent #Pega a pasta atual onde está o arquivo codigo.py, pois ele está na mesma pasta da tebela
tabela = pandas.read_csv(pasta / "produtos.csv")
print (tabela)

#Passo 5: Cadastrar produtos
for linha in tabela.index:
  #Clicar no campo de código
  pyautogui.click(x=525, y=293)
  #Pegar da tabela o valor do campo que a gente quer preencher
  codigo = str(tabela.loc[linha, "codigo"])
  #Preencher o campo
  pyautogui.write(codigo)
  #Passar para o proximo campo
  pyautogui.press("tab")
  #Marca
  marca = str(tabela.loc[linha, "marca"])
  pyautogui.write(marca)
  pyautogui.press("tab")
  #Tipo
  tipo = str(tabela.loc[linha, "tipo"])
  pyautogui.write(tipo)
  pyautogui.press("tab")
  #Categoria
  categoria = str(tabela.loc[linha, "categoria"])
  pyautogui.write(categoria)
  pyautogui.press("tab")
  #Preço Unitário
  preco_unitario = str(tabela.loc[linha, "preco_unitario"])
  pyautogui.write(preco_unitario)
  pyautogui.press("tab")
  #Custo
  custo = str(tabela.loc[linha, "custo"])
  pyautogui.write(custo)
  pyautogui.press("tab")
  #Observação
  obs = str(tabela.loc[linha, "obs"])
  if obs != "nan":
    pyautogui.write(obs) #Caso o obs seja um valor vazio o código não vai retornar nada e apenas pular para o próximo passo
  pyautogui.press("tab")
  pyautogui.press("enter")
  pyautogui.scroll(5000) #Volta para o início da tela

