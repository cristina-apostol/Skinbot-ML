

![](/pictures/SKINBOT.png) 

# SKINBOT- PROJECT

## Proyecto final bootcamp Data Analysis



## Índice
1.[Contexto](#contexto)\
2.[Procedimiento](#procedimiento)\
3.[Próximos pasos](#próximospasos)
<a name="Contexto"/>

## Contexto
### ¿Qué es Skinbot? 

Skibot es un modelo de recomendación creado con machine learning para indicar diferentes rutinas faciales en base a la calificación de los usuarios de ciertos porductos y según su tipo de piel.

Esta idea surje en base a las tendencias actuales y el creciente interés por mantener una piel limpia y sana, y con la presmisa de poder ser aplicado como estrategia de marketing de una empresa de cosmética, de tipo engagement, o como un chatbot implantado en la propia página web.

<a name="Procedimiento"/>

## Procedimiento

Para llevar a cabo este proyecto se han puesto en práctica las siguientes herramientas:

<details>
<summary>ETL</summary>
<br>

- Extracción de datos mediante web sacraping de las páginas web, `Amazon` y `Skinsort`.
- Exploración y limpieza del dataset.

<br></details>
<details>
<summary>Modelo de recomendación</summary>
<br>

- Aplicación del modelo recomendador con filtro colaborativo, creando un usuario random para predecir en base a sus calificaiones que otros tipos de porductos le podría interesar.

<br></details>
<details>
<summary>Streamlit</summary>
<br>

Por último se ha llevado a cabo la creación de una aplicación online a través de Streamlit, para poder visualiar el modelo recomendador de manera gráfica.

<br></details>
<a name="próximospasos"/>
## Próximos pasos

Como futuras mejoras del proyecto se plantean los siguientes supuestos:
- Enriquecer el dataset para poder realizar filtros añadidos como por ejemplo, precio y tipos de ingredientes.
- Probar el entrenamiento de un modelo de reconocmiento facial para identificar el tipo de piel con una fotografía.
- Tener en cuenta las diferentes alergías que pueda tener una persona, y recomendar porductos en base a eso.
