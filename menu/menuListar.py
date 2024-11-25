import os
import json
from menu.mainMenu import designMainMenu
from datetime import datetime

def designMenuListar():
    ruta = 'datas/datagastos.json'
    try:
        # Cargar los datos del archivo JSON
        if os.path.exists(ruta):
            with open(ruta, 'r') as f:
                try:
                    datos = json.load(f)
                except json.JSONDecodeError:
                    print("El archivo JSON está corrupto o vacío.")
                    datos = {}
        else:
            print("No se encontró el archivo JSON.")
            datos = {}

        # Validar y obtener solo los gastos
        gastos = datos.get("gastos", [])

        # Mostrar menú de opciones
        opcion = int(input("""
    =============================================
                Listar Gastos
    =============================================
    Seleccione una opción para filtrar los gastos:
    =============================================
    1. Ver todos los gastos
    2. Filtrar por categoría
    3. Filtrar por rango de fechas
    4. Regresar al menú principal
    ============================================= 
    - Ingrese un número del (1-4): """))

        match opcion:
            case 1:
                # Listar todos los gastos
                if gastos:
                    os.system('cls')
                    print("\nLista de gastos:")
                    for i, gasto in enumerate(gastos, start=1):
                        print(f"\nGasto {i}:")
                        print(f"  - Monto: {gasto.get('monto', 'N/A')}")
                        print(f"  - Categoría: {gasto.get('categoria', 'N/A')}")
                        print(f"  - Descripción: {gasto.get('descripcion', 'N/A')}")
                        print(f"  - Fecha: {gasto.get('fecha', 'N/A')}")
                else:
                    print("No hay gastos registrados.")
                designMenuListar()

            case 2:
                # Filtrar por categoría
                categoria = input("\nIngrese la categoría que desea filtrar (ej. comida, transporte, etc.): ").strip().lower()

                # Filtrar los gastos según la categoría
                gastos_filtrados = [gasto for gasto in gastos if categoria in gasto.get('categoria', '').lower()]

                if gastos_filtrados:
                    os.system('cls')
                    print("\nGastos filtrados por categoría:")
                    for i, gasto in enumerate(gastos_filtrados, start=1):
                        print(f"\nGasto {i}:")
                        print(f"  - Monto: {gasto.get('monto', 'N/A')}")
                        print(f"  - Categoría: {gasto.get('categoria', 'N/A')}")
                        print(f"  - Descripción: {gasto.get('descripcion', 'N/A')}")
                        print(f"  - Fecha: {gasto.get('fecha', 'N/A')}")
                else:
                    os.system('cls')
                    print("No se encontraron gastos para esa categoría.")

                designMenuListar()

            case 3:
                # Filtrar por rango de fechas
                fecha_inicio_str = input("\nIngrese la fecha de inicio (dd-mm-yyyy): ").strip()
                fecha_fin_str = input("\nIngrese la fecha de fin (dd-mm-yyyy): ").strip()

                # Convertir las fechas en objetos datetime para la comparación
                try:
                    fecha_inicio = datetime.strptime(fecha_inicio_str, "%d-%m-%Y")
                    fecha_fin = datetime.strptime(fecha_fin_str, "%d-%m-%Y")
                except ValueError:
                    print("Formato de fecha inválido. Asegúrese de usar el formato dd-mm-yyyy.")
                    return

                # Filtrar los gastos por el rango de fechas
                gastos_filtrados = []
                for gasto in gastos:
                    try:
                        fecha_gasto = datetime.strptime(gasto['fecha'], "%d-%m-%Y")
                        if fecha_inicio <= fecha_gasto <= fecha_fin:
                            gastos_filtrados.append(gasto)
                    except (ValueError, KeyError):
                        continue

                if gastos_filtrados:
                    os.system('cls')
                    print("\nGastos filtrados por rango de fechas:")
                    for i, gasto in enumerate(gastos_filtrados, start=1):
                        print(f"\nGasto {i}:")
                        print(f"  - Monto: {gasto.get('monto', 'N/A')}")
                        print(f"  - Categoría: {gasto.get('categoria', 'N/A')}")
                        print(f"  - Descripción: {gasto.get('descripcion', 'N/A')}")
                        print(f"  - Fecha: {gasto.get('fecha', 'N/A')}")
                else:
                    os.system('cls')
                    print("No se encontraron gastos en el rango de fechas especificado.")

                designMenuListar()

            case 4:
                # Regresar al menú principal
                os.system('cls')
                designMainMenu()

            case _:
                print("Opción no válida.")

    except ValueError:
        print("Por favor, ingrese un número válido.")
        input("Presione Enter para continuar...")
        os.system('cls')
        designMenuListar()  # Volver a mostrar el menú
