# db/conexion.py
import sqlite3

def conectar():
    return sqlite3.connect("inventario.db")