import streamlit as st
from chatbot import chatbot_component

chatbot_component()

st.set_page_config(
    page_title="Alerta Metanol",
    page_icon="⚠️",
    layout="wide"
)

st.title("Como Identificar Bebidas Seguras")
st.markdown("Fique atento a estes sinais:")

st.warning(
    "**ATENÇÃO:** O metanol **NÃO altera o cheiro, a cor ou o sabor** da bebida. "
    "Não confie nos seus sentidos para saber se é seguro!"
)

st.markdown("---")
# Usando colunas para comparar o certo e o errado
col1, col2 = st.columns(2)

with col1:
    st.subheader("❌ SUSPEITO")
    st.image("images/lacre_violado.jpg", caption="Lacre violado.")
    with st.container(border=True):
        st.markdown("❌ :red[**LACRE/TAMPA:**] Rompido, frouxo ou com cola aparente.")

    st.markdown("---")

    st.subheader("❌ SUSPEITO")
    st.image("images/rotulo_sujo2.jpg", caption="Rótulo desgastado.")
    with st.container(border=True):
        st.markdown("❌ :red[**RÓTULO:**] Sujo, rasgado ou mal colado.")

    st.markdown("---")

    st.subheader("❌ SUSPEITO")
    st.image("images/liquido_adulterado.jpg", caption="Líquido adulterado.")
    with st.container(border=True):
        st.markdown("❌ :red[**LÍQUIDO:**] Com partículas, turvo ou com cor incomum.")


with col2:
    st.subheader("✅ SEGURO")
    st.image("images/lacre_selado.jpg", caption="Lacre intacto.")
    with st.container(border=True):
        st.markdown("✅ :green[**LACRE/TAMPA:**] Intacto, sem sinais de violação.")

    st.markdown("---")

    st.subheader("✅ SEGURO")
    st.image("images/rotulo_limpo2.jpg", caption="Rótulo limpo")
    with st.container(border=True):
        st.markdown("✅ :green[**RÓTULO:**] Limpo, bem colado, com informações legíveis.")
    
    st.markdown("---")

    st.subheader("✅ SEGURO")
    st.image("images/liquido_original.jpg", caption="Líquido original.")
    with st.container(border=True):
        st.markdown("✅ :green[**LÍQUIDO:**] Transparente, sem partículas ou cor estranha.")


