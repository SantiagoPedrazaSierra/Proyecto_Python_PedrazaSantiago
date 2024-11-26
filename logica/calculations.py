import os
import json
from datetime import datetime, timedelta
from collections import defaultdict
from tabulate import tabulate 

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

    # Inicializar estructuras para los calculos
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

     # Crear los datos para la tabla de totales por periodo
    tabla_totales = []
    for clave, total in totales.items():
        tabla_totales.append([clave, f"${total:.2f}"])

    # Crear los datos para la tabla de gastos por categoría
    tabla_categoria = []
    for categoria, total in totales_por_categoria.items():
        tabla_categoria.append([categoria.capitalize(), f"${total:.2f}"])

    # Mostrar el reporte usando tabulate
    os.system('cls')
    print(f"\n=============================================")
    print(f"          Calculo de Gastos ({periodo.capitalize()})")
    print(f"=============================================\n")

    print(f"Totales por {periodo}:")
    print(tabulate(tabla_totales, headers=["Período", "Total"], tablefmt="fancy_grid"))

    print("\nGastos por Categoría:")
    print(tabulate(tabla_categoria, headers=["Categoría", "Total"], tablefmt="fancy_grid"))

    print(f"\n=============================================\n")

    input("\nPresione Enter para regresar al menú principal.")
    os.system('cls')