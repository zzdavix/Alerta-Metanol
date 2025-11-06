import streamlit as st
from chatbot import chatbot_component

chatbot_component()

# Configuração da página
st.set_page_config(
    page_title="Sintomas de Alerta - Alerta Metanol",
    page_icon="🚨",
    layout="wide"
)

# Título da Página
st.title("Sintomas de Alerta")
st.write(
    "Os sintomas da intoxicação por metanol podem demorar de 6 a 24 horas para aparecer. "
    "Fique atento aos sinais iniciais e, principalmente, aos sinais de gravidade."
)

st.markdown("---")

st.image("images/Sintomas.png", caption="Sintomas da intoxicação por metanol.")

# Usando st.tabs para organizar a informação
tab1, tab2 = st.tabs(["Sintomas Iniciais", "Sinais de Gravidade (Emergência!)"])

# Conteúdo da primeira aba
with tab1:
    st.subheader("Primeiros Sinais (6 a 24 horas após o consumo)")
    st.warning(
        "Estes sintomas iniciais podem ser facilmente confundidos com uma embriaguez forte ou uma ressaca. "
        "O sinal de alerta é a **piora progressiva** do quadro em vez da melhora."
    )
    
    st.markdown(
        """
        - **Náusea e Vômitos**
        - **Dor de Cabeça Forte e Persistente**
        - **Tontura, Fraqueza e Sensação de Cansaço Extremo**
        - **Dor Abdominal Forte (na boca do estômago)**
        """
    )

# Conteúdo da segunda aba
with tab2:
    st.subheader("Sinais de Gravidade")
    st.error(
        "Se você ou alguém apresentar **qualquer um dos sintomas abaixo**, especialmente após consumir "
        "uma bebida de origem duvidosa, vá para a UPA ou hospital mais próximo."
    )

    st.markdown("#### **Alterações na visão**")
    st.markdown(
        """
        - **Visão turva ou embaçada**
        - **Sensação de 'neve' ou 'chuviscos' na visão**
        - **Visão dupla**
        - **Dificuldade em distinguir cores**
        - **Perda parcial ou total da visão**
        """
    )

    st.markdown("#### **Sintomas Neurológicos**")
    st.markdown(
        """
        - **Confusão mental e agitação**
        - **Dificuldade para andar ou se manter em pé**
        - **Sonolência excessiva**
        - **Convulsões**
        """
    )
    
    st.markdown("#### **Respiração**")
    st.markdown(
        """
        - **Respiração rápida e curta**
        - **Dificuldade para respirar**
        """
    )

st.markdown("---")

# Caixa de destaque para a ação mais importante
st.error(
    "**ATENÇÃO:** A alteração visual é o principal sinal que diferencia a intoxicação por metanol "
    "de uma ressaca comum. Se a visão for afetada, a situação é gravíssima. Vá imediatamente para o hospital ou UPA mais próxima."
)
