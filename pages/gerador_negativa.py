import streamlit as st

# --- Título e descrição da página ---
st.title("Gerador de Texto de Negativa")
st.write("Preencha os campos abaixo para gerar o texto de notificação de negativa.")
st.markdown("---")

# --- Campos de entrada de dados ---
nome_cliente = st.text_input("Nome do Cliente")
marca = st.text_input("Marca (ex: Fleury, A+)")
convenio = st.text_input("Nome do Convênio")
data_agendamento = st.text_input("Data do Agendamento (ex: 24/08/2025)")

# Criando um espaço para adicionar vários exames
st.markdown("---")
st.write("## Exames não autorizados")
exames = st.text_area("Digite cada exame em uma linha separada.")

# --- Botão para gerar o texto ---
if st.button("Gerar Texto"):
    if nome_cliente and convenio and data_agendamento and exames:
        # Divide os exames por linha e formata com bullets
        lista_exames = [f"• *{exame.strip()}*" for exame in exames.split('\n') if exame.strip()]
        exames_formatados = "\n".join(lista_exames)

        # Monta o texto completo
        texto_gerado = f"""Olá, *{nome_cliente}*!
Somos do *{marca}*
O convênio *{convenio}* não autorizou estes exames do agendamento de *{data_agendamento}*:
{exames_formatados}

Para mais informações, entre em contato com sua operadora de saúde.

❗ Se quiser reagendar ou cancelar este agendamento, acesse o nosso app ou site."""

        # Exibe o texto gerado em uma caixa de texto para fácil cópia
        st.markdown("### Texto Gerado:")
        st.text_area("Copie o texto abaixo:", value=texto_gerado, height=350)
    else:
        st.error("Por favor, preencha todos os campos para gerar o texto.")