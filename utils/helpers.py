# utils/helpers.py
from tkinter import messagebox

# Función para mostrar mensajes de error en ventanas
def mostrar_error(mensaje):
    messagebox.showerror("Error", mensaje)

# Función para mostrar mensajes de éxito en ventanas
def mostrar_exito(mensaje):
    messagebox.showinfo("Éxito", mensaje)

# Validación de valores numéricos
def validar_numero(valor, tipo=int):
    try:
        return tipo(valor)
    except ValueError:
        return None

# Validación de campos obligatorios
def validar_campos_obligatorios(*campos):
    for campo in campos:
        if not campo:
            return False
    return True
