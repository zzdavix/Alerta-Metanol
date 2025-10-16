import streamlit as st
from chatbot import chatbot_component

chatbot_component()

st.set_page_config(
    page_title="O que Fazer? - Alerta Metanol",
    page_icon="🚑",
    layout="wide"
)

st.title("Como agir em caso de suspeita de intoxicação por metanol.")
st.markdown("---")

st.subheader("1. VÁ PARA O HOSPITAL OU UPA MAIS PRÓXIMA IMEDIATAMENTE.")
st.error(
    "**Não espere os sintomas piorarem. Não fique em casa.** "
    "O tratamento precisa ser iniciado o mais rápido possível para evitar danos permanentes à visão e outros órgãos."
)
st.info(
    "Os profissionais de saúde que identificarem a intoxicação farão a notificação compulsória à Secretaria de Saúde do seu município, o que é fundamental para o rastreamento de surtos."
)
st.write("")

st.subheader("2. INFORME A EQUIPE DE SAÚDE SOBRE A SUSPEITA.")
st.info(
    "Ao chegar, diga claramente: **'Eu (ou a pessoa que estou acompanhando) consumi uma bebida alcoólica "
    "de origem suspeita e acho que pode ser intoxicação por metanol.'** "
    "Essa informação direciona o diagnóstico."
)
st.write("")

st.subheader("3. LEVE A BEBIDA SUSPEITA (SE FOR SEGURO E POSSÍVEL).")
st.warning(
    "Leve a garrafa, mesmo que vazia, ou uma foto nítida do rótulo. "
    "Isso pode ajudar a equipe a confirmar o agente tóxico mais rapidamente."
)
st.write("")

st.subheader("4. LIGUE PARA OS CENTROS DE INFORMAÇÃO TOXICOLÓGICA.")
st.write(
    "Esses centros oferecem orientação especializada gratuita para a população e para os profissionais de saúde, 24 horas por dia. "
    "Eles podem fornecer informações cruciais sobre o tratamento."
)

# --- SEÇÃO MODIFICADA ---
col1, col2 = st.columns(2)

with col1:
    st.container(border=True).markdown(
        """
        <h3 style='text-align: center;'>Brasil (CIATox)</h3>
        <h2 style='text-align: center;'>📞 0800 722 6001</h2>
        <p style='text-align: center;'>Ligação gratuita para todo o país.</p>
        """, unsafe_allow_html=True
    )

with col2:
    st.container(border=True).markdown(
        """
        <h3 style='text-align: center;'>Grande João Pessoa (Assistência Toxicológica)</h3>
        <h2 style='text-align: center;'>📞 (83) 3216-7450</h2>
        <p style='text-align: center;'>Para saber qual serviço de saúde buscar na região.</p>
        """, unsafe_allow_html=True
    )
st.write("")

st.subheader("5. NÃO DIRIJA EM HIPÓTESE ALGUMA.")
st.error(
    "**Sua visão, seus reflexos e sua coordenação podem estar gravemente comprometidos.** "
    "Peça ajuda a um familiar, amigo, vizinho, chame um transporte por aplicativo ou, se necessário, uma ambulância (SAMU 192)."
)

st.markdown("---")