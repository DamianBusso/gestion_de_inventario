# db/modelo_productos.py
from db.conexion import conectar

# Función para agregar un producto
def agregar_producto(nombre, categoria, cantidad, umbral_stock, precio):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, categoria, cantidad, umbral_stock, precio)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, categoria, cantidad, umbral_stock, precio))
    conexion.commit()
    conexion.close()

# Función para consultar todos los productos
def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return productos
