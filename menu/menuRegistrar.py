import os
import json
from menu.mainMenu import designMainMenu
from logica.fechas import asignar_fecha

#Lista para almacenar los nuevos gastos a el archivo JSON

def designRegistrar():
    # Ruta del archivo JSON donde se guardarán los datos
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
            print("La entrada no es un texto válido.")
            raise ValueError("La categoría debe ser un texto.")
        
        descripcion = input("  - Descripción (opcional): ")
        if not descripcion.strip():  # Si la descripción está vacía, asignamos un valor por defecto
            descripcion = "No proporcionada"
            print("\nNo se proporcionó descripción, se asignará 'No proporcionada'.")

        # Confirmación de guardar o cancelar
        save_cancel = input(f"""
=============================================
Ingrese 'S' para guardar o 'C' para cancelar.
=============================================
""")

        if save_cancel.upper() == 'S':
            # Preparar los datos del gasto para ser guardados
            nuevo_gasto = {
                'monto': monto_gasto,
                'categoria': categoria,
                'descripcion': descripcion
            }

            #Asignar fecha automaticamente al gasto
            nuevo_gasto=asignar_fecha(nuevo_gasto)

            # Leer siempre el archivo para obtener los datos existentes
            if os.path.exists(ruta):
                try:
                    with open(ruta, 'r') as f:
                        # Intentar cargar los datos del archivo JSON
                        try:
                            gasto = json.load(f)
                        except json.JSONDecodeError:
                            # Si el archivo está vacío o es corrupto, inicializar como una lista vacía
                            gastos = []
                except FileNotFoundError:
                    # Si el archivo no existe, inicializar como una lista vacía
                    gasto = []
            else:
                # Si el archivo no existe, inicializar como una lista vacía
                gasto = []

            #Asignamos un numero a cada gasto
            num_gasto=len(gastos)+1
            nombre_gasto=f'gasto {num_gasto}'

            #Asiganmos a cada diccionario el nombre gasto
            nombre_gasto={nombre_gasto: nuevo_gasto}

            # Agregar el nuevo gasto a los datos existentes
            gastos.append(nombre_gasto)

            # Guardar los datos actualizados en el archivo JSON
            with open(ruta, 'w') as f:
                json.dump(nombre_gasto, f, indent=4)

            os.system('cls')
            print("\n¡Gasto registrado con éxito!")
            return designMainMenu()

        elif save_cancel.upper() == 'C':
            # Si se cancela el registro
            os.system('cls')
            print("\nEl registro ha sido cancelado.")
            return designMainMenu()

        else:
            # Si la opción es inválida
            print("\nOpción no válida. Solo se permite 'S' para guardar o 'C' para cancelar.")
            input("\nPresione Enter para continuar.")
            os.system('cls')
            designRegistrar()  # Reintentar el registro

    # Evaluar errores en la entrada de datos
    except ValueError as e:
        print(f"\nError: {e}")
        input("\n-Los datos utilizados no son válidos. ¡Presione Enter para continuar y seleccione una opción del menú!")
        os.system('cls')
        designRegistrar()

    # Manejo de interrupciones por el teclado (Ctrl + C)
    except KeyboardInterrupt:
        input("\n-Señor usuario no presione 'Ctrl + C', ¡Presione Enter para continuar y seleccione una opción del menú!")
        os.system('cls')
