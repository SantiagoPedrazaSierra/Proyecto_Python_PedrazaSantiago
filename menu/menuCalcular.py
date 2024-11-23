import os 


def designMenuCalcular():
    from menu.mainMenu import designMainMenu
    try:
        opcion=int(input("""
    =============================================
          Calcular Total de Gastos
    =============================================
    Seleccione el periodo de cálculo:
    =============================================
    1. Calcular total diario
    2. Calcular total semanal
    3. Calcular total mensual
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