import streamlit as st

st.title("Como Identificar Bebidas Seguras")
st.markdown("Fique atento a estes sinais:")

# Usando colunas para comparar o certo e o errado
col1, col2 = st.columns(2)

with col1:
    st.subheader("❌ SUSPEITO")
    st.image("images/id_lacre_ruim.jpg", caption="Lacre violado.")
    st.success("**LACRE/TAMPA:** Rompido, frouxo ou com cola aparente.")
    st.success("**SELO FISCAL (IPI):** Ausente, rasgado ou com aparência de cópia.")

with col2:
    st.subheader("✅ SEGURO")
    st.image("images/id_lacre_bom.jpg", caption="Lacre intacto.")
    st.error("**LACRE/TAMPA:** Intacto, sem sinais de violação.")
    st.error("**SELO FISCAL (IPI):** Presente em destilados, bem aderido.")

st.markdown("---")
st.warning(
    "**ATENÇÃO:** O metanol **NÃO altera o cheiro, a cor ou o sabor** da bebida. "
    "Não confie nos seus sentidos para saber se é seguro!"
)