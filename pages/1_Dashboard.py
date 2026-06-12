import streamlit as st
from services.calculos import total_receitas, total_gastos, saldo_atual, gastos_por_categoria
from services.analise_financeira import analisar_gastos
from charts.graficos import grafico_pizza, grafico_barras

from assets.style import aplicar_estilo, aplicar_sidebar

aplicar_estilo()
aplicar_sidebar()

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")


st.markdown("""
    <style>
        .metric-card {
            background: linear-gradient(135deg, #1a1a1a, #222222);
            border: 1px solid #2a2a2a;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
        }
        .metric-value {
            font-size: 1.8em;
            font-weight: bold;
            margin: 8px 0;
        }
        .metric-label {
            font-size: 0.85em;
            color: #888888;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .verde { color: #2ECC71; }
        .vermelho { color: #E74C3C; }
    </style>
""", unsafe_allow_html=True)

receitas = total_receitas()
gastos = total_gastos()
saldo = saldo_atual()

st.markdown("""
    <div style="padding: 30px 0 20px 0;">
        <h1 style="margin: 0; font-size: 2em; font-weight: 800; color: #fff;">Dashboard</h1>
        <p style="margin: 4px 0 0 0; color: #888;">Visão geral das suas finanças</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total de Receitas</div>
            <div class="metric-value verde">R$ {receitas:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total de Gastos</div>
            <div class="metric-value vermelho">R$ {gastos:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    cor = "verde" if saldo >= 0 else "vermelho"
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Saldo Atual</div>
            <div class="metric-value {cor}">R$ {saldo:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.markdown("<h3 style='color:#fff;'>Gastos por Categoria</h3>", unsafe_allow_html=True)
    dados_categoria = gastos_por_categoria()
    if dados_categoria:
        fig_pizza = grafico_pizza(dados_categoria)
        st.plotly_chart(fig_pizza, use_container_width=True)
    else:
        st.info("Nenhum gasto cadastrado ainda.")

with col_graf2:
    st.markdown("<h3 style='color:#fff;'>Receitas x Gastos</h3>", unsafe_allow_html=True)
    fig_barras = grafico_barras(receitas, gastos)
    st.plotly_chart(fig_barras, use_container_width=True)

st.markdown("---")

st.markdown("<h3 style='color:#fff;'>Alertas Financeiros</h3>", unsafe_allow_html=True)
alertas = analisar_gastos()

if alertas:
    for alerta in alertas:
        st.warning(alerta)
else:
    st.success("Seus gastos estao sob controle!")