import os 

def designMenuListar():
    from server.mainMenu import designMainMenu

    try:
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

        