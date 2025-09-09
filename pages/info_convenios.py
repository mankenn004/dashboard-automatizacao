import streamlit as st
import pandas as pd

st.title("Informações de Convênios")
st.write("Pesquise por convênio para ver suas informações.")

# Lendo o arquivo Excel
try:
    df_convenios = pd.read_excel('Infoconvenios.xlsx')
except FileNotFoundError:
    st.error("Arquivo 'Infoconvenios.xlsx' não encontrado. Por favor, adicione a planilha à pasta principal do seu projeto.")
    st.stop()

# Campo de busca para o convênio
convenio_busca = st.text_input("Digite o nome do convênio").upper()

# Botão de busca
if st.button("Buscar"):
    if convenio_busca:
        # Lógica para encontrar o convênio na planilha
        resultado_convenio = df_convenios[df_convenios['CONVENIO'].str.upper() == convenio_busca]
        
        if not resultado_convenio.empty:
            # Exibe o resultado se o convênio for encontrado
            st.markdown("---")
            st.markdown(f"**Convênio:** {resultado_convenio.iloc[0]['CONVENIO']}")
            st.markdown(f"**Informação:** {resultado_convenio.iloc[0]['INFORMAÇÃO']}")
        else:
            st.warning("Convênio não encontrado. Verifique se o nome foi digitado corretamente.")
    else:
        st.error("Por favor, digite o nome do convênio para buscar.")