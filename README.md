<img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps) - Mauro Ferrera'**</h1>

<p align="center">
<img src="https://tse3.mm.bing.net/th?id=OIP.LjaDN-lANs-PZ3Ni_TajnAHaF5&pid=Api&P=0&h=180"  height=300>

</p>
# HENRY Proyecto Integrador 1  
## Mauro Adan Ferrera
  

## ETL  
- realizado con el notebook 'etl_v41'
- Se trabaja con los datasets provistos para desanidar los datos y limpiarlos
- Se obtiene un df pre-procesado que sera utilizado posteriormente por la API, incluido en este repositorio como 'csv'
- nombre: 'MoviesDataset_v41.csv'

## EDA  
- realizado con el notebook 'eda_v1'

## API  
- realizada con FasrAPI
- deploy en Render disponible en: https://movies-v7.onrender.com/docs

## Sistema de recomendación  
- incluido como endpoint en la API
- utiliza una base de datos filtrada para las peliculas con 'popularity > 3', esto debido a la limitación de recursos memoria en la versión free de Render
- para realizarlo se aplicaron técnicas de reducción de la dimensionalidad para generar una matríz de similitud con las siguientes features:
- 1) 'title' y 'overview'
  2) 'collection'
  3) 'genres'
- El modelo elegido es K-vecinos
     
