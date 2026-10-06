#Passo a Passo do Sistema  de Vendas:
#1: Seção de cadastro de vendas: data, vendedor, produto, quantidade, valor e botã cadastrar - fica em uma barra lateral
#2: Seção de vendas cadastradas: tabela com as vendas
#3: Seção do dashboard: card/métrica com o faturamento total, gráfico de barras para vendas por vendedor e um gráfico de pizza de venda por produto

import streamlit as st
import pandas as pd
import plotly.express as px

#Carregar base de vendas
tabela_vendas = pd.read_csv ("vendas.csv")

#Título
st.write("# Sistema de Vendas")

#Seção cadastrar vendas
st.sidebar.write("## Cadastrar Vendas") #sidebar coloca tudo em uma barra lateral
data = st.sidebar.date_input ("Data")
vendedor = st.sidebar.selectbox ("Vendendor", ["Ana", "Bruna", "Carla"])
produto = st.sidebar.selectbox ("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input ("Quantidade", step=1) #step=1 serve pra deixar em número inteiro
valor = st.sidebar.number_input ("Valor")
botao_cadastrar = st.sidebar.button ("Cadastrar venda")

#Lógica do cadastrar
if botao_cadastrar:
  if valor <= 0 or quantidade <= 0:
    st.warning("Preencha todos os campos!!")
  else:
    nova_venda = [str(data), vendedor, produto, quantidade, valor] #Str transforma data em texto, pois o pandas le como texto mas o streamlit já consegue converter pra data
    ultima_linha = len(tabela_vendas) #Mostra o tamanho da tabela
    tabela_vendas.loc[ultima_linha] = nova_venda #Adiciona a nova venda na última linha
    tabela_vendas.to_csv("vendas.csv", index=False) #Atualiza o banco de dados, o index=false serve pra não salvar o índice
    print(nova_venda)
    st.success("Venda cadastrada!!") #Mensagem de quando uma ação foi realizada com sucesso

#Seção vendas cadastradas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas) #Tabela do panda que formata o dados de forma diferente e possui várias funcionalidades

#Seção dashboard
st.write("## Dashboard")
#Faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento}")

#Gráfico de barras - vendas por vendedor
grafico1 = px.bar(tabela_vendas, x = "vendedor", y = "valor", color= "produto")
st.plotly_chart(grafico1) #Para o gráfico aparecer no sistema precisa do st
#Gráfico de pizza - venda por produto
grafico2 = px.pie(tabela_vendas, names= "produto", values= "valor", hole= 0.5) #hole transforma o gráfico de pizza em um gráfico de rosquinha
st.plotly_chart(grafico2)