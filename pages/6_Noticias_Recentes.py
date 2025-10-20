import streamlit as st
import feedparser
import calendar
from datetime import datetime, timezone
from time import mktime # Converter a data do RSS
from urllib.parse import quote_plus # Formatar a query da URL
from zoneinfo import ZoneInfo
from bs4 import BeautifulSoup
from chatbot import chatbot_component

chatbot_component()

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Notícias Recentes - Alerta Metanol",
    page_icon="📰",
    layout="wide"
)

st.title("Notícias Recentes sobre Metanol e Bebidas Adulteradas")
st.markdown("Mantenha-se informado com as últimas notícias sobre os riscos, apreensões e casos relacionados.")
st.markdown("---")

# --- LÓGICA PARA BUSCAR NOTÍCIAS ---

# Usamos o cache para não chamar a API toda vez que a página recarrega
# O TTL (Time To Live) de 3600 segundos significa que os dados serão atualizados a cada hora
@st.cache_data(ttl=3600)
def buscar_noticias():
    # Termos de busca. Usamos "OR" para encontrar qualquer um dos termos.
    queries = [
    '"metanol"',
    '"intoxicação alcoólica"',
    '"bebida falsificada"',
    '"bebida adulterada"',
    '"apreensão de bebida"',
    '"álcool adulterado"',
    '"álcool falsificado"',
    '"intoxicação por metanol"',
    '"envenenamento por metanol"',
    '"álcool ilegal"',
    '"álcool clandestino"'
    ]

    artigos_combinados = []
    links_vistos = set() # Usado para evitar duplicatas
    titulos_vistos = set()

    for query in queries:
    # Codificamos os termos para usar na URL do Google
        query_encoded = quote_plus(query)

        # URL do Feed RSS do Google Notícias
        url = (
            f'https://news.google.com/rss/search?'
            f'q={query_encoded}&'
            'hl=pt-BR&'
            'gl=BR&'
            'ceid=BR:pt-419'
        )

        try:
            # Usamos o feedparser para "parsear" (ler) o XML do RSS
            feed = feedparser.parse(url)
            
            artigos_combinados = []
            
            # Iteramos pelas entradas do feed
            for entrada in feed.entries:
                nome_fonte = entrada.source.title if 'source' in entrada else 'Desconhecida'
                # Remover sufixo da fonte do título, se presente
                titulo_original = entrada.title
                
                sufixo_fonte = f" - {nome_fonte}"

                if titulo_original.endswith(sufixo_fonte):
                    entrada.title = titulo_original[:-len(sufixo_fonte)].strip()

                # Evita duplicatas baseadas em link ou título
                if entrada.link in links_vistos or entrada.title in titulos_vistos:
                    continue  # Pula duplicatas
                    
                # 'published_parsed' é um struct_time em UTC (GMT)
                # 'calendar.timegm' converte um struct_time UTC para um timestamp UTC
                utc_timestamp = calendar.timegm(entrada.published_parsed)
                
                # Cria um objeto datetime "aware" (com fuso) em UTC
                dt_publicacao_utc = datetime.fromtimestamp(utc_timestamp, tz=timezone.utc)
                
                # Salva como string ISO. Ela agora terá a informação de fuso (+00:00)
                iso_data = dt_publicacao_utc.isoformat()

                # Montamos o dicionário no mesmo formato que a News API fornecia
                artigos_combinados.append({
                    "title": entrada.title,
                    "description": entrada.summary, # O RSS chama de 'summary'
                    "url": entrada.link,
                    "urlToImage": None, # IMPORTANTE: RSS do Google não fornece imagem
                    "publishedAt": iso_data,
                    "source": {"name": entrada.source.title} # Fonte da notícia
                })
                links_vistos.add(entrada.link)
                titulos_vistos.add(entrada.title)
        except Exception as e:
            st.error(f"Erro ao buscar feed para a query '{query}': {e}")
            
        artigos_combinados.sort(key=lambda x: x["publishedAt"], reverse=True) # Ordena por data decrescente

        return artigos_combinados

# --- EXIBIÇÃO DAS NOTÍCIAS ---
ZONA_LOCAL = ZoneInfo("America/Fortaleza")  # Fuso horário da Paraíba, Brasil
artigos = buscar_noticias()

if artigos:
    # Limita a 15 notícias para não poluir a página
    for artigo in artigos[:15]:
        fonte = artigo["source"]["name"]
        
        dt_obj_utc = datetime.fromisoformat(artigo["publishedAt"])  # 1. Lê a string ISO (que já tem o fuso +00:00) para um objeto datetime
        dt_obj_local = dt_obj_utc.astimezone(ZONA_LOCAL) # 2. Converte o objeto datetime de UTC para o fuso local (Paraiba)
        data_publicacao = dt_obj_local.strftime('%d/%m/%Y às %H:%M') # 3. Formata a data/hora local

        st.subheader(artigo["title"])
        st.caption(f"Fonte: {fonte} | Publicado em: {data_publicacao}")

        st.markdown(f"[Ler a matéria completa →]({artigo['url']})")

        st.markdown("---")
else:
    st.warning("Nenhuma notícia recente encontrada sobre o tema.")
