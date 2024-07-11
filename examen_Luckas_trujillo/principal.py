
import funciones as fn

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez", "Isabel Gómez","Francisco Díaz","Elena Fernández"]


sueldo_trabajadores = {}

while True:
    print ("MENU")
    print ("1. Asignar sueldos aleatorios")
    print ("2. Clasificar Sueldos")
    print ("3. Ver estadísticas")
    print ("4. Reporte de sueldos")
    print ("5. Salir")
    opc_usuario = int(input("Opción: "))
    if opc_usuario == 1:
        fn.asignar_sueldos_aleatorios(trabajadores)
    else:
        if opc_usuario == 2:
                fn.clasificar_sueldos(sueldo_trabajadores)
        else:
            if opc_usuario == 3:
                fn.ver_estadisticas(sueldo_trabajadores)
            else:
                if opc_usuario == 4:
                    fn.reporte_sueldos(sueldo_trabajadores)
                else:
                    if opc_usuario == 5:
                        print ("Finalizando Programa")
                        print ("Realizado por Luckas Trujillo")
                        print ("R.U.T.: 18.618.540-4")
                        break
                    else:
                        print ("Opción incorrecta, intente nuevamente")

