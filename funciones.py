import data1.PlantaElec as plel


def validar_planta(planta):
  plantas=list(plel.consumo_energia.keys())
  while planta not in plantas:
    planta=input('No existe esta planta: Ingrese el nombre de una planta: ').title()
  return planta

def validar_CiudadEnPlanta(planta,ciudad):
  while ciudad not in plel.consumo_energia[planta]:
    ciudad=input('Ciudad no encontrada: Ingrese una ciudad para esa planta: ').title()
  return ciudad

def total_anual_planta_ciudad(planta,ciudad):
  consumos=plel.consumo_energia[planta][ciudad]['consumos']
  tarifa=plel.consumo_energia[planta][ciudad]['tarifa']
  return sum(consumos)*tarifa

def validar_ciudad(ciudad):
  ciudades=list(plel.informacion['costa'])+list(plel.informacion['sierra'])+list(plel.informacion['oriente'])
  while ciudad not in ciudades:
    ciudad=input('Ciudad no encontrada: Ingrese una ciudad: ').title()
  return ciudad

def crear_diccionario_plantas_ciudad(ciudad):
  diccionario={}
  for planta in plel.consumo_energia:
    if ciudad in plel.consumo_energia[planta]:
      diccionario[planta]=total_anual_planta_ciudad(planta,ciudad)
  return diccionario

def validar_region(region):
  while region not in ['costa','sierra','oriente']:
    region=input('Región no encontrada: Ingrese una región: ').lower()
  return region

def total_region(region):
  cdRegion=plel.informacion[region]
  total=0
  for ciudad in cdRegion:
    total+=sum(list(crear_diccionario_plantas_ciudad(ciudad).values()))
  return total

def validar_mes(mes):
  0,1,2,3,4,5,6,7,8,9,10,11
  while not(mes.isdigit()) or int(mes)<0 or int(mes)>11:
    mes=input('Mes equivocado: Ingrese un mes: ')
  return int(mes)

def consumo_mes_planta(planta,mes):
  total=0
  for ciudad in plel.consumo_energia[planta]:
    consumo=plel.consumo_energia[planta][ciudad]['consumos'][mes]
    tarifa=plel.consumo_energia[planta][ciudad]['tarifa']
    total+=consumo*tarifa
  return total