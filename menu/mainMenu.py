import os 
import keyboard 
def designMainMenu():
    from menu.menuRegistrar import designRegistrar 
    from menu.menuListar import designMenuListar
    from menu.menuCalcular import designMenuCalcular
    from menu.menuReporteGatos import designMenuReportGastos


    try:
        keyboard.is_pressed('ctrl+c')
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
                os.system('cls')
                designRegistrar()
            case 2:
                os.system('cls')
                designMenuListar()
            case 3:
                os.system('cls')
                designMenuCalcular()
            case 4:
                os.system('cls')
                designMenuReportGastos()
            case 5:
                print("\n-Saliendo del programa...")
                os._exit 
            case _: print("Opcion no valida")
    except ValueError:
        print("\nPor favor, ingrese un número válido.")
        input("Presione Enter para continuar...")
        os.system('cls')
        designMainMenu()
    except KeyboardInterrupt:
        input("\n-Señor usuario no presione 'Ctrl + C'¡Presione Enter para continuar y seleccione una opcion del menu!")
        os.system('cls')
        designMainMenu()
        

        
            

