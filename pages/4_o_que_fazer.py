import streamlit as st
from theme_toggle import add_theme_toggle

# Configuração da página
st.set_page_config(
    page_title="O que Fazer? - Alerta Metanol",
    page_icon="🚑",
    layout="wide"
)

add_theme_toggle()

# Título da Página
st.title("Como agir em caso de suspeita de intoxicação por metanol.")

st.markdown("---")

# Passo 1
st.subheader("1. VÁ PARA O HOSPITAL OU UPA MAIS PRÓXIMA IMEDIATAMENTE.")
st.error(
    "**Não espere os sintomas piorarem. Não fique em casa.** "
    "O tratamento precisa ser iniciado o mais rápido possível para evitar danos permanentes à visão e outros órgãos."
)
st.write("") # Adiciona um espaço

# Passo 2
st.subheader("2. INFORME A EQUIPE DE SAÚDE SOBRE A SUSPEITA.")
st.info(
    "Ao chegar, diga claramente: **'Eu (ou a pessoa que estou acompanhando) consumi uma bebida alcoólica "
    "de origem suspeita e acho que pode ser intoxicação por metanol.'** "
    "Essa informação direciona o diagnóstico."
)
st.write("") # Adiciona um espaço

# Passo 3
st.subheader("3. LEVE A BEBIDA SUSPEITA (SE FOR SEGURO E POSSÍVEL).")
st.warning(
    "Leve a garrafa, mesmo que vazia, ou uma foto nítida do rótulo. "
    "Isso pode ajudar a equipe a confirmar o agente tóxico mais rapidamente."
)
st.write("") # Adiciona um espaço

# Passo 4
st.subheader("4. LIGUE PARA O CIATox (Centro de Informação Toxicológica).")
st.write(
    "O CIATox oferece orientação especializada gratuita para a população e para os profissionais de saúde, 24 horas por dia. "
    "Eles podem fornecer informações cruciais sobre o tratamento."
)
# Bloco de destaque para o número de telefone
st.container(border=True).header("📞 0800 722 6001")
st.caption("A ligação é gratuita para todo o Brasil.")
st.write("") # Adiciona um espaço

# Passo 5
st.subheader("5. NÃO DIRIJA EM HIPÓTESE ALGUMA.")
st.error(
    "**Sua visão, seus reflexos e sua coordenação podem estar gravemente comprometidos.** "
    "Peça ajuda a um familiar, amigo, vizinho, chame um transporte por aplicativo ou, se necessário, uma ambulância (SAMU 192)."
)

st.markdown("---")