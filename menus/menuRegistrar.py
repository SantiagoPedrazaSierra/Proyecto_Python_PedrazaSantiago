import os 
import requests


def designRegistrar():

    
        print(f"""
    =============================================
            Registrar Nuevo Gasto
    =============================================
    Ingrese la información del gasto:""")
        try:
            
            
            monto_gasto=int(input("  - Monto del gasto: "))
            if (monto_gasto < 0):
                raise ValueError
            categoria=input("  - Categoría (ej. comida, transporte, entretenimiento, otros): ")
            if categoria.isdigit():
                    print("La entrada no es un texto")
                    raise ValueError

            descripcion=input("  - Descripción (opcional): ")
            if not descripcion.strip():  # strip() elimina los espacios en blanco al principio y al final
                print("La entrada no es un texto válido .")
                raise ValueError ("Ingrese espacio si no desea llenar la descripcion")
            

            save_cancel=input(f"""
    =============================================                     
    Ingrese 'S' para guardar o 'C' para cancelar.
    =============================================""")

            if save_cancel == "S":
                #Guardar datos en api
                encabezados={'Content-Type': 'application/json'}
                datos={'monto_gasto':monto_gasto,'categoria':categoria,'descripcion':descripcion}
                respuesta= requests.post('https://6737e78c4eb22e24fca66bb9.mockapi.io/propina/CalculateOption1Menu', headers=encabezados,json=datos) 
                print(f"\t {respuesta}")
                return 
            else:
                return print("")
        #Evaluar Errores
        except ValueError:
            input("\n-Los datos utilizados no son validos,¡Presione Enter para continuar y seleccione una opción del menú!.")
            os.system('clear')
            designRegistrar()
            
        except KeyboardInterrupt:
            input("\n-Señor usuario no presione 'Ctrl + C',¡Presione Enter para continuar y seleccione una opción del menú!.")
            os.system('clear')