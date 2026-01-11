from django.shortcuts import render
from .forms import CargarArchivoForm

import csv
import io
import re

def cargar_archivo(request):
    mensaje = ''
    errores = []

    if request.method == 'POST':
        form = CargarArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            datos = archivo.read().decode('utf-8')
            lineas = datos.splitlines()
            lector = csv.reader(lineas)

            for i, fila in enumerate(lector, start=1):
                # Validación de número de columnas
                if len(fila) != 5:
                    errores.append(f"Fila {i}: número incorrecto de columnas ({len(fila)} columnas)")
                    continue

                # Validación columna 1: número entero entre 3 y 10 caracteres
                if not (fila[0].isdigit() and 3 <= len(fila[0]) <= 10):
                    errores.append(f"Fila {i}, Columna 1: debe ser número entero entre 3 y 10 dígitos")

                # Validación columna 2: email
                if not re.match(r"[^@]+@[^@]+\.[^@]+", fila[1]):
                    errores.append(f"Fila {i}, Columna 2: formato de correo inválido")

                # Validación columna 3: debe ser 'CC' o 'TI'
                if fila[2] not in ['CC', 'TI']:
                    errores.append(f"Fila {i}, Columna 3: debe ser CC o TI")

                # Validación columna 4: valor entre 500000 y 1500000
                try:
                    valor = int(fila[3])
                    if not (500000 <= valor <= 1500000):
                        errores.append(f"Fila {i}, Columna 4: valor fuera de rango (500000-1500000)")
                except ValueError:
                    errores.append(f"Fila {i}, Columna 4: no es un número válido")

                # Columna 5: cualquier valor (no se valida)

            if not errores:
                mensaje = "Archivo validado correctamente ✅"

    else:
        form = CargarArchivoForm()

    return render(request, 'cargar.html', {'form': form, 'errores': errores, 'mensaje': mensaje})
