import streamlit as st
from streamlit_option_menu import option_menu

# --- Importe as funções das suas páginas ---
from pages import (
    p1_como_identificar as identificar,
    p2_como_se_previnir as previnir,
    p3_sintomas_de_alerta as sintomas,
    p4_o_que_fazer as o_que_fazer,
    p5_denuncie as denuncie,
    p6_Noticias_Recentes as noticias,
    p7_Contato as contato
)

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Alerta Metanol",
    page_icon="⚠️",
    layout="wide"  # Layout largo para aproveitar o espaço
)

# --- ESCONDER A BARRA LATERAL PADRÃO ---
st.markdown("""
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""", unsafe_allow_html=True)


# --- BARRA DE NAVEGAÇÃO NO TOPO ---
selected = option_menu(
    menu_title=None,  # Não queremos um título para o menu
    options=["Início", "Como Identificar", "Como se Prevenir", "Sintomas", "O que Fazer", "Denuncie", "Notícias", "Contato"],
    icons=["house", "search", "shield-check", "exclamation-triangle", "heart-pulse", "telephone-fill", "newspaper", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#1a1a1a"},
        "icon": {"color": "#6dd5ed", "font-size": "20px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#3c3c3c"},
        "nav-link-selected": {"background-color": "#005f73"},
    }
)


# --- CONTEÚDO DA PÁGINA DE INÍCIO (app.py original) ---
def show_inicio():
    st.title("⚠️ Alerta Metanol")
    st.subheader("Saiba como se proteger do metanol, um veneno invisível que pode estar em bebidas de origem duvidosa.")
    st.markdown("---")
    st.header("Vídeo da Campanha")
    # Coloque aqui o st.video() do seu vídeo
    # st.video("https://www.youtube.com/watch?v=T-1PfgEMTPI")
    st.info("Este é um site informativo desenvolvido pelo projeto PET-Saúde. Em caso de emergência, procure a unidade de saúde mais próxima.")


# --- ROTEAMENTO DAS PÁGINAS ---
if selected == "Início":
    show_inicio()
elif selected == "Como Identificar":
    identificar.show_page()
elif selected == "Como se Prevenir":
    previnir.show_page()
elif selected == "Sintomas":
    sintomas.show_page()
elif selected == "O que Fazer":
    o_que_fazer.show_page()
elif selected == "Denuncie":
    denuncie.show_page()
elif selected == "Notícias":
    noticias.show_page()
elif selected == "Contato":
    contato.show_page()