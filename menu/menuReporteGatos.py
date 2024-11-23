import os 

def designMenuReportGastos():
    from menu.mainMenu import designMainMenu

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
                os.system('cls')
            case 2:
                os.system('cls')
            case 3:
                os.system('cls')
            case 4:
                os.system('cls')
                designMainMenu()
            case _: print("Opcion no valida")
    except ValueError:
        print("Por favor, ingrese un numero valido.")
