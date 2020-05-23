# Información de los archivos csv

## bonos_covid19.csv

Ejemplo: importar usando Python/Pandas

``` python
import pandas as pd
df = pd.read_csv('bonos_covid19.csv', encoding = "ISO-8859-1", delimiter =';’)
```

### Características
| Tipo         | Valor      |
|--------------|------------|
| CODIFICACIÓN | ISO-8859-1 |
| DELIMITADOR  | ,          | 
| UBIGEO       | SI         |
| DEPARTAMENTO | SI         |
| PROVINCIA    | SI         |
| DISTRITO     | SI         |
| ERRORES      | NO         |

## casos_positivos_covid19.csv

Ejemplo: importar usando Python/Pandas

``` python
import pandas as pd
df = pd.read_csv('casos_positivos_covid19.csv', encoding = "ISO-8859-1", delimiter =',’)
```

### Características
| Tipo         | Valor      |
|--------------|------------|
| CODIFICACIÓN | ISO-8859-1 |
| DELIMITADOR  | ,          | 
| UBIGEO       | NO         |
| DEPARTAMENTO | SI         |
| PROVINCIA    | SI         |
| DISTRITO     | SI         |
| FECHA        | ISO 8601   |  
| ERRORES      | NO         |

## donaciones_covid19.csv

Ejemplo: importar usando Python/Pandas

``` python
import pandas as pd
df = pd.read_csv('donaciones_covid19.csv', encoding = "ISO-8859-1", delimiter ='|', parse_dates=['FECHA_MOVIMTO', 'FECHA_REG', 'FECHA_CONFIRMA'], error_bad_lines=False)
```

### Características
| Tipo         | Valor      |
|--------------|------------|
| CODIFICACIÓN | ISO-8859-1 |
| DELIMITADOR  | |          | 
| UBIGEO       | NO         |
| DEPARTAMENTO | NO         |
| PROVINCIA    | NO         |
| DISTRITO     | NO         |
| FECHA        | %d/%m/%Y %H:%M:%S  |  
| ERRORES      | SI         |


## ejecucion_presupuestal_covid19.csv

Ejemplo: importar usando Python/Pandas

``` python
import pandas as pd
df = pd.read_csv('ejecucion_presupuestal_covid19.csv', delimiter ='|')
```

### Características
| Tipo         | Valor      |
|--------------|------------|
| CODIFICACIÓN | ISO-8859-1 |
| DELIMITADOR  | |          | 
| UBIGEO       | NO         |
| DEPARTAMENTO | SI         |
| PROVINCIA    | SI         |
| DISTRITO     | SI         |
| ERRORES      | NO         |


## fallecidos_minsa_covid19.csv

Ejemplo: importar usando Python/Pandas

``` python
import pandas as pd
df = pd.read_csv('fallecidos_minsa_covid19.csv', encoding = "ISO-8859-1", delimiter =',', parse_dates=['fecha_fallecimiento', 'fecha_nacimiento'])
```

### Características
| Tipo         | Valor      |
|--------------|------------|
| CODIFICACIÓN | ISO-8859-1 |
| DELIMITADOR  | ,          | 
| UBIGEO       | NO         |
| DEPARTAMENTO | SI         |
| PROVINCIA    | SI         |
| DISTRITO     | SI         |
| FECHA        | ISO 8601   |  
| ERRORES      | NO         |


## fallecidos_sinadef_covid19.csv

Ejemplo: importar usando Python/Pandas

``` python
import pandas as pd
df = pd.read_csv('fallecidos_sinadef_covid19.csv', encoding = "ISO-8859-1", delimiter =';', parse_dates=['FECHA']) 
```

### Características
| Tipo         | Valor      |
|--------------|------------|
  | DELIMITADOR  | ;          |
| UBIGEO       | SI         |
| DEPARTAMENTO | SI         |
| PROVINCIA    | SI         |
| DISTRITO     | SI         |
| FECHA        | ISO 8601   |  
| ERRORES      | NO         |


