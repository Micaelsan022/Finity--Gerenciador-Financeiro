import streamlit as st
import pandas as pd
from datetime import datetime
from charts.graficos import grafico_linha
from database.conexao import conectar

from services.relatorios_service import (
    receitas_por_mes,
    gastos_por_mes,
    saldo_por_mes
)

st.set_page_config(page_title="Relatorios", layout="wide")

st.title("Relatorios Financeiros")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    mes = st.selectbox(
        "Mes",
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

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total de Receitas",
        f"R$ {sum(r[2] for r in receitas):,.2f}"
    )

with col2:
    st.metric(
        "Total de Gastos",
        f"R$ {sum(g[2] for g in gastos):,.2f}"
    )

with col3:
    st.metric(
        "Saldo",
        f"R$ {saldo:,.2f}"
    )

st.markdown("---")

st.subheader("Receitas do Periodo")

if receitas:
    df_receitas = pd.DataFrame(
        receitas,
        columns=["ID", "Descricao", "Valor", "Data", "Categoria"]
    )

    st.dataframe(
        df_receitas,
        width="stretch",
        hide_index=True
    )
else:
    st.info("Nenhuma receita encontrada.")

st.markdown("---")

st.subheader("Gastos do Periodo")

if gastos:
    df_gastos = pd.DataFrame(
        gastos,
        columns=["ID", "Descricao", "Valor", "Data", "Categoria"]
    )

    st.dataframe(
        df_gastos,
        width="stretch",
        hide_index=True
    )
else:
    st.info("Nenhum gasto encontrado.")

st.markdown("---")

st.subheader("Evolução do Saldo")

dados_linha = []

for m in range(1, mes + 1):
    saldo_mes = saldo_por_mes(m, ano)

    dados_linha.append(
        {
            "mes": f"{m:02d}/{ano}",
            "saldo": saldo_mes
        }
    )

fig_linha = grafico_linha(dados_linha)

if fig_linha:
    st.plotly_chart(fig_linha, width="stretch")

st.markdown("---")

st.subheader("Gastos por Categoria")

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
    df_categoria = pd.DataFrame(
        dados_categoria,
        columns=["Categoria", "Total Gasto"]
    )

    st.dataframe(
        df_categoria,
        width="stretch",
        hide_index=True
    )
else:
    st.info("Nenhum gasto por categoria encontrado.")