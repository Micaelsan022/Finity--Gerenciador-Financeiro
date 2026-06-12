import streamlit as st
import pandas as pd
from datetime import datetime
from database.conexao import conectar
from services.analise_financeira import analisar_gastos

from assets.style import aplicar_estilo, aplicar_sidebar

aplicar_estilo()
aplicar_sidebar()

st.set_page_config(page_title="Gastos", layout="wide")

st.title("Gastos")


# Função para obter categorias de gasto
def obter_categorias_gasto():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Nome FROM Categorias WHERE Tipo = 'Gasto' ORDER BY Nome")
    resultado = cursor.fetchall()
    conn.close()
    return {row[1]: row[0] for row in resultado} if resultado else {}

# Função para inserir gasto
def inserir_gasto(descricao, valor, data, id_categoria):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Gastos (Descricao, Valor, DataGasto, Id_Categoria)
            VALUES (?, ?, ?, ?)
        """, (descricao, valor, data, id_categoria))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir gasto: {e}")
        return False
    finally:
        conn.close()

# Função para obter todos os gastos
def obter_gastos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT g.Id, g.Descricao, g.Valor, g.DataGasto, c.Nome
        FROM Gastos g
        JOIN Categorias c ON g.Id_Categoria = c.Id
        ORDER BY g.DataGasto DESC
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado

# Função para deletar gasto
def deletar_gasto(id_gasto):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Gastos WHERE Id = ?", (id_gasto,))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao deletar gasto: {e}")
        return False
    finally:
        conn.close()

# Exibir alertas
st.subheader("🚨 Alertas Financeiros")
alertas = analisar_gastos()

if alertas:
    for alerta in alertas:
        st.warning(alerta)
else:
    st.info("✅ Seus gastos estão sob controle!")

st.markdown("---")

# Layout em duas colunas
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Novo Gasto")
    
    with st.form(key="form_gasto"):
        descricao = st.text_input("Descrição", placeholder="Ex: Supermercado, Combustível, Conta...")
        valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
        data = st.date_input("Data", value=datetime.now())
        
        categorias = obter_categorias_gasto()
        if not categorias:
            st.warning("Nenhuma categoria de gasto cadastrada. Adicione categorias primeiro.")
            nome_categoria = st.text_input("Nova categoria")
        else:
            nome_categoria = st.selectbox("Categoria", options=list(categorias.keys()))
        
        submitted = st.form_submit_button("💾 Salvar Gasto", use_container_width=True)
        
        if submitted:
            if descricao and valor > 0:
                if not categorias and nome_categoria:
                    # Criar nova categoria
                    conn = conectar()
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO Categorias (Nome, Tipo)
                        VALUES (?, 'Gasto')
                    """, (nome_categoria,))
                    conn.commit()
                    cursor.execute("SELECT Id FROM Categorias WHERE Nome = ? AND Tipo = 'Gasto'", (nome_categoria,))
                    id_categoria = cursor.fetchone()[0]
                    conn.close()
                elif categorias:
                    id_categoria = categorias[nome_categoria]
                else:
                    st.error("Selecione ou crie uma categoria")
                    id_categoria = None
                
                if id_categoria:
                    if inserir_gasto(descricao, valor, data, id_categoria):
                        st.success("✅ Gasto adicionado com sucesso!")
                        st.rerun()
                    else:
                        st.error("❌ Erro ao adicionar gasto")
            else:
                st.error("Preencha todos os campos corretamente")

with col2:
    st.subheader("📋 Histórico de Gastos")
    
    gastos = obter_gastos()
    
    if gastos:
        # Criar DataFrame
        df = pd.DataFrame(
            gastos,
            columns=["ID", "Descrição", "Valor", "Data", "Categoria"]
        )
        
        # Formatar coluna de valor
        df["Valor"] = df["Valor"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "_").replace(".", ",").replace("_", "."))
        
        # Exibir tabela
        st.dataframe(
            df[["Descrição", "Valor", "Data", "Categoria"]],
            use_container_width=True,
            hide_index=True
        )
        
        # Adicionar opção de exclusão
        st.markdown("---")
        st.subheader("🗑️ Excluir Gasto")
        
        gastos_para_deletar = {f"{g[1]} - R$ {g[2]:.2f} ({g[3]})": g[0] for g in gastos}
        gasto_selecionado = st.selectbox("Selecione o gasto para deletar", 
                                        options=list(gastos_para_deletar.keys()),
                                        key="delete_gasto")
        
        if st.button("🗑️ Deletar Gasto Selecionado", use_container_width=True):
            id_gasto = gastos_para_deletar[gasto_selecionado]
            if deletar_gasto(id_gasto):
                st.success("✅ Gasto deletado com sucesso!")
                st.rerun()
            else:
                st.error("❌ Erro ao deletar gasto")
    else:
        st.info("📭 Nenhum gasto cadastrado ainda. Comece adicionando um gasto!")
