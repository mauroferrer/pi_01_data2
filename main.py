import pandas as pd
import numpy as np 
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def presentacion():
    return 'Mauro_Ferrera'

data = pd.read_csv("Data_pelicula_preparada.csv")



@app.get("/peliculas_idioma/{idioma}")
def peliculas_idioma(idioma:str):
    idioma_filtro = data[data['name_languague'] == idioma]
    cantida_pelis =  idioma_filtro['name_languague'].shape[0]
    return {'idioma:':idioma, 'cantidad peliculas:':cantida_pelis}



@app.get("/peliculas_duracion/{pelicula}")
def peliculas_duracion(pelicula:str):
    peli_filtro = data[data['title'] == pelicula]
    duracion =  peli_filtro['runtime']
    año = peli_filtro['release_year']
    return {'PELICULA:':pelicula, 'duracion en minutos:':duracion, 'año de estreno:':año } 



@app.get("/franquicia/{franquicia}")
def franquicia(franquicia:str):
    franquicia_filtro = data[data['name_collection'] == franquicia]
    cantidad_pelis = data['name_collection'].shape[0]
    ganancia = data['revenue'].sum()
    promedio = data['revenue'].mean()
    return {'franquicia:':franquicia, 'ganancias totales generadas:':ganancia, 'ganancia promedio:':promedio}



@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais:str):
    pais_filtro = data[data['name_countrie'] == pais]
    cantidad = pais_filtro['name_countrie'].shape[0]
    return{'pais:':pais, 'cantidad de peliculas creadas:':cantidad}



@app.get("/productoras_exitosas/{productora}")
def productora_exitosa(productora:str):
    productora_filtro = data[data['name_production'] == productora]
    cantidad = productora_filtro['revenue'].sum()
    cantidad_peliculas = productora_filtro['name_production'].shape[0]
    return{'productora:':productora, 'ganancias totales:':cantidad, 'cantidad de peliculas generadas:':cantidad_peliculas}



@app.get("/get_director/{director}")
def get_director(director:str):
   director_data = data[data['name_director'].apply(lambda x: director in x if isinstance(x, (list, str)) else False)].head(5)
   ganancias_totales = director_data['revenue'].sum()
   peliculas = []
   for _, row in director_data.iterrows():
        titulo = row['title']
        fecha_estreno = row['release_date']
        retorno = row['return']
        peliculas.append({'titulo': titulo, 'fecha_estreno': fecha_estreno, 'retorno':retorno})
    
   return {'nombre del director': director, 'retorno total': ganancias_totales, 'peliculas': peliculas}