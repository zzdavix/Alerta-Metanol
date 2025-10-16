import streamlit as st
from unidecode import unidecode
from thefuzz import process
from streamlit_float import float_init, float_parent, float_css_helper

# O dicionário RESPONSES e a função get_response permanecem inalterados
RESPONSES = {
    "emergency": {
        "keywords": ["sinto", "sintoma", "socorro", "ajuda", "emergencia", "passando mal", "dor"],
        "answer": (
            "**ATENÇÃO: Se você ou alguém apresenta sintomas, NÃO espere!**\n\n"
            "Vá **IMEDIATAMENTE** para o hospital ou UPA mais próxima. "
            "Para mais orientações, acesse a página **'O Que Fazer?'**."
        )
    },
    "identification": {
        "keywords": ["identificar", "falsa", "rotulo", "lacre", "selo"],
        "answer": "Para saber como identificar uma bebida segura, verifique o lacre e o selo fiscal (IPI). Eu recomendo que você visite a página **'Como Identificar'** para ver as imagens e detalhes."
    },
    "prevention": {
        "keywords": ["prevenir", "evitar", "seguro", "comprar"],
        "answer": "Para se prevenir, compre sempre em locais de confiança e desconfie de preços muito baixos. Veja todas as dicas na página **'Como se Prevenir'**."
    },
    "denounce": {
        "keywords": ["denunciar", "denuncia", "reclamar"],
        "answer": "Sua denúncia é muito importante! Você pode usar o formulário na página **'Denuncie'** ou contatar diretamente a AGEVISA. A página tem todos os telefones e links."
    },
    "what_to_do": {
        "keywords": ["fazer", "intoxicado", "hospital", "agir"],
        "answer": "Em caso de suspeita de intoxicação, a ação mais importante é ir para um hospital ou UPA imediatamente. A página **'O Que Fazer?'** tem o passo a passo completo."
    },
    "contact": {
        "keywords": ["contato", "falar", "sugestao", "parceria"],
        "answer": "Para dúvidas sobre o projeto, sugestões ou parcerias, acesse a página **'Contato'**. Lembre-se que aquele canal não é para emergências médicas."
    },
    "news": {
        "keywords": ["noticias", "casos", "recente"],
        "answer": "Você pode ver as notícias mais recentes sobre metanol e bebidas adulteradas na página **'Notícias Recentes'**."
    },
    "greeting": {
        "keywords": ["oi", "ola", "bom dia", "boa tarde", "boa noite"],
        "answer": "Olá! 👋 Sou o assistente virtual do Alerta Metanol. Como posso ajudar?"
    },
    "thanks": {
        "keywords": ["obrigado", "valeu", "tchau"],
        "answer": "De nada! Se cuide. Lembre-se: na dúvida, não beba."
    }
}

def get_response(user_input):
    normalized_input = unidecode(user_input.lower())
    words_in_input = normalized_input.split()
    best_match_score = 0
    best_response = "Desculpe, não entendi sua pergunta. Tente perguntar sobre 'sintomas', 'como prevenir' ou 'denunciar'."
    for word in words_in_input:
        match = process.extractOne(word, RESPONSES["emergency"]["keywords"], score_cutoff=85)
        if match:
            return RESPONSES["emergency"]["answer"]
    for intent_key, intent_data in RESPONSES.items():
        if intent_key == "emergency":
            continue
        for word in words_in_input:
            match = process.extractOne(word, intent_data["keywords"])
            if match and match[1] > best_match_score and match[1] > 80:
                best_match_score = match[1]
                best_response = intent_data["answer"]
    return best_response

def chatbot_component():
    """
    Cria um botão de controle na sidebar e uma janela de chat flutuante com botão de fechar, CSS responsivo e rolagem otimizada.
    """
    float_init()

    with st.sidebar:
        st.header("💬 Assistente Virtual")
        if st.button("Abrir / Fechar Chat"):
            st.session_state.chat_is_open = not st.session_state.get("chat_is_open", False)

    if st.session_state.get("chat_is_open", False):
        # Adiciona CSS para melhorar a rolagem
        st.markdown("""
            <style>
            .chat-container {
                overflow-y: auto;
                -webkit-overflow-scrolling: touch; /* Melhora a rolagem em dispositivos móveis */
                scrollbar-width: thin; /* Barra de rolagem fina para Firefox */
            }
            .chat-container::-webkit-scrollbar {
                width: 8px; /* Barra de rolagem fina para Chrome/Safari */
            }
            .chat-container::-webkit-scrollbar-thumb {
                background-color: #4A4A4A; /* Cor da barra de rolagem */
                border-radius: 4px;
            }
            .chat-container::-webkit-scrollbar-track {
                background: transparent; /* Fundo da trilha de rolagem */
            }
            </style>
        """, unsafe_allow_html=True)

        float_container = st.container()
        with float_container:
            # Botão de fechar no topo do contêiner
            col1, col2 = st.columns([4, 1])
            with col1:
                st.subheader("Fale com o Assistente")
            with col2:
                if st.button("✖", key="close_chat"):
                    st.session_state.chat_is_open = False
                    st.rerun()

            chat_container = st.container(height=350)
            with chat_container:
                # Aplica a classe CSS personalizada para o contêiner de chat
                st.markdown('<div class="chat-container">', unsafe_allow_html=True)
                if "messages" not in st.session_state:
                    st.session_state.messages = [{"role": "assistant", "content": "Olá! Como posso te ajudar?"}]
                
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])
                st.markdown('</div>', unsafe_allow_html=True)

            if prompt := st.chat_input("Sua pergunta..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                response = get_response(prompt)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()

            # Aplica o CSS responsivo usando float_css_helper, com bottom ajustado para 30px
            css = float_css_helper(
                position="fixed",
                bottom="30px",  # Ajustado conforme sua preferência
                right="20px",
                width="350px",
                height="500px",
                background="#1E1E1E",
                border="1px solid #4A4A4A",
                border_radius="10px",
                box_shadow="5px 5px 15px rgba(0,0,0,0.4)",
                z_index="1000",
                display="flex",
                flex_direction="column",
                padding="15px",
                max_width="90vw"
            )
            float_parent(css)