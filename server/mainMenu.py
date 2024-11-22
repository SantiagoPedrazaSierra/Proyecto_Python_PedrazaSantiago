import os 
def designMainMenu():
    from menus.menuRegistrar import designRegistrar 
    from menus.menuListar import designMenuListar
    from menus.menuCalcular import designMenuCalcular
    from menus.menuReporteGatos import designMenuReportGastos


    try:
        opcion=int(input("""
    =============================================
            Simulador de Gasto Diario
    =============================================
    Seleccione una opción:

    1. Registrar nuevo gasto
    2. Listar gastos
    3. Calcular total de gastos
    4. Generar reporte de gastos
    5. Salir
    ============================================= 
    -ingrese un numero del (1-5): """))
        
        match opcion:
            case 1:
                os.system('clear')
                designRegistrar()
            case 2:
                os.system('clear')
                designMenuListar()
            case 3:
                os.system('clear')
                designMenuCalcular()
            case 4:
                os.system('clear')
                designMenuReportGastos()
            case 5:
                print("\n-Saliendo del programa...")
                os._exit 
            case _: print("Opcion no valida")
    except ValueError:
        print("Por favor, ingrese un numero valido.")

        

        
            

