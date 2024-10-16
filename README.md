# STAY_UNIQUE_TOLEDO_DAVID
Prueba tecnica

Este proyecto realiza el scraping de al menos 100 propiedades de hoteles en Booking.com y limpia los datos obtenidos. El script utiliza Playwright para automatizar el navegador, extraer datos de hoteles y transformarlos en un formato limpio.

## Estructura del Proyecto

```bash
.
├── web_scraping.py  # Código de scraping
├── data_processing.py   # Código para limpiar los datos
├── README.md            # Explicación del proyecto
├── requirements.txt     # Dependencias del proyecto
└── data/                # Archivos generados
```

## Configuración del Entorno

1. Instalar dependencias: Asegúrate de tener Python y pip instalados. Luego, instala las dependencias:

```bash
pip install -r requirements.txt
```

Se debe instalar todas las librerias que estan en el archivo requirements.txt

2. Instalar navegadores de Playwright: Ejecuta este comando para instalar los navegadores necesarios:

Nota: Utilicé Playwright en mi proyecto porque es una herramienta eficaz para automatizar navegadores y realizar scraping en sitios web dinámicos como Booking.com.

```bash
playwright install
```

## Ejecución del Proyecto

1. Ejecutar el scraping: Para comenzar el scraping de los hoteles, ejecuta:

```bash
python web_scraping.py
```

Esto generará un archivo CSV con los datos extraídos en la carpeta `data/hotels_list.csv`.

2. Limpiar los datos: Para limpiar, transformar y visualizar los datos obtenidos, ejecuta:

```bash
python data_processing.py
```

El archivo data_cleaning.py tiene tres funciones principales. La primera, clean_and_transform_data_scraping(), limpia los datos obtenidos de un proceso de web scraping que extrae información de hoteles de Booking.com. El archivo original con los datos (hotels_list.csv) se procesa para separar detalles como la disponibilidad y los precios. Finalmente, guarda la versión limpia en un nuevo archivo llamado hotels_list_cleaned.csv.

La segunda función, clean_and_transform_data_stay_unique(), trabaja con dos archivos de datos externos, info_properties.csv y reservas_info.csv. Estos contienen información sobre propiedades y reservas. La función fusiona ambos archivos, calcula nuevas métricas como la tasa de ocupación y los ingresos por noche, y luego guarda el resultado en stay_unique_merged.csv.

La última función, eda_process(), realiza un análisis exploratorio de los datos fusionados. Crea una matriz de correlación para las variables numéricas y genera gráficos para una mejor visualización de los datos.


## Descripción del Pipeline de ETL

El proceso de ETL (Extract, Transform, Load) implementado sigue los siguientes pasos:

- **Extract (Extracción)**: Se realiza un scraping de propiedades en Booking.com mediante el script web_scraping.py, que extrae información como precios, disponibilidad y puntuaciones de hoteles, y almacena estos datos en un archivo CSV llamado hotels_list.csv. Luego se cargó dos archivos externos, info_properties.csv y reservas_info.csv, que contienen información sobre las propiedades y reservas.

- **Transform (Transformación)**: Los datos extraídos pasan por varios procesos de limpieza y mejora. Primero, en los datos de scraping, se limpian y reorganizan columnas como disponibilidad y precios, eliminando información irrelevante o fragmentada, y estructurando mejor los detalles. Estos datos limpios se guardan en un nuevo archivo CSV llamado hotels_list_cleaned.csv. Luego, los datos de las propiedades y reservas se fusionan, calculando nuevas métricas como la tasa de ocupación y el ingreso por noche, a partir de las columnas existentes. También se procesan correctamente las fechas para evitar errores en el análisis.

- **Load (Carga)**: Los datos transformados se guardan en un archivo llamado stay_unique_merged.csv. Este archivo contiene los datos fusionados de propiedades y reservas. Además, se realiza un análisis exploratorio de los datos, generando visualizaciones como una matriz de correlación entre variables numéricas y un gráfico que muestra los ingresos totales por canal de reserva. De esta manera, se tiene información a nivel general y detallado sobre los datos. Estos archivos tambien podrían ingresarse a un motor de base de datos como PostgreSql para un mejor manejo y performance a nivel de tablas.

## Retos y Problemas

- **Identificadores en la página**: Fue un algo complicado encontrar la manera de poder identificar los ID de donde estaban ubicado la información de cada propiedad y adaptarlo al código para su extracción.
- **Datos faltantes**: A veces, algunos hoteles no muestran el precio o la puntuación de reseñas. Se manejan estos casos asignando 'N/A' cuando los datos no están disponibles para que el proceso continúe sin fallos.
- **Análisis de datos**: Finalmente, al momento del análisis de datos surgio algunos problemas, especialmente al trabajar con múltiples variables y correlaciones. Al principio, la visualización de los resultados no era clara, así que ajusté las gráficas para que fueran más legibles.
