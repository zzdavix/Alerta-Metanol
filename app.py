import streamlit as st

# Configuração da página (título, ícone)
st.set_page_config(
    page_title="Alerta Metanol",
    page_icon="⚠️",
    layout="wide"
)

# Título e subtítulo
st.title("Alerta Metanol")
st.subheader("Saiba como se proteger do metanol, um veneno invisível que pode estar em bebidas de origem duvidosa.")

st.markdown("---") # Linha divisória

# Colunas para os botões de acesso rápido
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("COMO IDENTIFICAR UMA BEBIDA SEGURA", use_container_width=True):
        st.switch_page("pages/1_como_identificar.py")

with col2:
    if st.button("COMO SE PREVINIR", use_container_width=True):
        st.switch_page("pages/2_como_se_previnir.py")

with col3:
    if st.button("SINTOMAS DE ALERTA", use_container_width=True):
        st.switch_page("pages/3_sintomas_de_alerta.py")

st.write("") # Espaço entre as linhas de botões 
col4, col5 = st.columns(2)

with col4:
    if st.button("COMO AGIR EM SUSPEITA DE INTOXICAÇÃO", use_container_width=True):
        st.switch_page("pages/4_o_que_fazer.py")

with col5:
    if st.button("QUERO DENUNCIAR UM LOCAL", use_container_width=True):
        st.switch_page("pages/5_denuncie.py")

st.markdown("---")

# Você pode incorporar um vídeo do YouTube
st.header("Vídeo da Campanha")
st.video("https://www.youtube.com/watch?v=T-1PfgEMTPI")

st.info("Este é um site informativo desenvolvido pelo projeto PET-Saúde. Em caso de emergência, procure a unidade de saúde mais próxima.")