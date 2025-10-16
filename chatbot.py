import streamlit as st

def get_response(user_input):
    """
    Retorna uma resposta baseada em palavras-chave encontradas no input do usuário.
    """
    text = user_input.lower().strip()
    
    # MENSAGEM PADRÃO
    response = "Desculpe, não entendi sua pergunta. Tente perguntar sobre 'sintomas', 'como prevenir' ou 'denunciar'."

    # Regra de Emergência
    if any(word in text for word in ["sinto", "passando mal", "sintoma", "socorro", "ajuda", "emergência"]):
        response = (
            "**ATENÇÃO: Se você ou alguém apresenta sintomas, NÃO espere!**\n\n"
            "Vá **IMEDIATAMENTE** para o hospital ou UPA mais próxima. "
            "Para mais orientações, acesse a página **'O Que Fazer?'**."
        )
        return response # Usamos 'return' aqui para parar a execução imediatamente, pois é uma emergência.

    # Outras regras (agora usando if/elif para garantir apenas uma resposta)
    if any(word in text for word in ["identificar", "saber se é falsa", "rótulo", "lacre", "selo"]):
        response = "Para saber como identificar uma bebida segura, verifique o lacre e o selo fiscal (IPI). Eu recomendo que você visite a página **'Como Identificar'** para ver as imagens e detalhes."
    elif any(word in text for word in ["prevenir", "evitar", "seguro", "comprar"]):
        response = "Para se prevenir, compre sempre em locais de confiança e desconfie de preços muito baixos. Veja todas as dicas na página **'Como se Prevenir'**."
    elif any(word in text for word in ["denunciar", "denúncia"]):
        response = "Sua denúncia é muito importante! Você pode usar o formulário na página **'Denuncie'** ou contatar diretamente a AGEVISA. A página tem todos os telefones e links."
    elif any(word in text for word in ["fazer", "intoxicado", "hospital"]):
        response = "Em caso de suspeita de intoxicação, a ação mais importante é ir para um hospital ou UPA imediatamente. A página **'O Que Fazer?'** tem o passo a passo completo."
    elif any(word in text for word in ["contato", "falar com", "sugestão"]):
        response = "Para dúvidas sobre o projeto, sugestões ou parcerias, acesse a página **'Contato'**. Lembre-se que aquele canal não é para emergências médicas."
    elif any(word in text for word in ["notícias", "casos", "recente"]):
        response = "Você pode ver as notícias mais recentes sobre metanol e bebidas adulteradas na página **'Notícias Recentes'**."
    elif any(word in text for word in ["oi", "olá", "bom dia", "boa tarde"]):
        response = "Olá! 👋 Sou o assistente virtual do Alerta Metanol. Como posso ajudar?"
    elif any(word in text for word in ["obrigado", "valeu", "tchau"]):
        response = "De nada! Se cuide. Lembre-se: na dúvida, não beba."
    # ADICIONADO: Resposta para 'teste'
    elif text == "teste":
        response = "Estou funcionando corretamente! Pronto para ajudar a encontrar informações sobre metanol."

    return response # Garante que a resposta (padrão ou específica) seja sempre retornada.


def chatbot_component():
    """
    Cria o componente completo do chatbot na sidebar.
    (Esta função permanece a mesma)
    """
    with st.sidebar:
        st.header("💬 Assistente Virtual")

        if "chat_is_open" not in st.session_state:
            st.session_state.chat_is_open = False

        if st.button("Fale com o Assistente"):
            st.session_state.chat_is_open = not st.session_state.chat_is_open
        
        if st.session_state.chat_is_open:
            st.markdown("---")
            
            chat_container = st.container(height=400)
            
            if "messages" not in st.session_state:
                st.session_state.messages = [{"role": "assistant", "content": "Olá! Como posso te ajudar a encontrar informações sobre os perigos do metanol?"}]

            with chat_container:
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

            if prompt := st.chat_input("Sua pergunta..."):
                st.session_state.messages.append({"role": "user", "content": prompt})

                # Obtém a resposta do bot
                response = get_response(prompt)
                
                # Adiciona a resposta ao histórico
                st.session_state.messages.append({"role": "assistant", "content": response})

                # Reroda para atualizar a interface
                st.rerun()