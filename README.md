# Spotify ETL Project

  

Este proyecto de extracción, transformación y carga (ETL) se conecta a la API de Spotify para analizar patrones de escucha y almacenar datos relevantes en una base de datos PostgreSQL. La información extraída se utiliza para explorar estadísticas de tus canciones favoritas, analizar tendencias y visualizar patrones de escucha a través de un dashboard en Looker Studio.

  
## Tabla de Contenidos

  

- [Instalación](#instalación)

- [Configuración](#configuración)

- [Ejecución](#ejecución)

- [Automatización](#automatización)

- [Análisis de Datos en SQL](#análisis-de-datos-en-sql)

- [Visualización en Looker Studio](#visualización-en-looker-studio)

- [Estructura del Proyecto](#estructura-del-proyecto)
  
  
  
## Instalación
  
1. Clona el repositorio: 
 
```bash 
git clone https://github.com/usuario/spotify-etl.git cd spotify-etl
```

2. Crea y activa un entorno virtual
```bash
python -m venv venv source venv/bin/activate # En macOS/Linux 

.\\venv\\Scripts\\activate # En Windows
```
3. Instala las dependencias
```bash
pip install -r requirements.txt
```

## Configuración

1. Crea un archivo `.env`  en la raíz del proyecto con las siguientes variables:
 ```plaintext
 SPOTIPY_CLIENT_ID='tu_client_id' 
 SPOTIPY_CLIENT_SECRET='tu_client_secret' 
 SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
 ```
2. Crea una base de datos SQL
```sql
CREATE DATABASE spotify_db;
```
3. Configura las tablas necesarias en PostgreSQL. La tabla principal es `spotify_tracks`, con la estructura siguiente:
```sql
CREATE TABLE spotify_tracks ( 
	track_id VARCHAR PRIMARY KEY, 
	track_name VARCHAR, 
	artist_name VARCHAR, 
	album_name VARCHAR, 
	played_at TIMESTAMP, 
	duration_ms INTEGER, 
	popularity INTEGER 
);
```

## Ejecución
Para ejecutar el proceso ETL una vez, activa tu entorno virtual y ejecuta el archivo `spotify_etl.py`:

```bash
python spotify_etl.py
```
Este comando extraerá los datos de Spotify, los transformará y los cargará en tu base de datos PostgreSQL.

## Automatización 
Para automatizar el proceso ETL usando el Task Scheduler de Windows:

1.  Abre el Programador de tareas (Task Scheduler).
2.  Crea una nueva tarea y selecciona la frecuencia deseada (diario, semanal, etc.).
3.  Configura el programa a ejecutar:
    -   Ruta: `C:\\ruta\\de\\tu\\python.exe`
    -   Argumentos: `C:\\ruta\\de\\spotify-etl\\spotify_etl.py`

## Análisis de datos SQL

Una vez que los datos estén en la base de datos PostgreSQL, puedes realizar consultas SQL para analizar patrones de escucha. Ejemplos de consultas:

-   Canciones más escuchadas:
    
```sql
    SELECT track_name, artist_name, COUNT(*) as play_count
    FROM spotify_tracks
    GROUP BY track_name, artist_name
    ORDER BY play_count DESC
    LIMIT 10;
```
    
-   Artistas más populares:
    
```sql 
    SELECT artist_name, AVG(popularity) as avg_popularity
    FROM spotify_tracks
    GROUP BY artist_name
    ORDER BY avg_popularity DESC
    LIMIT 10;
```

## Visualización en Looker Studio

 1. Crea una cuenta en [Looker Studio](https://lookerstudio.google.com/)
 
 3.  Si aún no tienes una. Conecta Looker Studio a tu base de datos
    PostgreSQL. 
    
 4. Diseña un dashboard para visualizar las tendencias de
    escucha, como canciones más escuchadas y artistas más populares.

## Estructura del Proyecto

```
spotify_etl_project/ 
│ 
├── etl.py # Script principal del ETL 
├── config/ 
│ └── config.py # Configuración de la API de Spotify 
├── utils/ 
│ ├── spotify_api.py # Funciones para la extracción de la API de Spotify 
│ └── transform.py # Funciones para transformar los datos 
│ 
├── analysis/ 
│ └── queries.sql # Consultas SQL de análisis 
│ 
├── requirements.txt # Librerías necesarias 
├── .env # Variables de entorno (credenciales) 
├── .gitignore # Archivos a ignorar por Git 
└── README.md # Descripción del proyecto
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un fork del proyecto y envía tus pull requests con mejoras o nuevas funcionalidades.




