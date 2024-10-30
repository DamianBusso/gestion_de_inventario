# ui/ventana_inventario.py
import tkinter as tk
from db.modelo_productos import obtener_productos

def ventana_ver_inventario(root):
    ventana = tk.Toplevel(root)
    ventana.title("Inventario")
    
    productos = obtener_productos()
    for i, producto in enumerate(productos):
        for j, valor in enumerate(producto):
            tk.Label(ventana, text=valor).grid(row=i, column=j)
