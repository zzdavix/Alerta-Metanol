import streamlit as st
from unidecode import unidecode
from thefuzz import process
from streamlit_float import float_init, float_parent, float_css_helper
import botoes

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
                st.markdown("##### Fale com o Assistente")
            with col2:
                if st.button("✖", key="close_chat"):
                    st.session_state.chat_is_open = False
                    st.rerun()

            chat_container = st.container(height=390)
            with chat_container:
                st.markdown('<div class="chat-container">', unsafe_allow_html=True)

                # --- INICIALIZAÇÃO DO CHAT ---
                if "messages" not in st.session_state:
                    st.session_state.messages = [
                        {"role": "assistant", "content": "Olá! Como posso te ajudar?"}
                    ]
                    # Controla qual menu exibir: "main", "outro_assunto", ou "none"
                    st.session_state.menu_state = "main" 

                # --- EXIBE O HISTÓRICO DE MENSAGENS ---
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

                # --- LÓGICA DE NAVEGAÇÃO DOS BOTÕES ---

                # Pega o estado atual do menu
                current_menu_state = st.session_state.get("menu_state", "main")

                # 1. MOSTRAR O MENU PRINCIPAL
                if current_menu_state == "main":
                    st.write("Olá! Eu sou o assistente virtual e estou aqui para ajudar. Qual sua situação agora?")
                    
                    # Botão 1: Emergência
                    if st.button("🚨 EMERGÊNCIA (Suspeita de Intoxicação)", width="stretch"):
                        st.session_state.messages.append({"role": "user", "content": "Emergência."})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.emer_resp}) # Resposta: "ATENÇÃO: A intoxicação..."
                        st.session_state.menu_state = "emergencia"
                        st.rerun()

                    # Botão 2: Prevenção e Dúvidas
                    if st.button("💡 PREVENÇÃO E DÚVIDAS (Quero me informar)", width="stretch"):
                        st.session_state.messages.append({"role": "user", "content": "Quero me informar."})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.prev_resp}) # Resposta: "Ótimo! A informação é a melhor defesa..."
                        st.session_state.menu_state = "prevencao"
                        st.rerun()

                    # Botão 3: Denúncia
                    if st.button("📣 DENÚNCIA (Quero relatar um problema)", width="stretch"):
                        st.session_state.messages.append({"role": "user", "content": "Quero fazer uma denúncia."})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.denuncia_resp}) # Resposta: "Sua denúncia é fundamental..."
                        st.session_state.menu_state = "denuncia"
                        st.rerun()

                    # Botão 4: Outros Assuntos
                    if st.button("📰 OUTROS ASSUNTOS (Notícias, Contato)", width="stretch"):
                        st.session_state.messages.append({"role": "user", "content": "Outros assuntos."})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.outros_resp}) # Resposta: "Selecione o que você busca:"
                        st.session_state.menu_state = "outros"
                        st.rerun()

                # 2. FLUXO DE EMERGÊNCIA
                elif current_menu_state == "emergencia":
                    # Botão de sintomas graves
                    if st.button(botoes.emer_sim_grave_botao, width="stretch"): # "Sim, sintomas graves..."
                        st.session_state.messages.append({"role": "user", "content": botoes.emer_sim_grave_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.sint_grave_resp}) # Resposta: "LIGUE IMEDIATAMENTE..."
                        st.session_state.menu_state = "none" 
                        st.rerun()
                    
                    # Botão de sintomas iniciais
                    if st.button(botoes.emer_sim_inicial_botao, width="stretch"): # "Sim, sintomas iniciais..."
                        st.session_state.messages.append({"role": "user", "content": botoes.emer_sim_inicial_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.sint_inicial_resp}) # Resposta: "Esses sintomas podem evoluir..."
                        st.session_state.menu_state = "none" 
                        st.rerun()
                    
                    # Botão de sintomas não presentes
                    if st.button(botoes.emer_nao_botao, width="stretch"): # "Não, mas bebi algo suspeito..."
                        st.session_state.messages.append({"role": "user", "content": botoes.emer_nao_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.sint_nao_resp}) # Resposta: "Fique alerta..."
                        st.session_state.menu_state = "none" 
                        st.rerun()
                    
                    # Botão de todos os sintomas
                    if st.button(botoes.emer_todos_botao, width="stretch"): # "Quais são TODOS os sintomas?"
                        st.session_state.messages.append({"role": "user", "content": botoes.emer_todos_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.sint_todos_resp}) # Resposta: "Claro. Os sintomas são divididos em fases..."
                        st.session_state.menu_state = "none"
                        st.rerun()

                # 3. FLUXO DE PREVENÇÃO E DÚVIDAS
                elif current_menu_state == "prevencao":
                    if st.button(botoes.prev_como_botao, width="stretch"): # "Como me previnir (em bares, festas, etc.)"
                        st.session_state.messages.append({"role": "user", "content": botoes.prev_como_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.prev_como_resp}) # Resposta: "O principal é a procedência..."
                        st.session_state.menu_state = "prevencao_como"
                        st.rerun()

                    if st.button(botoes.prev_identificar_botao, width="stretch"): # "Como identificar uma bebida falsa"
                        st.session_state.messages.append({"role": "user", "content": botoes.prev_identificar_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.prev_identificar_resp}) # Resposta: "É difícil ter 100% de certeza..."
                        st.session_state.menu_state = "prevencao_identificar"
                        st.rerun()

                    if st.button(botoes.prev_oqe_botao, width="stretch"): # "O que é Metanol?"
                        st.session_state.messages.append({"role": "user", "content": botoes.prev_oqe_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.prev_oqe_resp}) # Resposta: "É um tipo de álcool tóxico..."
                        st.session_state.menu_state = "none"
                        st.rerun()

                # 3.1 SUB-FLUXO: Como se Prevenir
                elif current_menu_state == "prevencao_como":
                    if st.button(botoes.prev_como_bares_botao, width="stretch"): # "Dicas em Bares e Festas"
                        st.session_state.messages.append({"role": "user", "content": botoes.prev_como_bares_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.prev_como_bares_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()
                    
                    if st.button(botoes.prev_como_garrafas_botao, width="stretch"): # "Dicas ao Comprar Garrafas"
                        st.session_state.messages.append({"role": "user", "content": botoes.prev_como_garrafas_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.prev_como_garrafas_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()

                # 3.2 SUB-FLUXO: Como Identificar
                elif current_menu_state == "prevencao_identificar":
                    if st.button(botoes.prev_id_rotulo_botao, width="stretch"): # "Sinais no Rótulo e Lacre"
                        st.session_state.messages.append({"role": "user", "content": botoes.prev_id_rotulo_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.prev_id_rotulo_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()
                    
                    if st.button(botoes.prev_id_liquido_botao, width="stretch"): # "Sinais no Líquido"
                        st.session_state.messages.append({"role": "user", "content": botoes.prev_id_liquido_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.prev_id_liquido_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()

                    if st.button(botoes.prev_id_cheiro_botao, width="stretch"): # "Dá para saber pelo cheiro ou gosto?"
                        st.session_state.messages.append({"role": "user", "content": botoes.prev_id_cheiro_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.prev_id_cheiro_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()


                # 4. FLUXO DE DENÚNCIA
                elif current_menu_state == "denuncia":
                    if st.button(botoes.denuncia_form_botao, width="stretch"): # "Quero denunciar um estabelecimento (Online)"
                        st.session_state.messages.append({"role": "user", "content": botoes.denuncia_form_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.denuncia_form_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()
                    
                    if st.button(botoes.denuncia_telefones_botao, width="stretch"): # "Quero os telefones de órgãos públicos"
                        st.session_state.messages.append({"role": "user", "content": botoes.denuncia_telefones_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.denuncia_telefones_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()

                    if st.button(botoes.denuncia_o_que_precisa_botao, width="stretch"): # "O que preciso para fazer uma boa denúncia?"
                        st.session_state.messages.append({"role": "user", "content": botoes.denuncia_o_que_precisa_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.denuncia_o_que_precisa_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()


                # 5. FLUXO DE OUTROS ASSUNTOS
                elif current_menu_state == "outros":
                    if st.button(botoes.outros_noticias_botao, width="stretch"): # "Notícias Recentes"
                        st.session_state.messages.append({"role": "user", "content": botoes.outros_noticias_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.outros_noticias_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()
                    
                    if st.button(botoes.outros_contato_botao, width="stretch"): # "Falar com o responsável pelo site"
                        st.session_state.messages.append({"role": "user", "content": botoes.outros_contato_botao})
                        st.session_state.messages.append({"role": "assistant", "content": botoes.outros_contato_resp})
                        st.session_state.menu_state = "none"
                        st.rerun()


                # 6. ESTADO DE RESPOSTA (nenhum menu ativo)
                elif current_menu_state == "none":
                    # Mostra um botão para reiniciar a conversa
                    if st.button("Voltar ao Início", width="stretch"):
                        st.session_state.messages.append({"role": "user", "content": "Voltar ao Início."})
                        st.session_state.menu_state = "main"
                        st.rerun()


                # 7. MOSTRAR O BOTÃO "VOLTAR" (APÓS UMA RESPOSTA FINAL)
                elif current_menu_state == "none":
                    last_message = st.session_state.messages[-1]
                    
                    # Adicionamos as novas respostas à lista de gatilhos
                    menu_trigger_responses = [botoes.sint_grave_resp, botoes.sint_inicial_resp,
                                              botoes.sint_nao_resp, botoes.sint_todos_resp]

                    if last_message["role"] == "assistant" and last_message["content"] in menu_trigger_responses:
                        if st.button("Voltar ao Menu ↩️", width="stretch"):
                            st.session_state.messages.append({"role": "user", "content": "Voltar ao menu."})
                            st.session_state.messages.append({"role": "assistant", "content": "Olá! Como posso te ajudar?"})
                            st.session_state.menu_state = "main" # Volta ao menu principal
                            st.rerun()

                st.markdown('</div>', unsafe_allow_html=True)

            # --- LÓGICA DO INPUT NORMAL DO USUÁRIO ---
            if prompt := st.chat_input("Digite sua mensagem..."):
                # Se o usuário digitar, o menu deve sumir
                st.session_state.menu_state = "none" 
                
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