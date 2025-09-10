import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- Título e descrição da página ---
st.title("Gerador de Texto de Negativa")
st.write("Preencha os campos abaixo para gerar o texto de notificação de negativa.")
st.markdown("---")

# --- Campos de entrada de dados ---
nome_cliente = st.text_input("Nome do Cliente")
marca = st.text_input("Sua Marca (ex: Fleury, A+)")
convenio = st.text_input("Nome do Convênio")
data_agendamento = st.text_input("Data do Agendamento (ex: 24/08/2025)")

# Criando um espaço para adicionar vários exames
st.markdown("---")
st.write("## Exames não autorizados")
exames = st.text_area("Digite cada exame em uma linha separada.")

# --- Lógica para gerar o texto ---
if st.button("Gerar Texto"):
    if nome_cliente and convenio and data_agendamento and exames:
        # Divide os exames por linha e formata com bullets
        lista_exames = [f"• {exame.strip()}" for exame in exames.split('\n') if exame.strip()]
        exames_formatados = "\n".join(lista_exames)

        # Monta o texto completo
        st.session_state['texto_gerado'] = f"""Olá, {nome_cliente}!
Somos do {marca}
O convênio {convenio} *não autorizou* estes exames do agendamento de {data_agendamento}:
{exames_formatados}

Para mais informações, entre em contato com sua operadora de saúde.

❗ Se quiser reagendar ou cancelar este agendamento, acesse o nosso app ou site."""

# --- Exibir o texto gerado e o botão de copiar ---
if 'texto_gerado' in st.session_state:
    st.markdown("---")
    st.markdown("### Texto Gerado:")
    st.text_area("Selecione e copie o texto abaixo:", value=st.session_state['texto_gerado'], height=350, key='texto_para_copiar')

    copy_button = st.button("Copiar Texto Gerado")
    
    if copy_button:
        components.html(
            """
            <script>
                var textarea = document.querySelector('textarea[data-testid="stTextarea"]');
                if (textarea) {
                    textarea.select();
                    document.execCommand('copy');
                }
            </script>
            """,
            height=0,
            width=0,
        )
        st.success("Texto copiado para a área de transferência!")