#Passo a passo para criar o Chatbot
#1: Campo de mensagem (input)
#2: Quando o usuário enviar a mensagem
  #2.1: Mostrar a mensagem
  #2.2: Mandar a mensagem para a IA responder
  #2.3: Mostrar a mensagem da IA
#Ferramentas: streamlit (cria o sistema e os elementos do chatbot) e openAI
#Para rodar o código: ir no terminal e digitar streamlit run + nome do arquivo

import streamlit as st
import os #Permite acessar variávis de ambiente
from dotenv import load_dotenv
from openai import OpenAI #A biblioteca openai possui várias ferramentas

#Carrega as variáveis do arquivo .env
load_dotenv()
#Recupera a chave do Gemini
api_key = os.getenv("GEMINI_API_KEY")
#Verifica se a chave foi configurada
if not api_key:
  st.error("Configure a GEMINI_API_KEY no arquivo .env")
  st.stop()

#Conecta com a API do Gemini
modelo_ia = OpenAI(api_key= api_key,
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai") #A base_url serve pois o gemini não pertence à openai

st.write("## ChatBot de IA") #Colocar hashtag dentro das aspas deixa o texto maior - maior a quantidade de hashtag menor o texto
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui") #Campo pro usuário inserir a informação

#Cria o histórico de mensagens
if not "lista_mensagens" in st.session_state: #session_state é a memória do streamlit
  st.session_state["lista_mensagens"] = []

#Percorre a lista de mensagens e exibe todas elas
for mensagem in st.session_state["lista_mensagens"]:
  quem_enviou = mensagem['role']
  texto_mensagem = mensagem['content']
  st.chat_message(quem_enviou).write(texto_mensagem)

if mensagem_usuario:
  #Exibir a mensagem na tela
  st.chat_message("user").write(mensagem_usuario) # st.chat_message(quem tá mandando (user ou assistant)).write(mensagem do usuário)
  mensagem1 = {'role':'user', 'content':mensagem_usuario}
  st.session_state["lista_mensagens"].append(mensagem1) #Adiciona a mensagem na lista

  #Pegar a mensagem da IA
  #chat - manda o histórico de mensagens para que a ia possa entender o contexto
  #completion - complementa a resposta
  resposta_modelo = modelo_ia.chat.completions.create(
    messages = st.session_state["lista_mensagens"],
    model = "gemini-flash-lite-latest" #latest pega o último modelo
  )
  resposta_ia = resposta_modelo.choices[0].message.content
  print(resposta_modelo)
  mensagem2 = {'role':'assistant', 'content':resposta_ia}
  st.session_state["lista_mensagens"].append(mensagem2)
  #Exibir a mensagem da IA no chat
  st.chat_message("assistant").write(resposta_ia)
