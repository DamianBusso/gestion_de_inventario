# ui/ventana_principal.py
import tkinter as tk
from tkinter import messagebox
from ui.ventana_agregar import ventana_agregar_producto
from ui.ventana_inventario import ventana_ver_inventario
from ui.ventana_movimiento import ventana_registrar_movimiento

def main():
    root = tk.Tk()
    root.title("Sistema de Gestión de Inventario")
    root.geometry("600x400")

    # Botón para agregar productos
    btn_agregar = tk.Button(root, text="Agregar Producto", command=lambda: ventana_agregar_producto(root))
    btn_agregar.pack(pady=10)

    # Botón para ver el inventario
    btn_ver = tk.Button(root, text="Ver Inventario", command=lambda: ventana_ver_inventario(root))
    btn_ver.pack(pady=10)

    # Botón para registrar movimiento
    btn_movimiento = tk.Button(root, text="Registrar Movimiento", command=lambda: ventana_registrar_movimiento(root))
    btn_movimiento.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
