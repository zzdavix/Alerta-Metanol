# --- FLUXO DE CONVERSAS ---

# ==============================================================================
#                             1. FLUXO DE EMERGÊNCIA
# ==============================================================================

# Emergência - Inicial
emer_resp = "A intoxicação por metanol é uma emergência grave. Você ou alguém próximo está apresentando sintomas agora?"

# Emergência - Botões
emer_sim_grave_botao = "Sim, sintomas graves"
emer_sim_inicial_botao = "Sim, sintomas iniciais"
emer_nao_botao = "Não, mas bebi algo suspeito"
emer_todos_botao = "Quais são todos os sintomas?"

#Emergência -> Sintomas
sint_grave_resp = "Ligue imediatamente para o SAMU (192) ou vá para a emergência mais próxima." \
" \n\nEnquanto espera: \n1. NÃO beba mais nada. \n2. NÃO tente vomitar."\
" \n3. Se possível, guarde uma amostra da bebida suspeita para análise."

sint_inicial_resp = "Esses sintomas podem evoluir. Os sintomas graves (como problemas na visão) podem demorar de 12 a 24 horas." \
" Monitore atentamente. Se os sintomas piorarem ou se você tiver certeza que a bebida era suspeita, procure um médico imediatamente."

sint_nao_resp = "Fique alerta. Os sintomas podem demorar até 24 horas para aparecer." \
" O sinal mais claro de intoxicação por metanol (e que a difere da ressaca comum) são alterações na visão (vista turva, flashes, 'tempestade de neve')." \
" Se isso ocorrer, é uma emergência." \

sint_todos_resp = (
    "Sintomas iniciais (6-12 horas após ingestão):\n"
    "- Dor de cabeça\n"
    "- Tontura\n"
    "- Náusea e vômito\n"
    "- Dor abdominal\n\n"
    "Sintomas graves (12-24 horas após ingestão):\n"
    "- Dificuldade para respirar\n"
    "- Confusão mental\n"
    "- Alterações na visão (vista turva, flashes, 'tempestade de neve')\n"
    "- Convulsões\n"
    "- Coma\n\n"
    "Se você ou alguém próximo apresentar esses sintomas após consumir bebidas alcoólicas, procure ajuda médica imediatamente."
)

# ==============================================================================
#                                  2. PREVENÇÃO
# ==============================================================================

# Prevenção - Inicial
prev_resp = "Sobre o que você quer aprender primeiro?"

# Prevenção - Botões
prev_como_botao = "Como me previnir (em bares, festas, etc.)"
prev_identificar_botao = "Como identificar uma bebida falsa (rótulos, garrafa)"
prev_oqe_botao = "O que é Metanol?"

# Prevenção -> O que é Metanol?
prev_oqe_resp = "É um tipo de álcool tóxico, usado na indústria (como solvente, combustível). Ele NUNCA deve ser bebido." \
" Algumas bebidas falsificadas o utilizam no lugar do álcool comum (etanol) por ser mais barato, causando envenenamento."

# Prevenção -> Como se Prevenir
prev_como_resp = "O principal é a procedência. O que você quer saber?"

# Prevenção -> Como se Prevenir - Botões
prev_como_bares_botao = "Dicas em Bares e Festas"
prev_como_garrafas_botao = "Dicas ao Comprar Garrafas"

# Prevenção -> Como se Prevenir - Respostas
prev_como_bares_resp = "Evite 'shots' de origem desconhecida ou 'open bar' muito barato." \
" Prefira bebidas lacradas (cerveja, garrafas individuais) ou veja o bartender preparar seu drink com uma garrafa de marca conhecida."

prev_como_garrafas_resp = "Desconfie de preços muito baixos. Compre em mercados e distribuidoras oficiais. Verifique sempre o lacre e a qualidade do rótulo."

# Prevenção -> Como Identificar
prev_identificar_resp = "É difícil ter 100% de certeza, mas há sinais claros. O que você quer checar?"

# Prevenção -> Como Identificar - Botões
prev_id_rotulo_botao = "Sinais no Rótulo e Lacre"
prev_id_liquido_botao = "Sinais no Líquido"
prev_id_cheiro_botao = "Dá para saber pelo cheiro ou gosto?"

# Prevenção -> Como Identificar - Respostas
prev_id_rotulo_resp = "Procure por: Rótulos tortos, com cola aparente, erros de português ou impressão de baixa qualidade." \
" O lacre não deve girar em falso ou parecer danificado."\

prev_id_liquido_resp = "Verifique se a cor está correta (compare com fotos oficiais) e se há partículas ou sujeira suspensas no líquido."\


prev_id_cheiro_resp = "**NÃO É RECOMENDADO PROVAR PARA TESTAR.** O metanol tem cheiro e gosto muito similares ao álcool comum (etanol). Confie nos sinais visuais da embalagem."


# ==============================================================================
#                                  3. DENÚNCIA
# ==============================================================================

# Denúncia - Inicial
denuncia_resp = "Sua denúncia é fundamental para proteger outras pessoas. Como você prefere agir?"

# Denúncia - Botões
denuncia_form_botao = "Quero denunciar um estabelecimento (Online)"
denuncia_telefones_botao = "Quero os telefones de órgãos públicos"
denuncia_o_que_precisa_botao = "O que preciso para fazer uma boa denúncia?"

# Denúncia -> Respostas
denuncia_form_resp = "Excelente. Por favor, acesse nossa página 'Denúncia' para preencher o formulário seguro. Tente ter em mãos o nome e o endereço do local."

denuncia_telefones_resp = "Claro. Para casos urgentes ou denúncias formais, ligue para: \n* Vigilância Sanitária: (83) 98814-7935" \
" \n * Cieges-PB: Segunda a Sexta, 08h às 16h30: (83) 99146-6771. Fins de semana e feriados: (83) 98828-2522"

denuncia_o_que_precisa_resp = "Quanto mais informações, melhor. Tente anotar: \n1. Nome e Endereço do local. \n2. Data e hora do ocorrido. \n3. Nome da bebida (se souber)." \
" \n4. Se possível, guarde a garrafa ou comprovantes de pagamento."\

# ==============================================================================
#                              4. OUTROS ASSUNTOS
# ==============================================================================

# Outros - Inicial
outros_resp = "Selecione o que você busca:"

# Outros - Botões
outros_noticias_botao = "Notícias Recentes"
outros_contato_botao = "Entrar em Contato / Sugestões"

# Outros -> Respostas
outros_noticias_resp = "Para ver os últimos casos e alertas sobre bebidas contaminadas, acesse nossa página 'Notícias Recentes'."

outros_contato_resp = "Para sugestões, críticas ou parcerias, acesse nossa página 'Contato'."