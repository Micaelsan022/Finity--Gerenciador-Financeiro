from database.conexao import conectar

def total_receitas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Valor) FROM Receitas")
    resultado = cursor.fetchone()[0]
    conn.close()
    return resultado or 0.0

def total_gastos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Valor) FROM Gastos")
    resultado = cursor.fetchone()[0]
    conn.close()
    return resultado or 0.0

def saldo_atual():
    return total_receitas() - total_gastos()

def gastos_por_categoria():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.Nome, SUM(g.Valor) as total
        FROM Gastos g
        JOIN Categorias c ON g.Id_Categoria = c.Id
        GROUP BY c.Nome
    """)
    resultado = cursor.fetchall()
    conn.close()

    total = total_gastos()
    if total == 0:
        return []

    return [
        {
            "categoria": row[0],
            "total": row[1],
            "porcentagem": round((row[1] / total) * 100, 2)
        }
        for row in resultado
    ]