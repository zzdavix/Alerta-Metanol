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
        st.switch_page("pages/1_Como_Identificar.py")

with col2:
    if st.button("COMO SE PREVINIR", use_container_width=True):
        st.switch_page("pages/2_Como_se_Previnir.py")

with col3:
    if st.button("SINTOMAS DE ALERTA", use_container_width=True):
        st.switch_page("pages/3_Sintomas_de_Alerta.py")

st.write("") # Espaço entre as linhas de botões 
col4, col5 = st.columns(2)

with col4:
    if st.button("COMO AGIR EM SUSPEITA DE INTOXICAÇÃO", width="stretch"):
        st.switch_page("pages/4_O_Que_Fazer.py")

with col5:
    if st.button("QUERO DENUNCIAR UM LOCAL", width="stretch"):
        st.switch_page("pages/5_Denuncie.py")

st.markdown("---")

# Você pode incorporar um vídeo do YouTube
st.header("Vídeo da Campanha")
st.video("https://www.youtube.com/watch?v=T-1PfgEMTPI")

st.info("Este é um site informativo desenvolvido pelo projeto PET-Saúde. Em caso de emergência, procure a unidade de saúde mais próxima.")