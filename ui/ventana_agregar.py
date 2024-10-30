# ui/ventana_agregar.py
import tkinter as tk
from utils.helpers import mostrar_error, mostrar_exito, validar_numero, validar_campos_obligatorios
from db.modelo_productos import agregar_producto

def ventana_agregar_producto(root):
    ventana = tk.Toplevel(root)
    ventana.title("Agregar Producto")
    
    tk.Label(ventana, text="Nombre del Producto").grid(row=0, column=0)
    tk.Label(ventana, text="Categoría").grid(row=1, column=0)
    tk.Label(ventana, text="Cantidad").grid(row=2, column=0)
    tk.Label(ventana, text="Umbral de Stock").grid(row=3, column=0)
    tk.Label(ventana, text="Precio").grid(row=4, column=0)
    
    nombre = tk.Entry(ventana)
    categoria = tk.Entry(ventana)
    cantidad = tk.Entry(ventana)
    umbral_stock = tk.Entry(ventana)
    precio = tk.Entry(ventana)
    
    nombre.grid(row=0, column=1)
    categoria.grid(row=1, column=1)
    cantidad.grid(row=2, column=1)
    umbral_stock.grid(row=3, column=1)
    precio.grid(row=4, column=1)
    
    def guardar():
        # Validación de campos obligatorios
        if not validar_campos_obligatorios(nombre.get(), categoria.get(), cantidad.get(), umbral_stock.get(), precio.get()):
            mostrar_error("Todos los campos son obligatorios.")
            return
        
        # Validación de que los valores numéricos sean correctos
        cantidad_valida = validar_numero(cantidad.get(), int)
        umbral_stock_valido = validar_numero(umbral_stock.get(), int)
        precio_valido = validar_numero(precio.get(), float)
        
        if cantidad_valida is None or umbral_stock_valido is None or precio_valido is None:
            mostrar_error("Cantidad, Umbral de Stock y Precio deben ser números válidos.")
            return

        # Si todas las validaciones son correctas, agrega el producto
        agregar_producto(nombre.get(), categoria.get(), cantidad_valida, umbral_stock_valido, precio_valido)
        mostrar_exito("Producto agregado exitosamente.")
        ventana.destroy()
    
    tk.Button(ventana, text="Guardar", command=guardar).grid(row=5, column=1)
