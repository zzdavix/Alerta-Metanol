import streamlit as st
import pandas as pd
from datetime import datetime
import os
import uuid
from chatbot import chatbot_component

chatbot_component()

if not os.path.exists('denuncias_imagens'):
    os.makedirs('denuncias_imagens')

CSV_FILE = 'denuncias.csv'

def salvar_denuncia(nome, endereco, descricao, imagem):
    denuncia_id = str(uuid.uuid4())

    nova_denuncia = {
        "id": [denuncia_id],
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "nome_estabelecimento": nome,
        "endereco": endereco,
        "descricao": descricao,
        "caminha_imagem": ["Nenhuma imagem enviada"]
    }

    if imagem is not None:
        id_curto = denuncia_id.split('-')[0]
        caminho_imagem = os.path.join("denuncias_imagens", f"{id_curto}_{imagem.name}")
        
        with open(caminho_imagem, "wb") as f:
            f.write(imagem.getbuffer())
        
        nova_denuncia["caminho_imagem"] = [caminho_imagem]

    df = pd.DataFrame(nova_denuncia)
    
    colunas_ordenadas = ["id", "timestamp", "nome_estabelecimento", "endereco", "descricao", "caminho_imagem"]
    df = df[colunas_ordenadas]

    df.to_csv(CSV_FILE, mode='a', header=not os.path.exists(CSV_FILE), index=False)

# --- INTERFACE DO USUÁRIO ---

st.title("Denuncie um Ponto de Venda Suspeito")
st.write("Sua denúncia é anônima e ajuda a vigilância sanitária a proteger a comunidade.")

with st.form(key="denuncia_form", clear_on_submit=True):
    st.subheader("Enviar Denúncia Anônima pelo Site")
    nome_estabelecimento = st.text_input("Nome do Estabelecimento (se souber)")
    endereco = st.text_area("Endereço ou Ponto de Referência")
    descricao = st.text_area("Descreva por que a bebida ou o local parece suspeito")
    foto_suspeita = st.file_uploader("Envie uma foto (opcional)", type=['jpg', 'png', 'jpeg'])

    submit_button = st.form_submit_button(label="Enviar Denúncia Anônima")

    if submit_button:
        salvar_denuncia(nome_estabelecimento, endereco, descricao, foto_suspeita)
        st.success("✅ Denúncia enviada com sucesso! Obrigado por sua colaboração.")
        st.balloons()

st.markdown("---")

# --- SEÇÃO ADICIONADA ---
st.header("Outros Canais de Denúncia (Paraíba)")
st.warning("Utilize os canais abaixo para denúncias formais diretamente aos órgãos competentes.")

st.subheader("AGEVISA (Agência Estadual de Vigilância Sanitária)")
st.markdown(
    """
    - **Site:** [agevisa.pb.gov.br/servicos/ouvidoria](http://agevisa.pb.gov.br/servicos/ouvidoria)
    - **Telefone (Ouvidoria):** (83) 98814-7935
    """
)

st.subheader("Centro de Inteligência Estratégica Estadual em Saúde da Paraíba")
st.markdown(
    """
    - **Telefone (Segunda a Sexta, 08h às 16h30):** (83) 99146-6771
    - **Telefone (Fins de semana e feriados):** (83) 98828-2522
    """
)

st.subheader("Autoridades Policiais")
st.info(
    "A venda de bebida adulterada é crime. Você pode acionar a Polícia para denunciar os locais de venda."
)