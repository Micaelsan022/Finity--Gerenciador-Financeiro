import streamlit as st

from services.calculos import (
    total_receitas,
    total_gastos,
    saldo_atual,
    gastos_por_categoria
)

from services.analise_financeira import analisar_gastos

from charts.graficos import (
    grafico_pizza,
    grafico_barras
)

st.title("Dashboard Financeiro")

# Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Saldo Atual", f"R$ {saldo_atual():,.2f}")

with col2:
    st.metric("Total Receitas", f"R$ {total_receitas():,.2f}")

with col3:
    st.metric("Total Gastos", f"R$ {total_gastos():,.2f}")

st.divider()

# Gráfico de Pizza
st.subheader("Gastos por Categoria")

dados_categoria = gastos_por_categoria()

if dados_categoria:
    fig_pizza = grafico_pizza(dados_categoria)
    st.plotly_chart(fig_pizza, width="stretch")
else:
    st.info("Nenhum gasto cadastrado.")

st.divider()

# Gráfico de Barras
st.subheader("Receitas x Gastos")

fig_barras = grafico_barras(
    total_receitas(),
    total_gastos()
)

st.plotly_chart(fig_barras, use_container_width=True)

st.divider()

# Alertas Financeiros
st.subheader("Alertas Financeiros")

alertas = analisar_gastos()

if alertas:
    for alerta in alertas:
        st.warning(alerta)
else:
    st.success("Nenhum alerta financeiro encontrado.")