import streamlit as st

# Configuração da página (opcional, mas bom para consistência)
st.set_page_config(
    page_title="Como se Prevenir - Alerta Metanol",
    page_icon="🛡️",
    layout="wide"
)

# Título da Página
st.title("Como se Prevenir")
st.markdown("Dicas para evitar o consumo de bebidas falsificadas.")

st.markdown("---")

# Dividir a página em duas colunas para o "Faça" e "Não Faça"
col1, col2 = st.columns(2)

# Coluna da esquerda: O que FAZER
with col1:
    st.subheader("👍 FAÇA")
    
    st.success(
        "**Compre em locais de confiança:** "
        "Dê preferência a supermercados, distribuidoras registradas e lojas conveniadas. "
        "Esses estabelecimentos têm um controle maior sobre a origem de seus produtos."
    )
    
    st.success(
        "**Na dúvida, pergunte:** "
        "Em bares, restaurantes ou festas, se não tiver certeza, pergunte ao responsável qual a marca e a procedência da bebida que será servida no seu drink."
    )

    st.success(
        "**Se desconfiar, não beba:** "
        "Se a garrafa parecer violada, o rótulo estiver estranho ou o preço for bom demais para ser verdade, "
        "recuse a bebida. Escolha outra opção que você confie."
    )
    
    st.success(
        "**Converse com seus amigos:** "
        "Espalhe a informação. Um alerta seu pode salvar a vida de alguém próximo. "
        "Compartilhe o link deste site."
    )

# Coluna da direita: O que NÃO FAZER
with col2:
    st.subheader("👎 NÃO FAÇA")
    
    st.error(
        "**Nunca compre pelo preço baixo:** "
        "Bebidas falsificadas são vendidas por valores muito abaixo do mercado para atrair consumidores. "
        "O barato pode custar sua visão ou sua vida."
    )
    
    st.error(
        "**Não compre de fontes duvidosas:** "
        "Evite comprar bebidas de vendedores ambulantes, em festas clandestinas ou através de "
        "anúncios suspeitos em redes sociais e aplicativos de mensagem."
    )
    
    st.error(
        "**Evite drinks prontos de origem desconhecida:** "
        "Cuidado com 'batidas' e 'drinks' vendidos em garrafas PET ou recipientes sem rótulo. "
        "Você não sabe o que foi usado na preparação."
    )
    
    st.error(
        "**Não ignore os sinais:** "
        "Se um amigo passar mal após beber, não assuma que é apenas uma ressaca. "
        "Fique atento aos sintomas de alerta e não hesite em procurar ajuda."
    )

st.markdown("---")

# Mensagem final de reforço
st.info("Lembre-se: A melhor forma de garantir a segurança é consumir produtos de origem conhecida e verificada.")