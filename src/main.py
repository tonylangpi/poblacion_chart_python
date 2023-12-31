import graficar_info
import leer_csv
import poblacion_por_pais

def run():
   res =  leer_csv.read_csv('./src/data.csv')
#    opc =  input("Digita un pais:")
#    pais = poblacion_por_pais.search_country(opc, res)
#    if len(pais) > 0:
#     graficar_info.generate_chart_bars(pais.keys(), pais.values())
# print("No se encontro el pais")
   country, per = poblacion_por_pais.generate_world_population(res)
   graficar_info.generate_chart_pie(country, per)
if __name__ == '__main__':
   run()