# ETL de Celulares de la tienda Hiraoka

## Descripción

Este proyecto implementa un proceso ETL (Extract, Transform, Load) para procesar catálogos de productos de celulares obtenidos en formato JSON.

El flujo realiza la lectura de archivos JSON, la limpieza de datos, la transformación de precios a formato numérico y la generación de archivos Excel listos para análisis o distribución.

## Funcionalidades

* Lectura de archivos JSON.
* Limpieza de nombres de marca.
* Conversión de precios monetarios a formato numérico.
* Exportación de datos procesados a Excel.
* Generación automática de archivos utilizando la fecha actual del sistema.

## Estructura del Proyecto

```text
project/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   │   └── Celulares_YYYYMMDD.json
│   │
│   └── clean/
│       └── Celulares_YYYYMMDD.xlsx
│
└── .venv/
```

## Versión de Python

Este proyecto fue desarrollado utilizando:

```text
Python 3.12.7
```

Verificar la versión instalada:

```bash
python --version
```

Resultado esperado:

```text
Python 3.12.7
```

## Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

## Crear el Entorno Virtual

Windows:

```bash
python -m venv .venv
```

## Activar el Entorno Virtual

Windows:

```bash
.venv\Scripts\activate
```

Si la activación fue exitosa, la consola mostrará algo similar a:

```text
(.venv) C:\Proyectos\MiProyecto>
```

## Instalar Dependencias

Una vez activado el entorno virtual:

```bash
pip install -r requirements.txt
```

## Actualizar el Archivo requirements.txt

Si se agregan nuevas librerías al proyecto:

```bash
pip freeze > requirements.txt
```

## Ejecución del Proyecto

Desde la carpeta raíz del proyecto ejecutar:

```bash
python main.py
```

## Flujo de Procesamiento

El proceso realiza las siguientes actividades:

### 1. Extracción

Lee un archivo JSON ubicado en:

```text
data/raw/Celulares_YYYYMMDD.json
```

### 2. Transformación

Se aplican las siguientes reglas:

* Eliminación de saltos de línea y espacios adicionales en la columna Marca.
* Conversión de PrecioRegular a tipo numérico.
* Conversión de PrecioOnline a tipo numérico.
* Limpieza de símbolos monetarios (S/).
* Eliminación de separadores de miles.

### 3. Carga

Genera un archivo Excel en:

```text
data/clean/Celulares_YYYYMMDD.xlsx
```

## Dependencias Principales

* pandas
* openpyxl
* xlsxwriter

## Datos de Entrada

El archivo JSON debe contener una estructura similar a:

```json
{
    "Url": "https://ejemplo.com",
    "Codigo": "12345",
    "Marca": "SAMSUNG",
    "Descripcion": "Celular Samsung Galaxy",
    "PrecioRegular": "S/ 1,299.00",
    "PrecioOnline": "S/ 1,159.00"
}
```

## Datos de Salida

El archivo Excel generado contendrá las columnas:

* Url
* Codigo
* Marca
* Descripcion
* PrecioRegular
* PrecioOnline

Las columnas de precios serán exportadas como valores numéricos para facilitar análisis posteriores.

## Autor

**Edgar Quispe**  
*Azure Data Engineer*

Desarrollo de soluciones ETL, Data Warehousing, integración de datos y automatización de procesos utilizando Python, Azure Data Factory, SQL Server y tecnologías analíticas modernas.

LinkedIn: https://www.linkedin.com/in/edgar-quispe-151051167/