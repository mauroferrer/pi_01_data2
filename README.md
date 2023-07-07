p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps) - Mauro Ferrera'**</h1>

<p align="center">
<img src="https://tse3.mm.bing.net/th?id=OIP.LjaDN-lANs-PZ3Ni_TajnAHaF5&pid=Api&P=0&h=180"  height=300>

</p>

## ¡Bienvenido/a a este proyecto donde haremos un proceso de ETL, un analisis EDA y un modelo de ML(Machine learning) para hacer un sistema de recomendacion, trabajando con plataformas de streaming  

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

### Debemos crear un sistema de recomendaciones que recomienda peliculas segun las peliculas vistas por el usuario 
### Nos situamos en el rol de un MLops Engineer
### Tenemos datos de películas y metadatos extraídos de plataformas de streaming que necesitamos transformar para obtener información relevante y permitir consultas a través de una API.
<hr>

## DESCRIPCION DE NUESTRO DATOS

### Característica         |  Descripción			
#### **adult:**	                *Indica si la película tiene califiación X, exclusiva para adultos.*			
#### **belongs_to_collection:**	*Un diccionario que indica a que franquicia o serie de películas pertenece la película*			
#### **budget:**	            *El presupuesto de la película, en dólares*			
#### **genres:**	            *Un diccionario que indica todos los géneros asociados a la película*			
#### **homepage:**	            *La página web oficial de la película*			
#### **id:**	                *ID de la pelicula*			
#### **imdb_id:**	            *IMDB ID de la pelicula*			
#### **original_language:**	    *Idioma original en la que se grabo la pelicula*			
#### **original_title:**	    *Titulo original de la pelicula*			
#### **overview:**	            *Pequeño resumen de la película*			
#### **popularity:**	        *Puntaje de popularidad de la película, asignado por TMDB (TheMoviesDataBase)*			
#### **poster_path:**	        *URL del póster de la película*			
#### **production_companies:**	*Lista con las compañias productoras asociadas a la película*			
#### **production_countries:**	*Lista con los países donde se produjo la película*			
#### **release_date:**	        *Fecha de estreno de la película*			
#### **revenue:**	            *Recaudación de la pelicula, en dolares*			
#### **runtime:**	            *Duración de la película, en minutos*			
#### **spoken_languages:**	    *Lista con los idiomas que se hablan en la pelicula*			
#### **status:**	            *Estado de la pelicula actual (si fue anunciada, si ya se estreno, etc)*			
#### **tagline:**	            *Frase celebre asociadaa la pelicula*			
#### **title:**	                *Titulo de la pelicula*			
#### **video:**	                *Indica si hay o no un trailer en video disponible en TMDB*			
#### **vote_average:**	        *Puntaje promedio de reseñas de la pelicula*
#### **vote_count:**	        *Numeros de votos recibidos por la pelicula, en TMDB*			




<hr>

## **PASO 1:**
### *ETL:*

### * Algunos campos, como belongs_to_collection, production_companies y otros están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, los desanidamos para poder hacer algunas de las consultas en la API!

### * Los valores nulos de los campos revenue, budget los rellenamos por el número 0.

### * Los valores nulos del campo release date los eliminamos.

### * A las columnas fechas, las pasamos al formato AAAA-mm-dd, además creamos la columna release_year donde extraemos el año de la fecha de estreno.

### * Creamos la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

### * Eliminamos  las columnas que no serán utilizadas, video, imdb_id, adult, original_title, poster_path y homepage.

               Econtramos el ETL en el archivo llamado "ETL.ipynb"

<hr>

## **PASO 2:**
### *Creamos las consultas y desarrollammos la API en donde se van a ejecutar las consultas( la creamos con FastAPI y Uvicorn)*

<hr>

#### def peliculas_idioma( Idioma: str ): Se ingresa un idioma (como están escritos en el dataset). Nos devuelve la cantidad de películas producidas en ese idioma.
                    
<hr>

#### def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Nos devuelve la duracion y el año.

<hr>

#### def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio

<hr>

#### def peliculas_pais( Pais: str ): Se ingresa un país (como están escritos en el dataset), retornando la cantidad de peliculas producidas en el mismo.
     
<hr>

#### def productoras_exitosas( Productora: str ): Se ingresa la productora, entregando el revenue total y la cantidad de peliculas que realizo.

<hr>

#### def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro del dataset devolviendo el éxito del mismo medido a través del retorno. Además, nos devuelve el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

<hr>

## **PASO 3:**
### *Creamos un* **deployment** *con render .donde vamos a poder ejecutar nuestras consultas y modelo de recomendacion desde una web* 
### **URL:** https://pi1-data12-ml.onrender.com/docs#/default 

<hr>

## **PASO 4:**
### *Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)*
### - Vemos el tipo de dato de cada columna para saber con que dats estamos trabajando
### - Visualizamos la cantidad de filas y columnas
### - Vemos la cantidad de nulos en cada columna 
### - Hacemos una descripcion estadistica de los datos numericos para conocer los minimos, maximos, media, etc.
### - Hacemos una descripcion estadistica de los datos tipo texto 
### - Mapa de calor con las correlaciones para identificar que tipo de correlacion tienen las columnas entre si, baja, media o alta
### - Hacemos deteccion de outliers para detectar valores incorrector o incoherentes
### - Histograma de los datos para resumir la informacion de los mismos
### - Nube de palabras para identificar los temas mas recurrentes

<hr>

## **PASO 5:**
### *Creamos el modelo que nos va a recomendar peliculas, segun la pelicula vista*
### *Utilizamos solo 20 mil filas del datasets
### *Convertimos el texto en una matriz de caracteristicas numericas para facilitar el calculo de similitudes
### *Remplazamos valores nulos por un espacio vacio para evitar errores
### *Analizamos y extraemos las palabras mas importantes con TF-IDF Y creamos una matriz que representa la importancia de las palabra en cada descripcion esto nos sirve para encontrar las peliculas similares
### *Calculamos la similitud coseno entre todas las descripciones la similitud coseno es una medida que nos indica cuanto se parecen dos vectores
### *Creamos una funcion recomendacion(titulo:str) y nos devuelve las 5 peliculas mas similares a la pelicula pasada como parametro
### *Accedemos a la fila 'idx' de la matriz 'simitulud coseno' enumeramos filas, creamos lista de tuplas, donde cada tupla contiene el indice y similitud coseno de la pelicula
### *Ordenamos la lista de tuplas en funcion de la similitud coseno de manera descendente, guardamos resultados en variable sim_scores
### *Creamos lista de las 5 mejores primeras peliculas
### *Seleccionamos los titulos segun los indices y los pasamos a una lista
### *Retornamos la lista

<hr>

### *LinkedIn*: https://www.linkedin.com/in/mauro-ferrera/
### ¡ Gracias por ver <3!