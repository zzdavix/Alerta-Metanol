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
    st.image("images/id_lacre_ruim.jpg", caption="Lacre violado.")
    st.error("**LACRE/TAMPA:** Rompido, frouxo ou com cola aparente.")
    st.error("**SELO FISCAL (IPI):** Ausente, rasgado ou com aparência de cópia.")

with col2:
    st.subheader("✅ SEGURO")
    st.image("images/id_lacre_bom.jpg", caption="Lacre intacto.")
    st.success("**LACRE/TAMPA:** Intacto, sem sinais de violação.")
    st.success("**SELO FISCAL (IPI):** Presente em destilados, bem aderido.")


