import streamlit as st
import pandas as pd

# Título da página
st.title("Hipóteses Diagnósticas")
st.write("Pesquise a sigla de um exame para ver o nome e a hipótese diagnóstica.")

# ---
# Lendo o arquivo Excel.
# Substitua 'seu_arquivo.xlsx' pelo nome real da sua planilha
# e certifique-se de que a planilha está na mesma pasta que este script.
try:
    df = pd.read_excel('HIPOTESES.xlsx')
except FileNotFoundError:
    st.error("Arquivo 'HIPOTESES.xlsx' não encontrado. Por favor, coloque a planilha na mesma pasta deste script.")
    st.stop()

# Campo de busca
sigla_busca = st.text_input("Digite a sigla do exame").upper()

# Botão de busca
if st.button("Buscar"):
    if sigla_busca:
        # Lógica para encontrar a sigla na planilha
        resultado = df[df['SIGLA'].str.upper() == sigla_busca]
        
        if not resultado.empty:
            # Exibe o resultado se a sigla for encontrada
            exame_encontrado = resultado['EXAME'].iloc[0]
            hipotese_encontrada = resultado['HIPÓTESE DIAGNÓSTICA'].iloc[0]
            
            st.markdown("---")
            st.markdown(f"**Exame:** {exame_encontrado}")
            st.markdown(f"**Hipótese Diagnóstica:**")
            st.info(hipotese_encontrada)
        else:
            # Mensagem se a sigla não for encontrada
            st.warning("Sigla não encontrada. Verifique se digitou corretamente.")
    else:
        st.error("Por favor, digite a sigla para buscar.")