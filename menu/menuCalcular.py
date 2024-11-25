import os 
import keyboard
from menu.mainMenu import designMainMenu
from logica.calculations import calculos
def designMenuCalcular():
    
    try:
        keyboard.is_pressed('ctrl+c')
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
                calculos("diario")
                designMainMenu()
            case 2:
                os.system('cls')
                calculos("semanal")
                designMainMenu()
            case 3:
                os.system('cls')
                calculos("mensual")
                designMainMenu()
            case 4:
                os.system('cls')
                designMainMenu()
                
            case _: print("Opcion no valida")
    except ValueError:
        print("\nPor favor, ingrese un número válido.")
        input("Presione Enter para continuar...")
        os.system('cls')
        designMenuCalcular()
    except KeyboardInterrupt:
        input("\n-Señor usuario no presione 'Ctrl + C'¡Presione Enter para continuar y seleccione una opcion del menu!")
        os.system('cls')
        designMenuCalcular()