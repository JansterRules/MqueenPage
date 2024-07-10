import os
import sys
import django

# Añadir el directorio del proyecto al path de Python
proyecto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(proyecto_dir)

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_mecanico.settings')
django.setup()

# Ahora podemos importar nuestros modelos
from taller_makween.models import Producto

# Lista de productos de taller mecánico
productos = [
    ("Aceite de motor", "Lubricantes", 25000),
    ("Filtro de aceite", "Filtros", 8000),
    ("Filtro de aire", "Filtros", 12000),
    ("Bujías", "Encendido", 5000),
    ("Pastillas de freno", "Frenos", 30000),
    ("Discos de freno", "Frenos", 45000),
    ("Amortiguadores", "Suspensión", 80000),
    ("Batería", "Eléctrico", 75000),
    ("Alternador", "Eléctrico", 120000),
    ("Correa de distribución", "Motor", 35000),
    ("Radiador", "Refrigeración", 90000),
    ("Termostato", "Refrigeración", 15000),
    ("Bomba de agua", "Refrigeración", 40000),
    ("Embrague", "Transmisión", 150000),
    ("Caja de cambios", "Transmisión", 500000),
    ("Neumáticos", "Ruedas", 80000),
    ("Llantas de aleación", "Ruedas", 200000),
    ("Escape", "Escape", 100000),
    ("Catalizador", "Escape", 180000),
    ("Kit de distribución", "Motor", 85000),
]

# Poblar la base de datos
for i, (nombre, categoria, precio) in enumerate(productos, start=1):
    try:
        Producto.objects.create(
            id=str(i),  # Convertimos el número a string ya que el modelo espera un CharField
            nombre=nombre,
            categoria=categoria,
            precio=precio
        )
        print(f"Producto creado: ID {i} - {nombre}")
    except Exception as e:
        print(f"Error al crear el producto ID {i} - {nombre}: {str(e)}")

print("Proceso de población de la base de datos completado.")