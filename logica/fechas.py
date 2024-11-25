from datetime import datetime

#Funcion para asignar fecha a los registros de gasto 
def asignar_fecha(gasto):
    fecha_actual= datetime.now().strftime("%d-%m-%Y")
    gasto["fecha"] = fecha_actual
    return gasto