import streamlit as st
import psycopg2          # Para o banco de dados Neon
from supabase import create_client as create_supabase_client, Client
import os
import uuid
from datetime import datetime
from chatbot import chatbot_component

# Ativa o chatbot
chatbot_component()

# --- FUNÇÕES DE CONEXÃO AO BANCO DE DADOS (NEON) ---

def get_db_conn():
    """Retorna uma nova conexão com o banco de dados PostgreSQL usando a URL dos secrets."""
    try:
        conn_string = st.secrets["db_url"]
        conn = psycopg2.connect(conn_string)
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def init_db():
    """Cria a tabela 'denuncias' se ela não existir. (Boa prática)"""
    conn = get_db_conn()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS denuncias (
                        id UUID PRIMARY KEY,
                        timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        nome_estabelecimento VARCHAR(255),
                        endereco TEXT,
                        descricao TEXT,
                        caminho_imagem VARCHAR(512)
                    );
                """)
            conn.commit()
        except Exception as e:
            st.error(f"Erro ao inicializar a tabela: {e}")
        finally:
            if conn:
                conn.close()

# --- FUNÇÃO DE CONEXÃO AO STORAGE DE IMAGENS (SUPABASE) ---

def get_storage_client():
    """Inicializa e retorna o cliente Supabase."""
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_ANON_KEY"]
        
        # A biblioteca 'supabase' cuida das headers e da inicialização
        supabase_client: Client = create_supabase_client(url, key)
        
        # Retornamos apenas o componente de storage
        return supabase_client.storage
        
    except Exception as e:
        st.error(f"Erro ao conectar ao serviço de armazenamento: {e}")
        return None

# --- FUNÇÃO PRINCIPAL PARA SALVAR A DENÚNCIA ---

def salvar_denuncia(nome, endereco, descricao, imagem):
    denuncia_id = uuid.uuid4()
    caminho_final_imagem = "Nenhuma imagem enviada" # Valor padrão

    # 1. Se houver imagem, faz o upload para o Supabase Storage
    if imagem is not None:
        storage_client = get_storage_client() # Esta função agora é mais robusta
        if storage_client:
            try:
                bucket_name = "denuncias" 
                
                id_curto = str(denuncia_id).split('-')[0]
                extensao = os.path.splitext(imagem.name)[1]
                nome_arquivo_storage = f"public/{id_curto}_{denuncia_id}{extensao}"

                # Este código de upload é idêntico e agora deve funcionar
                storage_client.from_(bucket_name).upload(
                    file=imagem.getvalue(), # Usando .getvalue()
                    path=nome_arquivo_storage,
                    file_options={"content-type": imagem.type}
                )
                
                url_publica = storage_client.from_(bucket_name).get_public_url(nome_arquivo_storage)
                caminho_final_imagem = url_publica

            except Exception as e:
                # Vamos imprimir o erro no console para um debug melhor
                print(f"ERRO DETALHADO DO STORAGE: {e}") 
                st.error(f"Erro ao fazer upload da imagem: {e}")
                caminho_final_imagem = "Erro no upload da imagem"
        else:
            caminho_final_imagem = "Erro ao conectar ao storage"


    # 2. Salva os metadados no Banco de Dados Neon
    conn = None
    try:
        conn = get_db_conn()
        if conn is None:
            raise Exception("Não foi possível conectar ao banco de dados.")
            
        with conn.cursor() as cur:
            sql = """
                INSERT INTO denuncias (id, nome_estabelecimento, endereco, descricao, caminho_imagem)
                VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(sql, (str(denuncia_id), nome, endereco, descricao, caminho_final_imagem))
        
        conn.commit() 
        
        # Só mostra o sucesso se a imagem foi enviada ou não havia imagem
        if "Erro" not in caminho_final_imagem:
             st.success("✅ Denúncia enviada com sucesso! Obrigado por sua colaboração.")
        else:
            # Se deu erro no upload, a denúncia foi salva mas o usuário precisa saber do erro da imagem
             st.warning("⚠️ Denúncia salva, mas o upload da imagem falhou.")

    except Exception as e:
        st.error(f"Erro ao salvar denúncia no banco de dados: {e}")
        if conn:
            conn.rollback() # Desfaz a transação em caso de erro
    finally:
        if conn:
            conn.close()

# --- RODA A INICIALIZAÇÃO DO BANCO DE DADOS ---
# (O Streamlit é inteligente e não vai rodar isso toda hora, 
# mas a função 'init_db' é segura para rodar múltiplas vezes de qualquer forma)
init_db()


# --- INTERFACE DO USUÁRIO (Código original) ---

st.title("Denuncie um Ponto de Venda Suspeito")
st.write("Sua denúncia é anônima e ajuda a vigilância sanitária a proteger a comunidade.")

with st.form(key="denuncia_form", clear_on_submit=True):
    st.subheader("Enviar Denúncia Anônima pelo Site")
    nome_estabelecimento = st.text_input("Nome do Estabelecimento (se souber)")
    endereco = st.text_area("Endereço ou Ponto de Referência")
    descricao = st.text_area("Descreva por que a bebida ou o local parece suspeito")
    foto_suspeita = st.file_uploader("Envie uma foto (opcional)", type=['jpg', 'png', 'jpeg'])

    submit_button = st.form_submit_button(label="Enviar Denúncia Anônima")

    if submit_button:
        # A mensagem de sucesso é mostrada dentro de 'salvar_denuncia'
        salvar_denuncia(nome_estabelecimento, endereco, descricao, foto_suspeita)

st.markdown("---")

# --- SEÇÃO ADICIONADA (Código original) ---
st.header("Outros Canais de Denúncia (Paraíba)")
st.warning("Utilize os canais abaixo para denúncias formais diretamente aos órgãos competentes.")

st.subheader("AGEVISA (Agência Estadual de Vigilância Sanitária)")
st.markdown(
    """
    - **Site:** [agevisa.pb.gov.br/servicos/ouvidoria](http://agevisa.pb.gov.br/servicos/ouvidoria)
    - **Telefone (Ouvidoria):** (83) 98814-7935
    """
)

st.subheader("Centro de Inteligência EstratégGica Estadual em Saúde da Paraíba")
st.markdown(
    """
    - **Telefone (Segunda a Sexta, 08h às 16h30):** (83) 99146-6771
    - **Telefone (Fins de semana e feriados):** (83) 98828-2522
    """
)

st.subheader("Autoridades Policiais")
st.info(
    "A venda de bebida adulterada é crime. Você pode acionar a Polícia para denunciar os locais de venda."
)