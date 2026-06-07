import streamlit as st
import pandas as pd
from datetime import datetime
from database.conexao import conectar

st.set_page_config(page_title="Metas", page_icon="🎯", layout="wide")

st.title("🎯 Metas Financeiras")

# Customização da barra lateral
st.sidebar.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="margin: 0; font-size: 2.5em;">💸 Finity</h1>
        <p style="margin: 5px 0 0 0; color: #888; font-size: 0.9em;">Gerenciador financeiro</p>
    </div>
    <hr style="margin: 20px 0;">
""", unsafe_allow_html=True)

# Função para inserir meta
def inserir_meta(nome, valor_alvo, prazo):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Metas (Nome, Valor_Alvo, Valor_Atual, Prazo)
            VALUES (?, ?, 0, ?)
        """, (nome, valor_alvo, prazo))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir meta: {e}")
        return False
    finally:
        conn.close()

# Função para obter todas as metas
def obter_metas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Id, Nome, Valor_Alvo, Valor_Atual, Prazo, Criada_Em
        FROM Metas
        ORDER BY Prazo ASC
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado

# Função para deletar meta
def deletar_meta(id_meta):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Metas WHERE Id = ?", (id_meta,))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao deletar meta: {e}")
        return False
    finally:
        conn.close()

# Função para atualizar valor atual da meta
def atualizar_valor_meta(id_meta, novo_valor):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE Metas SET Valor_Atual = ? WHERE Id = ?
        """, (novo_valor, id_meta))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao atualizar meta: {e}")
        return False
    finally:
        conn.close()

# Formulário para criar nova meta
st.subheader("➕ Criar Nova Meta")

with st.form(key="form_meta"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        nome = st.text_input("Nome da Meta", placeholder="Ex: Viagem, Carro, Casa...")
    
    with col2:
        valor_alvo = st.number_input("Valor Alvo (R$)", min_value=0.0, step=0.01)
    
    with col3:
        prazo = st.date_input("Prazo", value=datetime.now())
    
    submitted = st.form_submit_button("💾 Criar Meta", use_container_width=True)
    
    if submitted:
        if nome and valor_alvo > 0:
            if inserir_meta(nome, valor_alvo, prazo):
                st.success("✅ Meta criada com sucesso!")
                st.rerun()
            else:
                st.error("❌ Erro ao criar meta")
        else:
            st.error("Preencha todos os campos corretamente")

st.markdown("---")

# Exibir metas em cards
st.subheader("📊 Suas Metas")

metas = obter_metas()

if metas:
    for meta in metas:
        id_meta, nome, valor_alvo, valor_atual, prazo, criada_em = meta
        
        # Calcular progresso
        percentual = (valor_atual / valor_alvo * 100) if valor_alvo > 0 else 0
        percentual = min(percentual, 100)  # Limite a 100%
        
        # Determinar cor baseado no progresso
        if percentual >= 100:
            status_color = "🟢"
            status_text = "Concluída!"
        elif percentual >= 75:
            status_color = "🟡"
            status_text = f"{percentual:.1f}% concluída"
        else:
            status_color = "🔵"
            status_text = f"{percentual:.1f}% concluída"
        
        # Criar card
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### {status_color} {nome}")
                st.markdown(f"**Prazo:** {prazo}")
                
                # Barra de progresso
                st.progress(percentual / 100)
                
                # Informações de valores
                col_val1, col_val2 = st.columns(2)
                with col_val1:
                    st.metric("Valor Atual", f"R$ {valor_atual:,.2f}".replace(",", "_").replace(".", ",").replace("_", "."))
                with col_val2:
                    st.metric("Valor Alvo", f"R$ {valor_alvo:,.2f}".replace(",", "_").replace(".", ",").replace("_", "."))
                
                st.caption(f"Status: {status_text}")
            
            with col2:
                st.markdown("---")
                if st.button("🗑️ Deletar", key=f"delete_{id_meta}", use_container_width=True):
                    if deletar_meta(id_meta):
                        st.success("✅ Meta deletada!")
                        st.rerun()
                    else:
                        st.error("❌ Erro ao deletar")
            
            # Input para atualizar valor
            st.markdown("**Atualizar Valor Atual:**")
            col_input1, col_input2 = st.columns([3, 1])
            
            with col_input1:
                novo_valor = st.number_input(
                    "Novo valor",
                    value=valor_atual,
                    min_value=0.0,
                    step=0.01,
                    key=f"valor_{id_meta}",
                    label_visibility="collapsed"
                )
            
            with col_input2:
                if st.button("✅", key=f"update_{id_meta}"):
                    if atualizar_valor_meta(id_meta, novo_valor):
                        st.success("✅ Meta atualizada!")
                        st.rerun()
                    else:
                        st.error("❌ Erro ao atualizar")
else:
    st.info("📭 Nenhuma meta cadastrada ainda. Comece criando sua primeira meta!")

# Resumo de metas
if metas:
    st.markdown("---")
    st.subheader("📈 Resumo de Metas")
    
    total_valor_alvo = sum(m[2] for m in metas)
    total_valor_atual = sum(m[3] for m in metas)
    progresso_geral = (total_valor_atual / total_valor_alvo * 100) if total_valor_alvo > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Metas", len(metas))
    
    with col2:
        metas_concluidas = sum(1 for m in metas if (m[3] / m[2] * 100) >= 100)
        st.metric("Metas Concluídas", metas_concluidas)
    
    with col3:
        st.metric("Valor Total Alvo", f"R$ {total_valor_alvo:,.2f}".replace(",", "_").replace(".", ",").replace("_", "."))
    
    with col4:
        st.metric("Valor Total Economizado", f"R$ {total_valor_atual:,.2f}".replace(",", "_").replace(".", ",").replace("_", "."))
    
    st.markdown("**Progresso Geral de Todas as Metas:**")
    st.progress(min(progresso_geral / 100, 1.0))
    st.caption(f"Progresso: {progresso_geral:.1f}%")
