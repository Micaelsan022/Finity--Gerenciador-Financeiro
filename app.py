import streamlit as st
from services.calculos import total_receitas, total_gastos, saldo_atual

st.set_page_config(
    page_title="Finity - Gerenciador Financeiro",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #0f0f0f;
            border-right: 1px solid #1a1a1a;
        }
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
        }
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

st.sidebar.markdown("""
    <div style="padding: 24px 16px 16px 16px;">
        <p style="margin: 0; font-size: 0.75em; color: #555; text-transform: uppercase; letter-spacing: 2px;">Gerenciador Financeiro</p>
        <h1 style="margin: 4px 0 0 0; font-size: 2em; color: #2ECC71; font-weight: 800;">Finity</h1>
    </div>
    <hr style="border: none; border-top: 1px solid #222; margin: 0 16px 16px 16px;">
""", unsafe_allow_html=True)

receitas = total_receitas()
gastos = total_gastos()
saldo = saldo_atual()

st.markdown("""
    <div style="padding: 40px 0 20px 0;">
        <p style="margin: 0; font-size: 0.8em; color: #888; text-transform: uppercase; letter-spacing: 3px;">Bem-vindo ao</p>
        <h1 style="margin: 4px 0 0 0; font-size: 3em; font-weight: 800; color: #2ECC71;">Finity</h1>
        <p style="margin: 8px 0 0 0; color: #aaa; font-size: 1em;">Seu gerenciador financeiro pessoal</p>
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

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h3 style='color:#fff;'>Como usar o Finity</h3>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
        <div class="metric-card">
            <div style="font-size:2em;">💰</div>
            <div style="font-weight:bold;margin:8px 0;color:#fff;">Receitas</div>
            <div style="color:#888;font-size:0.85em;">Registre todas as suas entradas de dinheiro</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="metric-card">
            <div style="font-size:2em;">💸</div>
            <div style="font-weight:bold;margin:8px 0;color:#fff;">Gastos</div>
            <div style="color:#888;font-size:0.85em;">Monitore seus gastos por categoria</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="metric-card">
            <div style="font-size:2em;">🎯</div>
            <div style="font-weight:bold;margin:8px 0;color:#fff;">Metas</div>
            <div style="color:#888;font-size:0.85em;">Defina e acompanhe seus objetivos</div>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
        <div class="metric-card">
            <div style="font-size:2em;">📊</div>
            <div style="font-weight:bold;margin:8px 0;color:#fff;">Relatórios</div>
            <div style="color:#888;font-size:0.85em;">Visualize seus dados financeiros</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align:center;color:#333;font-size:0.8em;padding:20px 0;">
        Finity v1.0.0 — Projeto Acadêmico
    </div>
""", unsafe_allow_html=True)