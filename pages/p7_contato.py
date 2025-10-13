import streamlit as st
import pandas as pd
from datetime import datetime
import os
import uuid  # Importe a biblioteca UUID

# --- LÓGICA PARA SALVAR A MENSAGEM ---

# Nome do arquivo que vai guardar as mensagens de contato
CSV_FILE = "contatos.csv"

def salvar_contato(nome, email, mensagem):
    """Salva a mensagem de contato com um ID único em um arquivo CSV."""
    
    # Gera um ID único para o contato
    contato_id = str(uuid.uuid4())
    
    # Cria um dicionário com os dados do contato, incluindo o novo ID
    novo_contato = {
        "id": [contato_id],  # Adicionamos a nova coluna de ID
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "nome": [nome],
        "email": [email],
        "mensagem": [mensagem]
    }

    df = pd.DataFrame(novo_contato)

    # Garante que a ordem das colunas esteja correta
    colunas_ordenadas = ["id", "timestamp", "nome", "email", "mensagem"]
    df = df[colunas_ordenadas]

    # Salva no arquivo CSV, adicionando uma nova linha sem repetir o cabeçalho
    df.to_csv(CSV_FILE, mode='a', header=not os.path.exists(CSV_FILE), index=False)


# --- INTERFACE DO USUÁRIO ---
def show_page():
    # Configuração da página
    st.set_page_config(
        page_title="Contato - Alerta Metanol",
        page_icon="💌",
        layout="centered"
    )

    st.title("💌 Fale Conosco")

    # AVISO IMPORTANTE
    st.error(
        "**ATENÇÃO:** Este canal **NÃO** é para emergências médicas. "
        "Em caso de suspeita de intoxicação, procure imediatamente uma unidade de saúde "
        "ou acesse a aba **'O que Fazer?'**."
    )

    st.write(
        "Tem alguma dúvida sobre o projeto, sugestão, ou interesse em parcerias? "
        "Preencha o formulário abaixo e a equipe do PET-Saúde entrará em contato."
    )

    # Formulário de Contato
    with st.form(key="contact_form", clear_on_submit=True):
        nome_usuario = st.text_input("Seu Nome", placeholder="Digite seu nome completo")
        email_usuario = st.text_input("Seu E-mail", placeholder="seu.email@exemplo.com")
        mensagem_usuario = st.text_area("Sua Mensagem", height=150, placeholder="Escreva sua mensagem aqui...")

        submit_button = st.form_submit_button(label="Enviar Mensagem")

        if submit_button:
            if nome_usuario and email_usuario and mensagem_usuario:
                salvar_contato(nome_usuario, email_usuario, mensagem_usuario)
                st.success("✅ Mensagem enviada com sucesso! Agradecemos o seu contato.")
            else:
                st.warning("⚠️ Por favor, preencha todos os campos antes de enviar.")

    st.markdown("---")

    # Informações adicionais de contato
    st.subheader("Outros Canais")
    st.markdown(
        """
        **E-mail Institucional:** `contato.petsaude.ufpb@email.com` 
        *(Este é um e-mail de exemplo, substitua pelo e-mail real do projeto)*
        """
    )