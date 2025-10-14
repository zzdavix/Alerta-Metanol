import streamlit as st
import pandas as pd
from datetime import datetime
import os
import uuid

if not os.path.exists('denuncias_imagens'):
    os.makedirs('denuncias_imagens')

CSV_FILE = 'denuncias.csv'

def salvar_denuncia(nome, endereco, descricao, imagem):
    denuncia_id = str(uuid.uuid4())  # Gera um ID único para cada denúncia

    nova_denuncia = {
        "id": [denuncia_id],
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "nome_estabelecimento": nome,
        "endereco": endereco,
        "descricao": descricao,
        "caminha_imagem": ["Nenhuma imagem enviada"]
    }

    # Se uma imagem foi enviada, salva ela e guarda o caminho
    if imagem is not None:
        # Gera um nome de arquivo único usando parte do ID da denúncia para fácil associação
        # Ex: denuncias_imagens/a1b2c3d4_minha_foto.jpg
        id_curto = denuncia_id.split('-')[0] # Pega a primeira parte do UUID
        caminho_imagem = os.path.join("denuncias_imagens", f"{id_curto}_{imagem.name}")
        
        with open(caminho_imagem, "wb") as f:
            f.write(imagem.getbuffer())
        
        nova_denuncia["caminho_imagem"] = [caminho_imagem]

    df = pd.DataFrame(nova_denuncia)
    
    # 3. Garanta que a ordem das colunas esteja correta
    colunas_ordenadas = ["id", "timestamp", "nome_estabelecimento", "endereco", "descricao", "caminho_imagem"]
    df = df[colunas_ordenadas]

    df.to_csv(CSV_FILE, mode='a', header=not os.path.exists(CSV_FILE), index=False)


# --- INTERFACE DO USUÁRIO (Permanece igual) ---

st.title("Denuncie um Ponto de Venda Suspeito")
st.write("Sua denúncia é anônima e ajuda a vigilância sanitária a proteger a comunidade.")

with st.form(key="denuncia_form", clear_on_submit=True):
    nome_estabelecimento = st.text_input("Nome do Estabelecimento (se souber)")
    endereco = st.text_area("Endereço ou Ponto de Referência")
    descricao = st.text_area("Descreva por que a bebida ou o local parece suspeito")
    foto_suspeita = st.file_uploader("Envie uma foto (opcional)", type=['jpg', 'png', 'jpeg'])

    submit_button = st.form_submit_button(label="Enviar Denúncia Anônima")

    if submit_button:
        # Chama a função para salvar os dados
        salvar_denuncia(nome_estabelecimento, endereco, descricao, foto_suspeita)
        
        st.success("✅ Denúncia enviada com sucesso! Obrigado por sua colaboração.")
        st.balloons()
