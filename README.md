# 3 - Limpieza de Datos

La página Global Shark Attack https://www.sharkattackfile.net/  lleva un control de los
accidentes que se producen por ataques de tiburones en el mundo.

El dataset puede descargarse de: https://www.sharkattackfile.net/incidentlog.htm

Registran los siguientes datos:

![dataset](img/dataset.png)

## Análisis
**A partir de la información provista por la página de referencia, se analiza la cantidad de incidentes de cada tipo por país.
Para ver en detalle el paso a paso del análisis, y observar los distintos criterios adoptados, ver:** [**-> Notebook**](notebook.ipynb)

## Limpieza del Campo Age

El módulo [clean_age.py](clean_age.py) implementa funciones para estandarizar y normalizar el campo de edad en el dataset. Este proceso incluye:

- Extracción de valores numéricos de cadenas de texto variadas
- Conversión de rangos de edad a valores únicos representativos
- Manejo de formatos inconsistentes y datos ambiguos

Si bien el módulo mejora significativamente la estandarización del campo `age`, **no es 100% efectivo** debido a la alta variabilidad y calidad inconsistente de los datos originales. Algunos registros contienen información ambigua, incompleta o en formatos no estructurados que dificultan su procesamiento automático.

### Mejoras Futuras

Este módulo representa una solución basada en reglas que podría beneficiarse de técnicas más avanzadas:

- **LLM-based cleaning**: Implementar un método de limpieza basado en modelos de lenguaje (LLM) que pueda interpretar contexto y manejar casos edge de forma más inteligente
- **Validación cruzada**: Correlacionar edad con otros campos para detectar inconsistencias

El clean_age.py es funcional para el análisis actual, pero queda identificado como un área de mejora prioritaria para futuras iteraciones del proyecto.


## Resultados
En la siguiente tabla se puede observar para cada país (ordenado por cantidad de incidentes en forma descendente) la cantidad encontrada por tipo de ataque.

![Tabla Resultado](img/tabla_ref_cruz.png)

También se proveen como resultado del análisis:
- Archivo Excel: `analisis_ataques_tiburones`
- Imágen de mapa formato png: `mapa_ataques_tiburones`
- Imágen de mapa formato svg: `mapa_ataques_tiburones`
- Archivo original fuente de datos: `GSAF5`

## Análisis Geográfico de Ataques

El siguiente mapa muestra la distribución global de ataques de tiburón, con cada país coloreado según el número total de ataques registrados. Los países con más ataques aparecen en tonos más oscuros de rojo, lo que permite identificar rápidamente las regiones más afectadas por este fenómeno.

![Mapa Global de Ataques de Tiburón](img/mapa_ataques_tiburones.png)

