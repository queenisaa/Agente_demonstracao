import streamlit as st
import requests
# from Memoria import PersistentMemory

#Configuração inicial
st.set_page_config(page_title= "Chat AI MindStudios - GPT-4-Mini", layout= "centered")
st.title("Chat com MindStudio")

# Inicialize uma vez por sessão a memoria
# memory = PersistentMemory('meu_app_memory.json')

#Iniciar Historico de Mensagens 
if "messages" not in st.session_state:
      st.session_state.messages = []

if "casos_usados" not in st.session.state:
      st.session_state.casos_usados = []

#Configuração da API
API_KEY = "sk7bNzmTUXlukUUGgQYGmu6KCowcMCqEiMQSOUiuAECg2og6yq0SAAeyywCKGiEoc4AUwY2g6oyaICgAQqAqyIiG"
APP_ID = "d8b32ac4-6ddd-410a-b986-a25aba677368"
API_URL = "https://api.mindstudio.ai/developer/v2/apps/run"

#Entrada do Usuario
user_input = st.chat_input("Escreva sua mensagem...")

if user_input and user_input.strip() != "":
    #Historico de Mensagem
     st.session_state.messages.append(("user", user_input))

historico = "\n".join(f"- {item}" for item in st.session_state.casos_usados)
    
    #preparando headers e payload
headers = {
          "Authorization": f"Bearer  {"sk7bNzmTUXlukUUGgQYGmu6KCowcMCqEiMQSOUiuAECg2og6yq0SAAeyywCKGiEoc4AUwY2g6oyaICgAQqAqyIiG"}",
          "Content-Type": "application/json"
      }
    
    #Deixando explicito o modelo de AI
payload = { 
          "appId": "d8b32ac4-6ddd-410a-b986-a25aba677368",
          "variables": {
              "user_input": user_input,
              "model": "gpt-4-mini",
              "historico_uso": historico
          }
      }
    
    #Mandando request pro mindstudio
with st.spinner("Processando"):
          response = requests.post("https://api.mindstudio.ai/developer/v2/apps/run", headers=headers, json=payload)
    
if response.status_code == 200:
        resposta = response.json().get("outputs", "Sem resposta.")
        with st.chat_message("assistant"):
            st.markdown(resposta)
else:
        st.error(f"Erro {response.status_code}: {response.text}")

#Mostrar historico
for role, msg in st.session_state.messages:
      if role == "user":
          with st.chat_message("user"):
              st.markdown(msg)
      else:
          with st.chat_message("assistant"):
              st.markdown(msg)

with st.expander("Casos de Uso Anteriores nesta Sessão:"):
    for caso in st.session_state.casos_usados:
        st.markdown(f"- {caso}") 

# Use em qualquer lugar do código
# memory['contador'] = memory.get('contador', 0) + 1