from collections import namedtuple

import pandas as pd
import unidecode

casos_df = pd.read_csv(
    "./data_original_covid_positivo/datos_abiertos_siscovid_2020_05_22.csv",
    parse_dates=["FECHA_NACIMIENTO", "FECHA_PRUEBA"],
    encoding="latin",
)

ubigeo_df = pd.read_csv(
    "./extras/ubigeo_distritos.csv", dtype={"ubigeo": "string"}
)

# Cambiando mayusculas
casos_df.columns = [col.lower() for col in casos_df.columns]
casos_df[["sexo", "departamento", "provincia", "distrito"]] = casos_df[
    ["sexo", "departamento", "provincia", "distrito"]
].apply(lambda x: x.str.title().str.strip())

# Limpiando acentos para uniformizar data
casos_df[["departamento", "provincia", "distrito"]] = casos_df[
    ["departamento", "provincia", "distrito"]
].applymap(lambda x: unidecode.unidecode(x) if isinstance(x, str) else x)
ubigeo_df = ubigeo_df.applymap(
    lambda x: unidecode.unidecode(x) if isinstance(x, str) else x
)

# Casos de Callao se asigna departamento Callao
casos_df.loc[
    (casos_df.provincia == "Callao") & (casos_df.departamento == ""),
    "departamento",
] = "Callao"

# Ayuda para unir localizaciones con ubigeo
localizacion = (
    casos_df.groupby(["departamento", "provincia", "distrito"], as_index=False)
        .count()
        .loc[:, ["departamento", "provincia", "distrito"]]
)
merge_ubigeos = localizacion.merge(
    ubigeo_df, how="left", on=["departamento", "provincia", "distrito"]
)

# Correcciones en distritos y provincias para uniformizar nombres
Dcorreccion = namedtuple(
    "RemplazarDistrito", ["departamento", "provincia", "distrito", "cambio"]
)
Pcorreccion = namedtuple(
    "RemplazarDepartamento", ["departamento", "provincia", "cambio"]
)

correcciones_distrito = [
    ("Apurimac", "Chincheros", "Anco_Huallo", "Anco-Huallo"),
    (
        "Ayacucho",
        "Huamanga",
        "Andres Avelino Caceres",
        "Andres Avelino Caceres Dorregaray",
    ),
    ("Huanuco", "Huanuco", "Quisqui (Kichki)", "Quisqui"),
    ("Piura", "Sechura", "Rinconada Llicuar", "Rinconada-Llicuar"),
    ("San Martin", "Picota", "Caspisapa", "Caspizapa"),
    (
        "Tacna",
        "Tacna",
        "Coronel Gregorio Albarracin L.",
        "Coronel Gregorio Albarracin Lanchipa",
    ),
    ("Ucayali", "Atalaya", "Raymondi", "Raimondi"),
    (
        "Callao",
        "Prov. Const. Del Callao",
        "Carmen De La Legua Reynoso",
        "Carmen De La Legua-Reynoso",
    ),
]

for correccion in correcciones_distrito:
    data_correccion = Dcorreccion(*correccion)
    casos_df.loc[
        (casos_df["departamento"] == data_correccion.departamento)
        & (casos_df["provincia"] == data_correccion.provincia)
        & (casos_df["distrito"] == data_correccion.distrito),
        "distrito",
    ] = data_correccion.cambio

correcciones_provincia = [
    ("Callao", "Prov. Const. Del Callao", "Callao"),
    ("Ica", "Nazca", "Nasca"),
]

for correccion in correcciones_provincia:
    data_correccion = Pcorreccion(*correccion)
    casos_df.loc[
        (casos_df["departamento"] == data_correccion.departamento)
        & (casos_df["provincia"] == data_correccion.provincia),
        "provincia",
    ] = data_correccion.cambio

casos_df = casos_df.merge(
    ubigeo_df, how="left", on=["departamento", "provincia", "distrito"]
)

duplicated_uuid = casos_df[
    casos_df.groupby("uuid")["uuid"].transform("size") > 1
    ]

# Ayudante para identificar id duplicados
dedup = duplicated_uuid.merge(duplicated_uuid, how="left", on="uuid")

# Algunos casos que explican duplicados e inconsistencias en data

# Caso de fechas de nacimiento diferentes para mismo uuid sin missings
comp_nacimiento = dedup[
    (dedup.fecha_nacimiento_x.notnull())
    & (dedup.fecha_nacimiento_x != dedup.fecha_nacimiento_y)
    ]

# Casos donde mismo id es identificado como masculino y feminino
comp_fem_masc = dedup[
    (dedup.sexo_x.notnull() & dedup.sexo_y.notnull())
    & (dedup.sexo_x != dedup.sexo_y)
    ]

# Mismo id diferente departamento
comp_dpto = dedup[
    (dedup.departamento_x.notnull())
    & (dedup.departamento_x != dedup.departamento_y)
    ]

# Mismo id diferente provincia
comp_provincia = dedup[
    (dedup.provincia_x.notnull()) & (dedup.provincia_x != dedup.provincia_y)
    ]

# Mismo id diferente distrito
comp_distrito = dedup[
    (dedup.distrito_x.notnull()) & (dedup.distrito_x != dedup.distrito_y)
    ]

# Mismo id diferente fecha de prueba
comp_fecha_prueba = dedup[
    (dedup.tipo_prueba_x.notnull())
    & (dedup.fecha_prueba_x != dedup.fecha_prueba_y)
    ]

# Para limpiar casos de dobles con misma id, nos quedamos con
# las observaciones que menos campos vacios tienen
casos_df["num_vacios"] = casos_df.isnull().sum(axis=1)
casos_df = casos_df.sort_values(
    by=["uuid", "num_vacios", "fecha_prueba"], ascending=[True, True, False]
)
casos_df = casos_df.groupby(["uuid"], as_index=False).first()
casos_df = casos_df.drop(columns="num_vacios")
casos_df.to_csv(
    "./data_limpia/data_limpia_datos_siscovid_2020_05_22.csv", index=False
)

# ### Nueva data 2020-05-24

new_covid_data = pd.read_csv(
    "./data_original_covid_positivo/datos_abiertos_siscovid_2020_05_24.csv",
    parse_dates=["FECHA_RESULTADO"],
    encoding="latin",
    dtype={"EDAD": pd.Int64Dtype()},
)
new_covid_data.columns = [col.lower() for col in new_covid_data.columns]

# Uniformizando minusculas y limpiando caracteres especiales
new_covid_data[["departamento", "provincia", "distrito"]] = new_covid_data[
    ["departamento", "provincia", "distrito"]
].applymap(lambda x: unidecode.unidecode(x) if isinstance(x, str) else x)
new_covid_data[
    ["sexo", "departamento", "provincia", "distrito"]
] = new_covid_data[["sexo", "departamento", "provincia", "distrito"]].apply(
    lambda x: x.str.title().str.strip()
)

# Correcciones en distritos y provincias para uniformizar nombres
Dcorreccion = namedtuple(
    "RemplazarDistrito", ["departamento", "provincia", "distrito", "cambio"]
)
Pcorreccion = namedtuple(
    "RemplazarDepartamento", ["departamento", "provincia", "cambio"]
)

correcciones_distrito = [
    (
        "Ayacucho",
        "Huamanga",
        "Andres Avelino Caceres",
        "Andres Avelino Caceres Dorregaray",
    ),
    (
        "Ayacucho",
        "Huamanga",
        "Andres Avelino Caceres D.",
        "Andres Avelino Caceres Dorregaray",
    ),
    (
        "Tacna",
        "Tacna",
        "Coronel Gregorio Albarracin L.",
        "Coronel Gregorio Albarracin Lanchipa",
    ),
    (
        "Puno",
        "Sandia",
        "San Pedro De Putina Puncu",
        "San Pedro De Putina Punco",
    ),
    ("Ica", "Nazca", "Nazca", "Nasca"),
]

for correccion in correcciones_distrito:
    data_correccion = Dcorreccion(*correccion)
    new_covid_data.loc[
        (new_covid_data["departamento"] == data_correccion.departamento)
        & (new_covid_data["provincia"] == data_correccion.provincia)
        & (new_covid_data["distrito"] == data_correccion.distrito),
        "distrito",
    ] = data_correccion.cambio

correcciones_provincia = [("Ica", "Nazca", "Nasca")]

for correccion in correcciones_provincia:
    data_correccion = Pcorreccion(*correccion)
    new_covid_data.loc[
        (new_covid_data["departamento"] == data_correccion.departamento)
        & (new_covid_data["provincia"] == data_correccion.provincia),
        "provincia",
    ] = data_correccion.cambio

# Convertir data Region a Lima
new_covid_data.loc[new_covid_data.departamento == 'Lima Region', 'departamento'] = 'Lima'

# Ayuda para unir localiazaciones con ubigeo
localizacion = (
    new_covid_data.groupby(
        ["departamento", "provincia", "distrito"], as_index=False
    )
        .count()
        .loc[:, ["departamento", "provincia", "distrito"]]
)
merge_ubigeos = localizacion.merge(
    ubigeo_df, how="left", on=["departamento", "provincia", "distrito"]
)

merge_ubigeos = localizacion.merge(
    ubigeo_df, how="left", on=["departamento", "provincia", "distrito"]
)

new_covid_data.to_csv(
    "./data_limpia/data_limpia_datos_covid_2020_05_24.csv", index=False
)
