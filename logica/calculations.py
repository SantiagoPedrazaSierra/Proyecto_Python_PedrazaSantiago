import os
import json
from datetime import datetime, timedelta
from collections import defaultdict

def calculos(periodo):
    ruta = 'datas/datagastos.json'

    # Crear el directorio si no existe
    os.makedirs('datas', exist_ok=True)

    # Cargar los datos del archivo JSON
    if os.path.exists(ruta):
        with open(ruta, 'r') as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                datos = {"gastos": [], "reportes": []}
    else:
        datos = {"gastos": [], "reportes": []}

    # Obtener la lista de gastos
    gastos = datos.get("gastos", [])
    if not gastos:
        print("No hay datos registrados para generar un reporte.")
        return

    # Inicializar estructuras para los reportes
    totales = defaultdict(float)
    totales_por_categoria = defaultdict(float)

    # Procesar los datos de gastos
    for gasto in gastos:
        # Validar que el registro tenga las claves necesarias
        if not all(k in gasto for k in ('fecha', 'categoria', 'monto')):
            print(f"Registro incompleto o mal formado: {gasto}")
            continue

        # Obtener y validar la fecha
        fecha_str = gasto['fecha']
        try:
            fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
        except ValueError:
            print(f"Formato de fecha inválido: {fecha_str}")
            continue

        categoria = gasto['categoria']
        monto = gasto['monto']

        # Acumular por categoría
        totales_por_categoria[categoria] += monto

        # Calcular totales según el período seleccionado
        if periodo == "diario":
            clave = fecha.strftime('%d-%m-%Y')
        elif periodo == "semanal":
            clave = (fecha - timedelta(days=fecha.weekday())).strftime('%d-%m-%Y') + " - " + \
                    (fecha + timedelta(days=6 - fecha.weekday())).strftime('%d-%m-%Y')
        elif periodo == "mensual":
            clave = fecha.strftime('%m-%Y')
        else:
            print("Periodo no reconocido.")
            return

        totales[clave] += monto

    # Verificar si hay datos para el período
    if not totales:
        print(f"No hay gastos registrados para el período {periodo}.")
        return

    # Generar el reporte en formato texto para el período seleccionado
    calculo = f"\n=============================================\n"
    calculo += f"          Calculo de Gastos ({periodo.capitalize()})\n"
    calculo += f"=============================================\n\n"
    calculo += f"Totales por {periodo}:\n"
    for clave, total in totales.items():
        calculo += f"  - {clave}: ${total:.2f}\n"

    calculo += "\nGastos por Categoría:\n"
    for categoria, total in totales_por_categoria.items():
        calculo += f"  - {categoria.capitalize()}: ${total:.2f}\n"

    calculo += "\n=============================================\n"

    # Mostrar el calculo al usuario y preguntar si desea guardarlo
    print(calculo)

    input("\nPresione Enter para regresar al menú principal.")
    os.system('cls')
