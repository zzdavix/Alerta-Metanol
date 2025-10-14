import streamlit as st
import requests
from datetime import datetime
from theme_toggle import add_theme_toggle

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Notícias Recentes - Alerta Metanol",
    page_icon="📰",
    layout="wide"
)

add_theme_toggle()

st.title("Notícias Recentes sobre Metanol e Bebidas Adulteradas")
st.markdown("Mantenha-se informado com as últimas notícias sobre os riscos, apreensões e casos relacionados.")
st.markdown("---")

# --- LÓGICA PARA BUSCAR NOTÍCIAS ---

# Usamos o cache para não chamar a API toda vez que a página recarrega
# O TTL (Time To Live) de 3600 segundos significa que os dados serão atualizados a cada hora
@st.cache_data(ttl=3600)
def buscar_noticias(api_key):
    # Termos de busca. Usamos "OR" para encontrar qualquer um dos termos.
    query = '"metanol" OR "intoxicação alcoólica" OR "bebida falsificada" OR "bebida adulterada"'

    # URL da API
    url = (
        'https://newsapi.org/v2/everything?'
        f'q={query}&'
        'language=pt&'          # Buscar notícias em português
        'sortBy=publishedAt&'   # Ordenar pelas mais recentes
        f'apiKey={api_key}'
    )

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro se a requisição falhar
        return response.json()["articles"]
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar notícias: {e}")
        return None

# --- EXIBIÇÃO DAS NOTÍCIAS ---

# Pega a chave da API dos segredos do Streamlit
API_KEY = st.secrets.get("NEWS_API_KEY")

if not API_KEY:
    st.error("Chave da API de Notícias não encontrada. Por favor, configure o arquivo secrets.toml.")
else:
    # Busca as notícias
    artigos = buscar_noticias(API_KEY)

    if artigos:
        # Limita a 15 notícias para não poluir a página
        for artigo in artigos[:15]:
            col1, col2 = st.columns([1, 3]) # Coluna da imagem menor que a do texto

            with col1:
                # Verifica se a notícia tem uma imagem
                if artigo["urlToImage"]:
                    st.image(artigo["urlToImage"], width="stretch")

            with col2:
                fonte = artigo["source"]["name"]
                data_publicacao = datetime.fromisoformat(artigo["publishedAt"].replace("Z", "+00:00")).strftime('%d/%m/%Y às %H:%M')

                st.subheader(artigo["title"])
                st.caption(f"Fonte: {fonte} | Publicado em: {data_publicacao}")
                st.write(artigo["description"])
                st.markdown(f"[Ler a matéria completa →]({artigo['url']})")

            st.markdown("---")
    else:
        st.warning("Nenhuma notícia recente encontrada sobre o tema.")