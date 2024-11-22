import os 

def designMenuReportGastos():
    from server.mainMenu import designMainMenu

    try:
        opcion=int(input("""
    =============================================
           Generar Reporte de Gastos
    =============================================
    Seleccione el tipo de reporte:

    1. Reporte diario
    2. Reporte semanal
    3. Reporte mensual
    4. Regresar al menú principal
    ============================================= 
    -ingrese un numero del (1-4): """))
        
        match opcion:
            case 1:
                os.system('clear')
            case 2:
                os.system('clear')
            case 3:
                os.system('clear')
            case 4:
                os.system('clear')
                designMainMenu()
            case _: print("Opcion no valida")
    except ValueError:
        print("Por favor, ingrese un numero valido.")
