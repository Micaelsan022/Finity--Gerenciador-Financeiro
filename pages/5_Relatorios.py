import streamlit as st
import pandas as pd
from datetime import datetime
from charts.graficos import grafico_linha
from database.conexao import conectar

from assets.style import aplicar_estilo, aplicar_sidebar

aplicar_estilo()
aplicar_sidebar()

from services.relatorios_service import (
    receitas_por_mes,
    gastos_por_mes,
    saldo_por_mes
)

st.set_page_config(page_title="Relatórios", page_icon="📈", layout="wide")


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

st.markdown("""
    <div style="padding: 30px 0 20px 0;">
        <h1 style="margin: 0; font-size: 2em; font-weight: 800; color: #fff;">Relatórios</h1>
        <p style="margin: 4px 0 0 0; color: #888;">Análise financeira por período</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    mes = st.selectbox(
        "Mês",
        options=list(range(1, 13)),
        index=datetime.now().month - 1
    )

with col2:
    ano = st.number_input(
        "Ano",
        min_value=2020,
        max_value=2100,
        value=datetime.now().year
    )

st.markdown("---")

receitas = receitas_por_mes(mes, ano)
gastos = gastos_por_mes(mes, ano)
saldo = saldo_por_mes(mes, ano)

total_rec = sum(r[2] for r in receitas)
total_gas = sum(g[2] for g in gastos)
cor = "verde" if saldo >= 0 else "vermelho"

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total de Receitas</div>
            <div class="metric-value verde">R$ {total_rec:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total de Gastos</div>
            <div class="metric-value vermelho">R$ {total_gas:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Saldo do Período</div>
            <div class="metric-value {cor}">R$ {saldo:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.markdown("<h3 style='color:#fff;'>Receitas do Período</h3>", unsafe_allow_html=True)
    if receitas:
        df_receitas = pd.DataFrame(
            receitas,
            columns=["ID", "Descrição", "Valor", "Data", "Id_Categoria"]
        )
        st.dataframe(df_receitas[["Descrição", "Valor", "Data"]], use_container_width=True, hide_index=True)
    else:
        st.info("Nenhuma receita encontrada.")

with col_graf2:
    st.markdown("<h3 style='color:#fff;'>Gastos do Período</h3>", unsafe_allow_html=True)
    if gastos:
        df_gastos = pd.DataFrame(
            gastos,
            columns=["ID", "Descrição", "Valor", "Data", "Id_Categoria"]
        )
        st.dataframe(df_gastos[["Descrição", "Valor", "Data"]], use_container_width=True, hide_index=True)
    else:
        st.info("Nenhum gasto encontrado.")

st.markdown("---")

st.markdown("<h3 style='color:#fff;'>Evolução do Saldo</h3>", unsafe_allow_html=True)

dados_linha = []
for m in range(1, mes + 1):
    dados_linha.append({
        "mes": f"{m:02d}/{ano}",
        "saldo": saldo_por_mes(m, ano)
    })

fig_linha = grafico_linha(dados_linha)
if fig_linha:
    st.plotly_chart(fig_linha, use_container_width=True)

st.markdown("---")

st.markdown("<h3 style='color:#fff;'>Gastos por Categoria</h3>", unsafe_allow_html=True)

conn = conectar()
cursor = conn.cursor()
cursor.execute("""
    SELECT c.Nome, SUM(g.Valor)
    FROM Gastos g
    JOIN Categorias c ON g.Id_Categoria = c.Id
    WHERE strftime('%m', g.DataGasto) = ?
      AND strftime('%Y', g.DataGasto) = ?
    GROUP BY c.Nome
""", (f"{mes:02d}", str(ano)))
dados_categoria = cursor.fetchall()
conn.close()

if dados_categoria:
    df_categoria = pd.DataFrame(dados_categoria, columns=["Categoria", "Total Gasto"])
    df_categoria["Total Gasto"] = df_categoria["Total Gasto"].apply(
        lambda x: f"R$ {x:,.2f}"
    )
    st.dataframe(df_categoria, use_container_width=True, hide_index=True)
else:
    st.info("Nenhum gasto por categoria encontrado.")