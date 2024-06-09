import os
import platform
import sys

# Obtener la versión de Python en uso
python_version = platform.python_version()

# Obtener la ruta del ejecutable de Python
python_executable = sys.executable

# Obtener la ruta de instalación de Python
python_home = os.path.dirname(os.path.dirname(python_executable))

# Configurar el comando para crear un entorno virtual
command = f"{python_executable} -m venv C:\\misProyectos\\myvenv"

# Crear o actualizar el archivo de configuración
config_content = f"""
home = {python_home}
include-system-site-packages = false
version = {python_version}
executable = {python_executable}
command = {command}
"""

config_file_path = "config.txt"  # Puedes cambiar el nombre del archivo si es necesario

# Escribir el contenido en el archivo de configuración
with open(config_file_path, "w") as config_file:
    config_file.write(config_content)

print(f"Archivo de configuración actualizado: {config_file_path}")
