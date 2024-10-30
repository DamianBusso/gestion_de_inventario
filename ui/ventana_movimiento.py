# ui/ventana_movimiento.py
import tkinter as tk
from tkinter import messagebox, ttk
from db.modelo_movimientos import registrar_movimiento

def ventana_registrar_movimiento(root):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Movimiento")
    
    tk.Label(ventana, text="ID del Producto").grid(row=0, column=0)
    tk.Label(ventana, text="Tipo de Movimiento").grid(row=1, column=0)
    tk.Label(ventana, text="Cantidad").grid(row=2, column=0)
    tk.Label(ventana, text="Descripción").grid(row=3, column=0)
    
    id_producto = tk.Entry(ventana)
    tipo_movimiento = ttk.Combobox(ventana, values=["entrada", "salida"])
    cantidad = tk.Entry(ventana)
    descripcion = tk.Entry(ventana)
    
    id_producto.grid(row=0, column=1)
    tipo_movimiento.grid(row=1, column=1)
    cantidad.grid(row=2, column=1)
    descripcion.grid(row=3, column=1)
    
    def guardar():
        registrar_movimiento(int(id_producto.get()), tipo_movimiento.get(), int(cantidad.get()), descripcion.get())
        messagebox.showinfo("Éxito", "Movimiento registrado exitosamente.")
        ventana.destroy()
    
    tk.Button(ventana, text="Guardar Movimiento", command=guardar).grid(row=4, column=1)
