Los notebooks disponibles son:

###Análisis exploratorio

Notebook donde se explora la data existente para mostrar el estado actual así como 
encontrar algunos insights que nos permitan proceder a realizar un modelo predictivo.  

URL: 
https://colab.research.google.com/drive/1avx-BHdYGCyAs7SrJYxmIqHCGx_k9BIR?usp=sharing

###Subir notebook a colab

Para automatizar la subida del notebook y de la data asociada tenemos el script upload_notebook.py 
y el script de configuración upload_config.py. Los pasos para ejecutarlo son:

1. Cambiar el nombre del script upload_config.example.py a upload_config.py.
2. Colocar el id del folder de colab donde se sube el notebook y los csv.
3. Ejecutar 'python upload_notebook.py'