import sys
import glob
import pandas as pd


def formatear_datos(input_file, output_file, delimiter=";"):
    df = pd.read_csv(input_file, encoding="ISO-8859-1", delimiter=delimiter)
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
        "nombre": "casos_positivos_covid19.csv",
        "delimiter": ","
    },
    {
        "nombre": "donaciones_covid19.csv",
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
]

# for filename in glob.glob("*.csv"):
for filename in files:
    input_file = "./{}".format(filename["nombre"])
    output_file = "{}{}".format(output_dir, filename["nombre"])
    delimiter = filename["delimiter"]

    try:
        formatear_datos(input_file, output_file, delimiter)
        print("Se limpio correctamente los datos de {} y se envio a {}".format(input_file, output_file))
    except Exception as e:
        print("Error limpiando datos en archivo: {}.".format(input_file))
