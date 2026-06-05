import sqlite3
import os

def conectar():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect("database/banco.db")
    return conn
