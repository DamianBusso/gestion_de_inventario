import sqlite3

# Conectar (o crear) la base de datos
conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

# Crear tabla de productos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT,
        cantidad INTEGER NOT NULL DEFAULT 0,
        umbral_stock INTEGER DEFAULT 10,
        precio REAL
    )
''')

# Crear tabla de movimientos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movimientos (
        id_movimiento INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto INTEGER,
        tipo TEXT NOT NULL, -- 'entrada' o 'salida'
        cantidad INTEGER NOT NULL,
        fecha TEXT DEFAULT CURRENT_TIMESTAMP,
        descripcion TEXT,
        FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
    )
''')

# Guardar cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos creada y tablas inicializadas.")
