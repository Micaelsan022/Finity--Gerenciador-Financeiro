from database.conexao import conectar


def receitas_por_mes(mes, ano):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM Receitas
        WHERE strftime('%m', DataReceita) = ?
        AND strftime('%Y', DataReceita) = ?
    """, (f"{mes:02d}", str(ano)))

    resultado = cursor.fetchall()
    conn.close()

    return resultado


def gastos_por_mes(mes, ano):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM Gastos
        WHERE strftime('%m', DataGasto) = ?
        AND strftime('%Y', DataGasto) = ?
    """, (f"{mes:02d}", str(ano)))

    resultado = cursor.fetchall()
    conn.close()

    return resultado


def saldo_por_mes(mes, ano):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(Valor)
        FROM Receitas
        WHERE strftime('%m', DataReceita) = ?
        AND strftime('%Y', DataReceita) = ?
    """, (f"{mes:02d}", str(ano)))

    total_receitas = cursor.fetchone()[0] or 0

    cursor.execute("""
        SELECT SUM(Valor)
        FROM Gastos
        WHERE strftime('%m', DataGasto) = ?
        AND strftime('%Y', DataGasto) = ?
    """, (f"{mes:02d}", str(ano)))

    total_gastos = cursor.fetchone()[0] or 0

    conn.close()

    return total_receitas - total_gastos