# 📝 Prueba técnica para Desarrollador Senior - ADRES

Este proyecto es una solución desarrollada en **Django** como parte de la prueba técnica para la vacante de **Desarrollador Junior en ADRES**.

## Objetivo

Desarrollar una aplicación web que permita **subir un archivo `.txt` con formato CSV**, validar su contenido con base en reglas específicas, y mostrar los errores encontrados o un mensaje de éxito si el archivo es válido.

---

## Tecnologías utilizadas

- Python 3.x
- Django 6.0.1
- HTML + Bootstrap 5

---

## Estructura del proyecto

prueba_django_adres/
│
├── prueba_adres/ # Configuración general de Django
├── validador_csv/ # Aplicación principal
│ ├── forms.py # Formulario para subir archivo
│ ├── views.py # Lógica de validación
│ ├── templates/
│ │ └── cargar.html # Interfaz de carga y visualización de errores
├── db.sqlite3 # Base de datos SQLite por defecto
├── manage.py
├── requirements.txt
└── README.md



---

## Validaciones realizadas

Cada fila del archivo `.txt` debe cumplir con los siguientes criterios:

| Columna | Validación                                                                 |
|---------|----------------------------------------------------------------------------|
| 1       | Solo debe permitir números enteros entre 3 y 10 caracteres                 |
| 2       | Solo debe permitir correos electrónicos                                    |
| 3       | Solo debe permitir los valores `CC` o `TI`                                 |
| 4       | Solo debe permitir valores entre `500000` y `1500000`                      |
| 5       | Permite cualquier valor                                                    |

---

## Instalación y ejecución


1) Clona el repositorio:
git clone https://github.com/tu_usuario/prueba_django_adres.git
cd prueba_django_adres


2. (Opcional) Crea y activa un entorno virtual:
python -m venv env
.\env\Scripts\Activate.ps1  # En Windows PowerShell


3. Instala dependencias:
pip install -r requirements.txt


4. Aplica migraciones:
python manage.py migrate


5. Ejecuta el servidor:
python manage.py runserver


6. Abre en tu navegador:
http://127.0.0.1:8000/



## Archivos de prueba

Se incluyen dos archivos de ejemplo en la raíz del proyecto:

valido.txt: contiene datos correctos que deben pasar todas las validaciones.

invalido.txt: contiene errores para comprobar la funcionalidad de validación.



## Autor
Santiago Gómez
Fecha: Enero de 2026
Vacante: Desarrollador Junior - ADRES
