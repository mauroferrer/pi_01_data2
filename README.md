![image](https://github.com/mauroferrer/pi_01_data2/assets/100243583/5f25ec9a-0d6e-42f6-b54b-a384a4c3e041)

# HENRY Proyecto Integrador 1  
## Mauro Adan Ferrera
pi_01_data2  

## ETL  
- realizado con el notebook 'ETL.ipynb'
- Se trabaja con los datasets provistos para desanidar los datos y limpiarlos
- Se obtiene un df pre-procesado que sera utilizado posteriormente por la API, incluido en este repositorio como 'csv'
- nombre: 'Data_reprarada_pelicula.csv'

## EDA  
- realizado con el notebook 'EDA.ipynb'

## API  
- realizada con FasrAPI
- deploy en Render disponible en: https://movies-v7.onrender.com/docs

## Sistema de recomendación  
En este proyecto tuve como propósito desarrollar un modelo de recomendaciones de películas, haciendo
uso de una amplia variedad de datos relacionados con películas, actores, fechas, entre otros aspectos
relevantes de esta área.  El modelo que nos va a recomendar 5 películas, según la película pasada como parametro, 


- incluido como endpoint en la API
- utiliza una base de datos filtrada para las peliculas con 'popularity > 3', esto debido a la limitación de recursos memoria en la versión free de Render
- para realizarlo se aplicaron técnicas de reducción de la dimensionalidad para generar una matríz de similitud con las siguientes features:
- 1) 'title' y 'overview'
  2) 'collection'
  3) 'genres'
- El modelo elegido es K-vecinos

modelo va a recomendar las películas más similares en base a la descripción y título de la película
vista por el usuario
