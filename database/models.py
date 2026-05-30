import sqlite3
import os

def criar_tabelas():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect("database/banco.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categorias (
            Id       INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome     TEXT    NOT NULL,
            Tipo     TEXT    NOT NULL CHECK (Tipo IN ('Receita', 'Gasto')),
            Icone    TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Receitas (
            Id           INTEGER PRIMARY KEY AUTOINCREMENT,
            Descricao    TEXT    NOT NULL,
            Valor        REAL    NOT NULL,
            DataReceita  TEXT    NOT NULL,
            Id_Categoria INTEGER NOT NULL,
            FOREIGN KEY (Id_Categoria) REFERENCES Categorias(Id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Gastos (
            Id           INTEGER PRIMARY KEY AUTOINCREMENT,
            Descricao    TEXT    NOT NULL,
            Valor        REAL    NOT NULL,
            DataGasto    TEXT    NOT NULL,
            Id_Categoria INTEGER NOT NULL,
            FOREIGN KEY (Id_Categoria) REFERENCES Categorias(Id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Metas (
            Id          INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome        TEXT    NOT NULL,
            Valor_Alvo  REAL    NOT NULL,
            Valor_Atual REAL    NOT NULL DEFAULT 0,
            Prazo       TEXT    NOT NULL,
            Criada_Em   TEXT    NOT NULL DEFAULT CURRENT_DATE
        )
    """)

    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")

criar_tabelas()
