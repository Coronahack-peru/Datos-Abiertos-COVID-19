import zipfile
import uuid
import pandas as pd


def formatear_datos(input_file, output_file, delimiter=";", doctype="csv"):
    dir_unzip = './archivos_descomprimidos/'
    if doctype == "zip":
        with zipfile.ZipFile(input_file, 'r') as zip_ref:
            zip_ref.extractall(dir_unzip)
        input_file = "{}{}".format(dir_unzip, zip_ref.namelist()[0])
    df = pd.read_csv(input_file, encoding="ISO-8859-1",
                     delimiter=delimiter, error_bad_lines=False)
    df.to_csv(output_file, encoding="UTF-8", index=False, sep=",")

    return True


input_dir = './'
output_dir = './data_limpia/'

files = [
    {
        "nombre": "bonos_covid19.csv",
        "delimiter": ";"
    },
    {
        "nombre": "bonos_covid19.zip",
        "delimiter": ";"
    },
    {
        "nombre": "casos_positivos_covid19.csv",
        "delimiter": ","
    },
    {
        "nombre": "casos_positivos_covid19.zip",
        "delimiter": ","
    },
    {
        "nombre": "donaciones_covid19.csv",
        "delimiter": "|"
    },
    {
        "nombre": "data_donaciones_covid19.zip",
        "delimiter": "|"
    },
    {
        "nombre": "ejecucion_presupuestal_covid19.csv",
        "delimiter": "|"
    },
    {
        "nombre": "equiposdeprotecion_covid19.csv",
        "delimiter": ";"
    },
    {
        "nombre": "fallecidos_minsa_covid19.csv",
        "delimiter": ","
    },
    {
        "nombre": "fallecidos_sinadef_covid19.csv",
        "delimiter": ";"
    },
    {
        "nombre": "fallecidos_sinadef_covid19.zip",
        "delimiter": ";"
    },
]

identificador = str(uuid.uuid4())[:4]

# for filename in glob.glob("*.csv"):
for filename in files:
    print("Trabajando con archivo: {}".format(filename['nombre']))
    identificador_file = str(uuid.uuid4())[:4]
    input_file = "./{}".format(filename["nombre"])
    output_file = "{}{}_{}_{}.csv".format(
        output_dir, identificador, filename["nombre"][:-4], identificador_file)
    delimiter = filename["delimiter"]
    doctype = filename["nombre"][-3:]

    try:
        formatear_datos(input_file, output_file, delimiter, doctype)
        print("Se limpio correctamente los datos de {} y se envio a {}".format(input_file, output_file))
    except Exception as e:
        print("Error limpiando datos en archivo: {}.".format(input_file))
        print(e)
