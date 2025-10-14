# theme_toggle.py
import streamlit as st

# --- CSS ATUALIZADO ---

# CSS para o tema claro (branco)
light_theme_css = """
<style>
    :root {
        --primary-color: #f63366;
        --background-color: #ffffff;
        --secondary-background-color: #f0f2f6;
        --text-color: #262730;
        --input-text-color: #262730;
        --input-background-color: #ffffff;
        --input-border-color: #cccccc;
    }
    body, .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-color);
    }
    .st-emotion-cache-18ni7ap, .st-emotion-cache-10trblm, .st-emotion-cache-6qob1r {
         background-color: var(--secondary-background-color);
    }

    /* --- REGRAS PARA BOTÕES --- */
    .stButton>button {
        border: 1px solid var(--input-border-color);
        background-color: var(--input-background-color);
        color: var(--text-color);
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        border-color: var(--primary-color);
        color: var(--primary-color);
    }
    .stButton>button:focus {
        box-shadow: none;
    }

    /* --- REGRAS PARA INPUTS, TEXT AREAS E FILE UPLOADER --- */
    div[data-baseweb="input"] > input,
    div[data-baseweb="textarea"] > textarea {
        background-color: var(--input-background-color);
        color: var(--input-text-color);
        border-color: var(--input-border-color);
    }
    div[data-baseweb="input"] > input::placeholder,
    div[data-baseweb="textarea"] > textarea::placeholder {
        color: #6c757d;
        opacity: 1;
    }
    .st-emotion-cache-1gulkj5, .st-emotion-cache-7oyrr6 {
        border-color: var(--input-border-color);
    }

    /* --- NOVAS REGRAS PARA ALERTAS (st.warning, st.info, etc.) --- */
    div[data-testid="stAlert"] {
        color: #31333F; /* Força uma cor de texto escura para todos os alertas */
    }

</style>
"""

# CSS para o tema escuro
dark_theme_css = """
<style>
    :root {
        --primary-color: #f63366;
        --background-color: #0e1117;
        --secondary-background-color: #262730;
        --text-color: #fafafa;
        --input-text-color: #fafafa;
        --input-background-color: #31333F;
        --input-border-color: #31333F;
    }
    body, .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-color);
    }
    .st-emotion-cache-18ni7ap, .st-emotion-cache-10trblm, .st-emotion-cache-6qob1r {
         background-color: var(--secondary-background-color);
    }

    /* --- REGRAS PARA BOTÕES --- */
    .stButton>button {
        border: 1px solid var(--input-border-color);
        background-color: var(--secondary-background-color);
        color: var(--text-color);
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        border-color: var(--primary-color);
        color: var(--primary-color);
    }
    .stButton>button:focus {
        box-shadow: none;
    }
    
    /* --- REGRAS PARA INPUTS, TEXT AREAS E FILE UPLOADER --- */
    div[data-baseweb="input"] > input,
    div[data-baseweb="textarea"] > textarea {
        background-color: var(--input-background-color);
        color: var(--input-text-color);
        border-color: var(--input-border-color);
    }
    div[data-baseweb="input"] > input::placeholder,
    div[data-baseweb="textarea"] > textarea::placeholder {
        color: #aaaaaa;
        opacity: 1;
    }
    .st-emotion-cache-1gulkj5, .st-emotion-cache-7oyrr6 {
        border-color: var(--input-border-color);
    }

    /* --- NOVAS REGRAS PARA ALERTAS (st.warning, st.info, etc.) --- */
    div[data-testid="stAlert"] {
        color: #fafafa; /* Força uma cor de texto clara para todos os alertas no tema escuro */
    }
    
</style>
"""

def add_theme_toggle():
    """
    Função para adicionar o botão de alternância de tema e aplicar o CSS correspondente.
    Deve ser chamada no início de cada página da sua aplicação.
    """
    if 'theme' not in st.session_state:
        st.session_state.theme = "light"

    def toggle_theme():
        if st.session_state.theme == "light":
            st.session_state.theme = "dark"
        else:
            st.session_state.theme = "light"

    st.sidebar.button("Alternar Tema 🌗", on_click=toggle_theme, use_container_width=True)

    if st.session_state.theme == "light":
        st.markdown(light_theme_css, unsafe_allow_html=True)
    else:
        st.markdown(dark_theme_css, unsafe_allow_html=True)