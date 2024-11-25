import os
import json
from datetime import datetime,timedelta
from menu.mainMenu import designMainMenu
from logica.fechas import asignar_fecha

def designRegistrar():
    ruta = 'datas/datagastos.json'

    print(f"""
=============================================
        Registrar Nuevo Gasto
=============================================
Ingrese la información del gasto:""")

    try:
        # Ingreso de datos
        monto_gasto = int(input("  - Monto del gasto: "))
        if monto_gasto < 0:
            raise ValueError("El monto no puede ser negativo.")

        categoria = input("  - Categoría (ej. comida, transporte, entretenimiento, otros): ")
        if categoria.isdigit():
            raise ValueError("La categoría debe ser un texto válido.")

        descripcion = input("  - Descripción (opcional): ").strip()
        if categoria.isdigit():
            raise ValueError("La descripcion debe ser un texto válido.")
        if not descripcion:
            descripcion = "No proporcionada"

        # Confirmación de guardar o cancelar
        save_cancel = input(f"""
=============================================
Ingrese 'S' para guardar o 'C' para cancelar.
=============================================
""").strip().upper()

        if save_cancel == 'S':
            # Preparar el gasto
            nuevo_gasto = {
                "monto": monto_gasto,
                "categoria": categoria,
                "descripcion": descripcion,
                "fecha": datetime.now().strftime('%d-%m-%Y')
            }

            # Cargar o iniciar datos
            if os.path.exists(ruta):
                with open(ruta, 'r') as f:
                    try:
                        datos = json.load(f)
                    except json.JSONDecodeError:
                        datos = {"gastos": [], "reportes": []}
            else:
                datos = {"gastos": [], "reportes": []}

            # Agregar el nuevo gasto
            datos["gastos"].append(nuevo_gasto)

            # Guardar en el archivo
            with open(ruta, 'w') as f:
                json.dump(datos, f, indent=4)

            os.system('clear')
            print("\n¡Gasto registrado con éxito!")
            return designMainMenu()

        elif save_cancel == 'C':
            os.system('clear')
            print("\nEl registro ha sido cancelado.")
            return designMainMenu()
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar.")
            os.system('clear')
            designRegistrar()

    except ValueError as e:
        print(f"\nError: {e}")
        input("\n-Los datos utilizados no son válidos. ¡Presione Enter para continuar!")
        os.system('clear')
        designRegistrar()

    except KeyboardInterrupt:
        input("\n-No presione 'Ctrl + C'. ¡Presione Enter para continuar!")
        os.system('clear')
