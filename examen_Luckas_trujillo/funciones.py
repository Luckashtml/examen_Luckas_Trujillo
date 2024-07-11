import random
import csv
import statistics 


def asignar_sueldos_aleatorios(trabajadores):
    sueldo_trabajadores = {}

    for trabajador in trabajadores:
        sueldo = random.randint(800000,2000000)
        sueldo_trabajadores[trabajador] = sueldo
    
    print ("Sueldo asignado satisfactoriamente.")
    print (sueldo_trabajadores)

    return sueldo_trabajadores


def clasificar_sueldos(sueldo_trabajadores):
    menor_a_800k = {}
    entre_800k_y_2M = {}
    mayor_a_2M = {}
    
    for trabajador,sueldo in sueldo_trabajadores.items():
        if sueldo < 800000:
            menor_a_800k[trabajador] = sueldo
        else:
            if sueldo >= 800000 and sueldo < 2000000:
                entre_800k_y_2M[trabajador] = sueldo
            else:
                mayor_a_2M[trabajador] = sueldo

    print ("Sueldos menores a $800.000: ",len(menor_a_800k))
    for trabajador,sueldo in menor_a_800k.items():
        print (trabajador," : $",sueldo)

    print ("Sueldos entre $800.000 y $2.000.000: ", len(entre_800k_y_2M))
    for trabajador,sueldo in entre_800k_y_2M.items():
        print (trabajador, " : $",sueldo)
    
    print ("Sueldos Superriores a $2.000.000: ",len(mayor_a_2M))
    for trabajador,sueldo in mayor_a_2M.items():
        print (trabajador," : $",sueldo)
    
    print ("Total Sueldos: ", sum(menor_a_800k,entre_800k_y_2M,mayor_a_2M))


def ver_estadisticas(sueldo_trabajadores):
    sueldo = list(sueldo_trabajadores.values())

    if not sueldo:
        print ("No se han asignado sueldos")
        return None,None,None,None
    
    max_sueldo = max(sueldo)
    min_sueldo = min(sueldo)
    promedio_sueldo = sum(sueldo_trabajadores)/len(sueldo_trabajadores)
    media_aritmetica = statistics.geometric_mean(sueldo_trabajadores)
    


def reporte_sueldos(sueldo_trabajadores):
    with open ('sueldo_trabajadores.csv','w',newline=" ") as archivo:
        escritor = csv.writer (archivo)
        
        for trabajador,sueldo in sueldo_trabajadores:
            escritor.writerow([trabajador,sueldo])
    
    print ("Reporte generado en sueldo_trabajadores.csv")



    