from time import localtime
def evaluar(dia, mes, anno):
    
    
    t = localtime()
    dia_actual, mes_actual, anno_actual = t.tm_mday, t.tm_mon, t.tm_year

    
    edad = anno_actual - anno

    if (mes_actual < mes) or (mes_actual == mes and dia_actual < dia):
        edad -= 1
    
    respuesta = f"Usted tiene {edad} años"
    return respuesta

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
