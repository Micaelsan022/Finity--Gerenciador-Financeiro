import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Finity - Gerenciador Financeiro",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Customização da barra lateral
st.sidebar.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="margin: 0; font-size: 2.5em;">💸 Finity</h1>
        <p style="margin: 5px 0 0 0; color: #888; font-size: 0.9em;">Gerenciador financeiro</p>
    </div>
    <hr style="margin: 20px 0;">
""", unsafe_allow_html=True)

# Conteúdo principal
st.title("Bem-vindo ao Finity! 💸")

st.markdown("""
    ### 🎯 O seu assistente financeiro pessoal
    
    Finity é um gerenciador financeiro inteligente que ajuda você a:
    
    - 💰 **Registrar Receitas** - Acompanhe todas as suas entradas de dinheiro
    - 💸 **Controlar Gastos** - Monitore seus gastos por categoria
    - 🎯 **Definir Metas** - Alcance seus objetivos financeiros
    - 📊 **Visualizar Relatórios** - Tenha insights sobre seu comportamento financeiro
    
    ---
    
    ### 🚀 Como começar?
    
    Use o menu lateral para navegar entre as seções. Comece adicionando suas receitas e gastos!
    
    ---
    
    ### 💡 Dicas
    
    - Mantenha seus dados atualizados para ter relatórios precisos
    - Crie categorias personalizadas de acordo com sua rotina
    - Defina metas realistas para motivar seus objetivos
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📚 **Dúvidas?** Consulte o README do projeto")

with col2:
    st.success("✅ **Versão** 1.0.0")

with col3:
    st.warning("⚠️ **Dica:** Faça backup regular do seu banco de dados")
