# DataEngineering-Solution-Construction-Repository

## Inteligencia de Negocios
## Name: Victor Williams Cruz Mamani
## Código: 2022073903

## Resumen

Este repositorio contiene una solución de ingeniería de datos que implementa un
pipeline ETL (Extract, Transform, Load) para obtener y almacenar precios de
criptomonedas. El flujo consulta la API pública de CoinGecko, procesa los
precios de Bitcoin, Ethereum y Solana en dólares estadounidenses y guarda los
resultados en una tabla PostgreSQL alojada en Supabase.

## ¿Qué hace el proyecto?

El pipeline ubicado en `pipeline/main_flow.py` realiza las siguientes
actividades:

1. **Extracción:** consulta los precios actuales de Bitcoin, Ethereum y Solana
   mediante la API de CoinGecko.
2. **Transformación:** normaliza el símbolo de cada criptomoneda a mayúsculas y
   convierte el precio a un valor numérico (`price_usd`).
3. **Carga:** inserta los datos transformados en la tabla `crypto_rates` de
   Supabase usando una conexión PostgreSQL.
4. **Confirmación:** muestra en consola la cantidad de registros insertados.

El proceso valida los errores HTTP de la API y requiere la variable de entorno
`DATABASE_URL` para conectarse a la base de datos.

## Estructura del proyecto

```text
.
├── pipeline/
│   └── main_flow.py   # Lógica del pipeline ETL
├── requirements.txt   # Dependencias de Python
└── README.md          # Documentación del proyecto
```

## Requisitos

- Python 3
- Acceso a Internet para consultar CoinGecko
- Una base de datos PostgreSQL o un proyecto Supabase
- Una tabla `crypto_rates` con las columnas `symbol` y `price_usd`

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Configuración y ejecución

Define la cadena de conexión de PostgreSQL en la variable de entorno
`DATABASE_URL` y ejecuta:

```bash
python pipeline/main_flow.py
```

Si la ejecución es correcta, el pipeline mostrará un mensaje indicando cuántos
registros fueron insertados en Supabase.

## Beneficio del repositorio

Este repositorio demuestra un flujo completo de ingeniería de datos: obtiene
información real desde una API externa, transforma los datos y los almacena en
una base de datos PostgreSQL. Puede utilizarse como base para practicar ETL,
integración de APIs, almacenamiento de datos y generación de información útil
para el análisis y la toma de decisiones.

## Potencial del proyecto

El proyecto podría convertirse en una plataforma automatizada de análisis de
mercados financieros. Entre sus posibles evoluciones se encuentran el
almacenamiento histórico de precios, la ejecución programada del pipeline, la
incorporación de más indicadores y criptomonedas, y la creación de dashboards
interactivos para visualizar tendencias, variaciones y oportunidades de
análisis.
