import sys

import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file, delimiter=';', encoding="ISO-8859-1")
df.to_csv(output_file, encoding="UTF-8", index=False)
