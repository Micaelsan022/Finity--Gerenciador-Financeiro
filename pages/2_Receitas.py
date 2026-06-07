import streamlit as st
import pandas as pd
from datetime import datetime
from database.conexao import conectar

st.set_page_config(page_title="Receitas", page_icon="💰", layout="wide")

st.title("💰 Receitas")

# Customização da barra lateral
st.sidebar.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="margin: 0; font-size: 2.5em;">💸 Finity</h1>
        <p style="margin: 5px 0 0 0; color: #888; font-size: 0.9em;">Gerenciador financeiro</p>
    </div>
    <hr style="margin: 20px 0;">
""", unsafe_allow_html=True)

# Função para obter categorias de receita
def obter_categorias_receita():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Nome FROM Categorias WHERE Tipo = 'Receita' ORDER BY Nome")
    resultado = cursor.fetchall()
    conn.close()
    return {row[1]: row[0] for row in resultado} if resultado else {}

# Função para inserir receita
def inserir_receita(descricao, valor, data, id_categoria):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Receitas (Descricao, Valor, DataReceita, Id_Categoria)
            VALUES (?, ?, ?, ?)
        """, (descricao, valor, data, id_categoria))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir receita: {e}")
        return False
    finally:
        conn.close()

# Função para obter todas as receitas
def obter_receitas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.Id, r.Descricao, r.Valor, r.DataReceita, c.Nome
        FROM Receitas r
        JOIN Categorias c ON r.Id_Categoria = c.Id
        ORDER BY r.DataReceita DESC
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado

# Função para deletar receita
def deletar_receita(id_receita):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Receitas WHERE Id = ?", (id_receita,))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao deletar receita: {e}")
        return False
    finally:
        conn.close()

# Layout em duas colunas
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("➕ Nova Receita")
    
    with st.form(key="form_receita"):
        descricao = st.text_input("Descrição", placeholder="Ex: Salário, Freelance, Bônus...")
        valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
        data = st.date_input("Data", value=datetime.now())
        
        categorias = obter_categorias_receita()
        if not categorias:
            st.warning("Nenhuma categoria de receita cadastrada. Adicione categorias primeiro.")
            nome_categoria = st.text_input("Nova categoria")
        else:
            nome_categoria = st.selectbox("Categoria", options=list(categorias.keys()))
        
        submitted = st.form_submit_button("💾 Salvar Receita", use_container_width=True)
        
        if submitted:
            if descricao and valor > 0:
                if not categorias and nome_categoria:
                    # Criar nova categoria
                    conn = conectar()
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO Categorias (Nome, Tipo)
                        VALUES (?, 'Receita')
                    """, (nome_categoria,))
                    conn.commit()
                    cursor.execute("SELECT Id FROM Categorias WHERE Nome = ? AND Tipo = 'Receita'", (nome_categoria,))
                    id_categoria = cursor.fetchone()[0]
                    conn.close()
                elif categorias:
                    id_categoria = categorias[nome_categoria]
                else:
                    st.error("Selecione ou crie uma categoria")
                    id_categoria = None
                
                if id_categoria:
                    if inserir_receita(descricao, valor, data, id_categoria):
                        st.success("✅ Receita adicionada com sucesso!")
                        st.rerun()
                    else:
                        st.error("❌ Erro ao adicionar receita")
            else:
                st.error("Preencha todos os campos corretamente")

with col2:
    st.subheader("📋 Histórico de Receitas")
    
    receitas = obter_receitas()
    
    if receitas:
        # Criar DataFrame
        df = pd.DataFrame(
            receitas,
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
        st.subheader("🗑️ Excluir Receita")
        
        receitas_para_deletar = {f"{r[1]} - R$ {r[2]:.2f} ({r[3]})": r[0] for r in receitas}
        receita_selecionada = st.selectbox("Selecione a receita para deletar", 
                                           options=list(receitas_para_deletar.keys()),
                                           key="delete_receita")
        
        if st.button("🗑️ Deletar Receita Selecionada", use_container_width=True):
            id_receita = receitas_para_deletar[receita_selecionada]
            if deletar_receita(id_receita):
                st.success("✅ Receita deletada com sucesso!")
                st.rerun()
            else:
                st.error("❌ Erro ao deletar receita")
    else:
        st.info("📭 Nenhuma receita cadastrada ainda. Comece adicionando uma receita!")
