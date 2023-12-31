import re

#***********************
def search_country(country, data):
    try:
        copia_datos = data.copy() #copia de la lista de diccionarios
        regex = "[0-9]{4} Population" #regex para detectar las columnas de poblacion
        pais_encontrado = list(filter(lambda x: x['Country/Territory'] == country, copia_datos))
        if len(pais_encontrado) > 0:
           objeto_pais_encontrado = { key: int(value) for key,value in pais_encontrado[0].items() if re.match(regex,key)} #genera un diccionario solo con las poblaciones del pais buscado por el usuario
           return objeto_pais_encontrado
        return pais_encontrado
    except TypeError:
        return "error"
#obtener un grafico de pastel con la World Population Percentage 
def generate_world_population(data):
    try:
        copia_datos = data.copy() #copia de la lista de diccionarios
        percentages_dict = {item["Country/Territory"]: item["World Population Percentage"] for item in copia_datos}
        countries = percentages_dict.keys()
        percentage = percentages_dict.values()
        return countries, percentage
    except TypeError:
        return "error"
    