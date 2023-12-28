import matplotlib.pyplot as plt
import csv
import re

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    info = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      info.append(country_dict)
    return info
#***********************
def search_country(country, data):
    try:
        copia_datos = data.copy() #copia de la lista de diccionarios
        regex = "[0-9]{4} Population" #regex para detectar las columnas de poblacion
        pais_encontrado = list(filter(lambda x: x['Country/Territory'] == country, copia_datos))
        objeto_pais_encontrado = { key: int(value) for key,value in pais_encontrado[0].items() if re.match(regex,key)} #genera un diccionario solo con las poblaciones del pais buscado por el usuario
        return objeto_pais_encontrado
    except TypeError:
        return "error"
    
def generate_chart(labels, vals):
    fig, ax = plt.subplots()
    ax.bar(labels, vals)
    plt.show()
    
def generate_chart_pie(labels, vals):
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    #generate_chart(['A', 'B', 'C'], [1, 2, 3])
    #generate_chart_pie(['A', 'B', 'C'], [1, 2, 3])
  res =  read_csv('./src/data.csv')
  opc =  input("Digita un pais:")
  pais = search_country(opc, res)
  generate_chart(pais.keys(), pais.values())