### IMPORTAMOS LIBRERIAS

import pandas as pd
import numpy  as np

from fastapi import FastAPI

import uvicorn

from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.utils.extmath           import randomized_svd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise        import linear_kernel


app = FastAPI()



### PRESENTACION:
### Creaoms consulta como presentacion con nuestro nombre
@app.get('/')
def presentacion():
    return 'Mauro_Ferrera'

### IMPORTAMOS LOS DATOS
data = pd.read_csv("Data_pelicula_preparada.csv")


### CONSULTA 1:
# Creamos una consulta donde nos devuelve la cantidad de peliculas creadas en el idioma pasado como parametro 
@app.get("/peliculas_idioma/{idioma}")
def peliculas_idioma(idioma:str):
    idioma_filtro = data[data['name_languague'] == idioma]
    cantida_pelis =  idioma_filtro['name_languague'].shape[0]
    return {'idioma:':idioma, 'cantidad peliculas:':cantida_pelis}


### CONSULTA 2:
# Creamos la consulta que nos devuelve la duracion en minutos y el año de estreno de la pelicula pasada como parametro
@app.get("/peliculas_duracion/{pelicula}")
def peliculas_duracion(pelicula:str):
    peli_filtro = data[data['title'] == pelicula]
    duracion =  peli_filtro['runtime']
    año = peli_filtro['release_year']
    return {'PELICULA:':pelicula, 'duracion en minutos:':duracion, 'año de estreno:':año } 


### CONSULTA 3:
# Creamos la consulta que nos devuelve las ganancias totales y la ganancia promedio de la franquicia pasada como parametro
@app.get("/franquicia/{franquicia}")
def franquicia(franquicia:str):
    franquicia_filtro = data[data['name_collection'] == franquicia]
    cantidad_pelis = data['name_collection'].shape[0]
    ganancia = data['revenue'].sum()
    promedio = data['revenue'].mean()
    return {'franquicia:':franquicia, 'ganancias totales generadas:':ganancia, 'ganancia promedio:':promedio}


### CONSULTA 4:
# Consulta que nos devuelve la cantidad de peliculas creadas en el pais pasado como parametro
@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais:str):
    pais_filtro = data[data['name_countrie'] == pais]
    cantidad = pais_filtro['name_countrie'].shape[0]
    return{'pais:':pais, 'cantidad de peliculas creadas:':cantidad}


### CONSULTA 5:
# Consulta que devuelve las ganancias generadas y cantidad de peliculas de la productora que le pasemos como parametro
@app.get("/productoras_exitosas/{productora}")
def productora_exitosa(productora:str):
    productora_filtro = data[data['name_production'] == productora]
    cantidad = productora_filtro['revenue'].sum()
    cantidad_peliculas = productora_filtro['name_production'].shape[0]
    return{'productora:':productora, 'ganancias totales:':cantidad, 'cantidad de peliculas generadas:':cantidad_peliculas}


### CONSULTA 6:
# Consulta que devuelve una lista con las 5 peliculas creadas por el director pasado como parametro, devolviendo su retorno total, fecha de estreno y nombre de cada pelicula
@app.get("/get_director/{director}")
def get_director(director:str):
   director_data = data[data['name_director'].apply(lambda x: director in x if isinstance(x, (list, str)) else False)].head(5)
   ganancias_totales = director_data['revenue'].sum()
   peliculas = []
   for _, row in director_data.iterrows():
        titulo = row['title']
        fecha_estreno = row['release_date']
        retorno = row['return']
        costo = row['budget']
        ganancia = row['revenue']
        peliculas.append({'titulo': titulo, 'fecha_estreno': fecha_estreno, 'retorno':retorno, 'ganancia generada:':ganancia, 'coste de la pelicula:': costo})
    
   return {'nombre del director': director, 'retorno total': ganancias_totales, 'peliculas': peliculas}



      ### CREACION DEL MODELO DE RECOMENDACIONES ### 

muestra_aleatoria = data.head(20000) # Utilizamos solo 20 mil filas del datasets 

tfidf = TfidfVectorizer(stop_words='english') #Convertimos el texto en una matriz de caracteristicas numericas

muestra_aleatoria['overview'] = muestra_aleatoria['overview'].fillna('') # Remplazamos valores nulos por un espacio vacio para evitar errores

tdfid_matrix = tfidf.fit_transform(muestra_aleatoria['overview']) # Analizamos y extraemos las palabras mas importantes con TF-IDF Y creamos una matriz que representa la
                                                                        #importancia de las palabra en cada descripcion, esto nos sirve para encontrar las peliculas similares


cosine_similarity = linear_kernel( tdfid_matrix, tdfid_matrix) # Calculamos la similitud coseno entre todas las descripciones la similitud coseno 
                                                                 # es una medida que nos indica cuanto se parecen dos vectores 



### Creamos la funcion 'recomendacion' que nos va a recomendar 5 peliculas en base al parametro titulo que le pasemos. ###

def recomendacion(titulo: str):
    idx = muestra_aleatoria[muestra_aleatoria['title'] == titulo].index[0] # Buscamos el indice titulo en nuestro datasets

    sim_cosine = list(enumerate(cosine_similarity[idx])) # Accedemos a la fila 'idx' de la matriz 'simitulud coseno' enumeramos filas, creamos lista de 
                                                             #tuplas, donde cada tupla contiene el indice y similitud coseno de la pelicula
    

    sim_scores = sorted(sim_cosine, key=lambda x: x[1], reverse=True) # Ordenamos la lista de tuplas en funcion de la similitud coseno de manera descendente,
                                                                         #guardamos resultados en variable sim_scores
    

    similar_indices = [i for i, _ in sim_scores[1:6]] # Creamos lista de las 5 mejores primeras peliculas

    similar_movies = muestra_aleatoria['title'].iloc[similar_indices].values.tolist() # Seleccionamos los titulos segun los indices y los pasamos a una lista
    
    return similar_movies #Retornamos la lista

### RESUMEN:
### En resumen creamos una funcion que toma el titulo de una pelicula y encuentra las peliculas mas similares basandose en la similitud del coseno 
### de las descripciones de las peliculas devolviendo una lista con 5 peliculas
