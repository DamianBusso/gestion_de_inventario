import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("inventario.db")

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Gestión de Inventario")
root.geometry("600x400")

# Función para agregar un producto
def agregar_producto():
    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Producto")
    
    tk.Label(ventana_agregar, text="Nombre del Producto").grid(row=0, column=0)
    tk.Label(ventana_agregar, text="Categoría").grid(row=1, column=0)
    tk.Label(ventana_agregar, text="Cantidad").grid(row=2, column=0)
    tk.Label(ventana_agregar, text="Umbral de Stock").grid(row=3, column=0)
    tk.Label(ventana_agregar, text="Precio").grid(row=4, column=0)
    
    nombre = tk.Entry(ventana_agregar)
    categoria = tk.Entry(ventana_agregar)
    cantidad = tk.Entry(ventana_agregar)
    umbral_stock = tk.Entry(ventana_agregar)
    precio = tk.Entry(ventana_agregar)
    
    nombre.grid(row=0, column=1)
    categoria.grid(row=1, column=1)
    cantidad.grid(row=2, column=1)
    umbral_stock.grid(row=3, column=1)
    precio.grid(row=4, column=1)
    
    def guardar_producto():
        try:
            conexion.execute('''
                INSERT INTO productos (nombre, categoria, cantidad, umbral_stock, precio)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre.get(), categoria.get(), int(cantidad.get()), int(umbral_stock.get()), float(precio.get())))
            conexion.commit()
            messagebox.showinfo("Éxito", "Producto agregado exitosamente.")
            ventana_agregar.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el producto: {e}")
    
    tk.Button(ventana_agregar, text="Guardar", command=guardar_producto).grid(row=5, column=1)

# Función para ver el inventario
def ver_inventario():
    ventana_inventario = tk.Toplevel(root)
    ventana_inventario.title("Inventario")

    productos = conexion.execute("SELECT * FROM productos").fetchall()
    
    for i, producto in enumerate(productos):
        for j, dato in enumerate(producto):
            tk.Label(ventana_inventario, text=dato).grid(row=i, column=j)

# Función para registrar un movimiento (entrada o salida)
def registrar_movimiento():
    ventana_movimiento = tk.Toplevel(root)
    ventana_movimiento.title("Registrar Movimiento")
    
    # Etiquetas y entradas para el formulario
    tk.Label(ventana_movimiento, text="ID del Producto").grid(row=0, column=0)
    tk.Label(ventana_movimiento, text="Tipo de Movimiento").grid(row=1, column=0)
    tk.Label(ventana_movimiento, text="Cantidad").grid(row=2, column=0)
    tk.Label(ventana_movimiento, text="Descripción").grid(row=3, column=0)
    
    id_producto = tk.Entry(ventana_movimiento)
    id_producto.grid(row=0, column=1)
    
    tipo_movimiento = ttk.Combobox(ventana_movimiento, values=["entrada", "salida"])
    tipo_movimiento.grid(row=1, column=1)
    
    cantidad = tk.Entry(ventana_movimiento)
    cantidad.grid(row=2, column=1)
    
    descripcion = tk.Entry(ventana_movimiento)
    descripcion.grid(row=3, column=1)
    
    # Función para guardar el movimiento en la base de datos
    def guardar_movimiento():
        try:
            tipo = tipo_movimiento.get()
            cantidad_valor = int(cantidad.get())
            id_producto_valor = int(id_producto.get())
            
            if tipo not in ["entrada", "salida"]:
                raise ValueError("Tipo de movimiento no válido.")
            
            # Insertar el movimiento en la tabla movimientos
            conexion.execute('''
                INSERT INTO movimientos (id_producto, tipo, cantidad, descripcion)
                VALUES (?, ?, ?, ?)
            ''', (id_producto_valor, tipo, cantidad_valor, descripcion.get()))
            
            # Actualizar la cantidad de productos
            if tipo == "entrada":
                conexion.execute('''
                    UPDATE productos
                    SET cantidad = cantidad + ?
                    WHERE id_producto = ?
                ''', (cantidad_valor, id_producto_valor))
            elif tipo == "salida":
                conexion.execute('''
                    UPDATE productos
                    SET cantidad = cantidad - ?
                    WHERE id_producto = ?
                ''', (cantidad_valor, id_producto_valor))
            
            conexion.commit()
            messagebox.showinfo("Éxito", f"Movimiento de {tipo} registrado exitosamente.")
            ventana_movimiento.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el movimiento: {e}")
    
    tk.Button(ventana_movimiento, text="Guardar Movimiento", command=guardar_movimiento).grid(row=4, column=1)

# Botones en la ventana principal
btn_agregar = tk.Button(root, text="Agregar Producto", command=agregar_producto)
btn_agregar.pack(pady=10)

btn_ver = tk.Button(root, text="Ver Inventario", command=ver_inventario)
btn_ver.pack(pady=10)

btn_movimiento = tk.Button(root, text="Registrar Movimiento", command=registrar_movimiento)
btn_movimiento.pack(pady=10)

root.mainloop()
