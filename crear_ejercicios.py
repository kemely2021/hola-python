import os

def crear_ejercicios(carpeta, cantidad=20):
    """
    Crea archivos de ejercicios en la carpeta indicada.
    
    Args:
        carpeta (str): Ruta de la carpeta donde crear los archivos.
        cantidad (int): Número de archivos a crear (por defecto 20).
    """
    # Crear la carpeta si no existe
    os.makedirs(carpeta, exist_ok=True)
    
    for i in range(1, cantidad + 1):
        nombre_archivo = os.path.join(carpeta, f"ejercicio{i}.py")
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(f"# Ejercicio {i}\n")
            f.write(f'print("Este es el ejercicio {i}")\n')
        print(f"✅ Archivo creado: {nombre_archivo}")

# Ejemplo de uso: generar 20 ejercicios en 01_introduccion_python
if __name__ == "__main__":
    crear_ejercicios("01_introduccion_python")
