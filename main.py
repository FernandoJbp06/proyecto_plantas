import functions.funciones as f 

print("1.Pedir al usuario el nombre de una planta y de una ciudad y presente el total de megavatios que han consumido dicha ciudad en dicha planta")
planta=input("ingresar el nombre de la planta: ").title()
planta=f.validar_planta(planta)
ciudad=input("ingresar el nombre de la ciudad: ").title()
cuidad=f.validar_CiudadEnPlanta(planta, ciudad)
print("El total de negativos de consumos para",cuidad,"en la planta",planta,"es:",f.total_anual_planta_ciudad(planta,ciudad))

print("\n2.Pedir al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves son los nombres de las plantas generadoras y el valor total")
ciudad=input("ingresar una ciudad: ").title()
ciudad=f.validar_ciudad(ciudad)
print("Diccionario para la ciudad de",ciudad,"\n",f.crear_diccionario_plantas_ciudad(ciudad))

print("\n3.Pedir el nombre de una región al usuario y presente cuanto dinero a recaudado la región sierra")
region=input("ingresar una región: ").lower()
region=f.validar_region(region)
print("Dinero recogido por la region",region,": $",f.total_region(region))

print("\n4.Total de megavatios consumo de una planta en un mes determinado")
planta=input("ingresar el nombre de una planta: ").title()
planta=f.validar_planta(planta)
mes=input("ingrese un mes: ")
mes=f.validar_mes(mes)
print("El total es: ",f.consumo_mes_planta(planta,mes))