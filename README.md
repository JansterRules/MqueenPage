# Taller Makween

Proyecto semestral para la asignatura PGY3121

## Tabla de Contenidos

- [Taller Makween](#taller-makween)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Configuración](#configuración)
  - [Instalación](#instalación)
  - [Uso](#uso)
  - [URLs del Proyecto](#urls-del-proyecto)

## Descripción

Taller Makween es un proyecto desarrollado para la asignatura PGY3121, que consiste en un sistema de gestión de taller mecánico.

## Estructura del Proyecto

```
misProyectos/
├── taller_makween/
│   ├── static/
│   │   ├── CSS/
│   │   ├── IMG/
│   │   └── JS/
│   ├── templates/
│   │   └── taller_makween/
│   │       ├── aboutus.html
│   │       ├── base.html
│   │       ├── Checkout.html
│   │       ├── faq.html
│   │       ├── galeria.html
│   │       ├── index.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── regvacante.html
│   │       ├── vehiculos_add.html
│   │       ├── vehiculos_edit.html
│   │       └── vehiculos_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── taller_mecanico/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── .gitignore
├── config.txt
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
Scripts Python/
├── get-pip.py
└── ScriptCambioValoresPYENV.py
```

## Configuración

Para cambiar las configuraciones de "pyvenv.cfg", ejecute el script `ScriptCambioValoresPyVENV.py` ubicado en `Django/Scripts Python/`. Este script generará un archivo `config.txt` con las configuraciones necesarias para reemplazar en el archivo `.cfg` mencionado.

## Instalación

Para instalar pip, ejecute el siguiente script:
```
python Scripts Python/get-pip.py
```

## Uso

Para iniciar el servidor, utilice el siguiente comando:
```
python manage.py runserver
```

## URLs del Proyecto

- [Vista index](http://127.0.0.1:8000/)
- [Vista base](http://127.0.0.1:8000/base)
- [Vista aboutus](http://127.0.0.1:8000/aboutus)
- [Vista Checkout](http://127.0.0.1:8000/checkout)
- [Vista faq](http://127.0.0.1:8000/faq)
- [Vista galeria](http://127.0.0.1:8000/galeria)
- [Vista login](http://127.0.0.1:8000/login)
- [Vista register](http://127.0.0.1:8000/register)
- [Vista regvacante](http://127.0.0.1:8000/regvacante)
- [Vista crud](http://127.0.0.1:8000/crud)
- [Vista vehiculosAdd](http://127.0.0.1:8000/vehiculosAdd)
- [Vista vehiculos_del](http://127.0.0.1:8000/vehiculos_del/<placa>)
- [Vista vehiculos_findEdit](http://127.0.0.1:8000/vehiculos_findEdit/<placa>)
- [Vista vehiculosUpdate](http://127.0.0.1:8000/vehiculosUpdate)
