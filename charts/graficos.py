import plotly.express as px
import plotly.graph_objects as go

def grafico_pizza(dados):
    if not dados:
        return None

    categorias = [item["categoria"] for item in dados]
    valores = [item["total"] for item in dados]

    fig = px.pie(
        names=categorias,
        values=valores,
        title="Gastos por Categoria",
        color_discrete_sequence=["#1A6B4A", "#2ECC71", "#27AE60", "#145A32", "#82E0AA"]
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )
    return fig

def grafico_barras(total_receitas, total_gastos):
    fig = go.Figure(data=[
        go.Bar(name="Receitas", x=["Receitas"], y=[total_receitas], marker_color="#2ECC71"),
        go.Bar(name="Gastos", x=["Gastos"], y=[total_gastos], marker_color="#E74C3C")
    ])
    fig.update_layout(
        title="Receitas vs Gastos",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        barmode="group"
    )
    return fig

def grafico_linha(dados):
    if not dados:
        return None

    meses = [item["mes"] for item in dados]
    saldos = [item["saldo"] for item in dados]

    fig = px.line(
        x=meses,
        y=saldos,
        title="Evolução do Saldo",
        markers=True,
        color_discrete_sequence=["#2ECC71"]
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis_title="Mês",
        yaxis_title="Saldo (R$)"
    )
    return fig