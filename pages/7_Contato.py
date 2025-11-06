import streamlit as st
# import pandas as pd  <-- REMOVIDO
import psycopg2          # <-- ADICIONADO (para o Neon)
from datetime import datetime
import os
import uuid
from chatbot import chatbot_component

chatbot_component()

# --- FUNÇÕES DE CONEXÃO AO BANCO DE DADOS (NEON) ---
# Esta função é idêntica à da página 5_Denuncie.py

def get_db_conn():
    """Retorna uma nova conexão com o banco de dados PostgreSQL usando a URL dos secrets."""
    try:
        conn_string = st.secrets["db_url"]
        conn = psycopg2.connect(conn_string)
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def init_db_contato():
    """Cria a tabela 'contatos' se ela não existir."""
    conn = get_db_conn()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS contatos (
                        id UUID PRIMARY KEY,
                        timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        nome VARCHAR(255),
                        email VARCHAR(255),
                        mensagem TEXT
                    );
                """)
            conn.commit()
        except Exception as e:
            st.error(f"Erro ao inicializar a tabela de contatos: {e}")
        finally:
            if conn:
                conn.close()

# --- LÓGICA ATUALIZADA PARA SALVAR A MENSAGEM ---
# REMOVIDO: CSV_FILE = "contatos.csv"

def salvar_contato(nome, email, mensagem):
    """Salva a mensagem de contato com um ID único no banco de dados PostgreSQL."""
    
    contato_id = uuid.uuid4()
    conn = None
    
    try:
        conn = get_db_conn()
        if conn is None:
            raise Exception("Não foi possível conectar ao banco de dados.")
            
        with conn.cursor() as cur:
            # O timestamp será preenchido automaticamente pelo banco (DEFAULT CURRENT_TIMESTAMP)
            sql = """
                INSERT INTO contatos (id, nome, email, mensagem)
                VALUES (%s, %s, %s, %s)
            """
            # Converte UUID para string para o psycopg2
            cur.execute(sql, (str(contato_id), nome, email, mensagem))
        
        conn.commit()
        st.success("✅ Mensagem enviada com sucesso! Agradecemos o seu contato.")

    except Exception as e:
        st.error(f"Erro ao salvar mensagem: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()


# --- INTERFACE DO USUÁRIO (Baseada no seu arquivo original) ---

# Roda a verificação da tabela ao carregar
init_db_contato()

# Configuração da página
st.set_page_config(
    page_title="Contato - Alerta Metanol",
    page_icon="✉️",
    layout="wide"
)

st.title("Fale Conosco")

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
            # A mensagem de sucesso agora é chamada de dentro de salvar_contato()
            salvar_contato(nome_usuario, email_usuario, mensagem_usuario)
        else:
            st.warning("⚠️ Por favor, preencha todos os campos antes de enviar.")

st.markdown("---")

# Informações adicionais de contato
st.subheader("Outros Canais")
st.markdown(
    """
    **E-mail Institucional:** `contatopet.gt09@gmail.com` 
    """
)