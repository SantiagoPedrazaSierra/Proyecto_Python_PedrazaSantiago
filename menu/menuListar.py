import os 
import json
from menu.mainMenu import designMainMenu
from datetime import datetime

def designMenuListar():
    ruta = 'datas/datagastos.json'
    try:
        #Cargar los datos de los archivos JSON 
        if os.path.exists(ruta):
            with open(ruta, 'r') as f:
                try:
                    gastos= json.load(f)
                except json.JSONDecodeError:
                    gastos=[] #si el archivo esta vacio
        else:
            gastos=[]
    
        #Mostrar menu de opciones 
        opcion=int(input("""
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
    -ingrese un numero del (1-4): """))
        
        match opcion:
            case 1:
                
              #Listar todos los gastos 
                if gastos:
                    os.system('cls')
                    print("\nLista de gastos:")
                    for gasto in gastos:
                        for nombre_gasto, datos in gasto.items():
                            print(f"\n{nombre_gasto}:")
                            print(f"  - Monto: {datos['monto']}")
                            print(f"  - Categoría: {datos['categoria']}")
                            print(f"  - Descripción: {datos['descripcion']}")
                            print(f"  - Fecha: {datos['fecha:']}")
                            
                else:
                        print("No hay gastos registrados.")
                designMenuListar()
            case 2:
                #Filtrar por categoria 
                categoria = input("\nIngrese la categoria que desea filtrar ej.(comida,transporte..etc)").strip().lower()
                
                #Filtrar los gastos segun la categoria 
                gastos_filtrados=[]
                for gasto in gastos:
                    for nombre_gasto, datos in gasto.items():
                        if categoria in datos['categoria'].lower():
                            gastos_filtrados.append(gasto)
                            break
                if gastos_filtrados:
                    os.system('cls')
                    print("\nGastos filtrados por categoria:")
                    for gasto in gastos_filtrados:
                        for nombre_gasto, datos in gasto.items():
                            print(f"\n{nombre_gasto}:")
                            print(f"  - Monto: {datos['monto']}")
                            print(f"  - Categoría: {datos['categoria']}")
                            print(f"  - Descripción: {datos['descripcion']}")
                            print(f"  - Fecha: {datos['fecha:']}")
                else:
                    os.system('cls')
                    print("No se encontraron gastos para esa categoria.")
                    
                designMenuListar()


            case 3:
                #Filtrar por rango de fechas 
                fecha_inicio_str= input("\nIngrese la fecha de inicio (dd-mm-yyyy): ").strip()
                fecha_fin_str= input("\nIngrese la fecha de fin (dd-mm-yyyy): ").strip()

                #Convertir las fechas en objetos datatime para la comparacion 
                try:
                    fecha_inicio= datetime.strptime(fecha_inicio_str, "%d-%m-%Y")
                    fecha_fin= datetime.strptime(fecha_fin_str, "%d-%m-%Y")
                except ValueError:
                    print("Formato de fecha invalido. Asegurese de usar el formato de dd-mm-yyyy")
                    return
                
                #Filtrar los gastos por el rango de fechas 
                gastos_filtrados= []
                for gasto in gastos:
                    for nombre_gasto, datos in gasto.items():
                        fecha_gasto=datetime.strptime(datos['fecha:'], "%d-%m-%Y")
                        if fecha_inicio <= fecha_gasto <= fecha_fin:
                            gastos_filtrados.append(gasto)

                if gastos_filtrados:
                    os.system('cls')
                    print("\nGastos filtrados por rango de fechas:")
                    for gasto in gastos_filtrados:
                        for nombre_gasto,datos in gasto.items():
                            print(f"\n{nombre_gasto}:")
                            print(f"  - Monto: {datos['monto']}")
                            print(f"  - Categoría: {datos['categoria']}")
                            print(f"  - Descripción: {datos['descripcion']}")
                            print(f"  - Fecha: {datos['fecha:']}")
                else:
                    os.system('cls')
                    print("No se encontraron gastos en el rango de fechas especificado.")

                designMenuListar()

            case 4:
                #Regresar al menu 
                os.system('cls')
                designMainMenu() 

            case _: print("Opcion no valida")

    except ValueError:
        print("Por favor, ingrese un numero valido.")
        input("Presione Enter para continuar...")
        os.system('cls')
        designMenuListar() #Volver a mostrar el menu 

        