#!/usr/bin/env python
# coding: utf-8

# # Hackaton : gobierno de datos abiertos - corona

# ## colaborador: J Caparo

# ## Convierte el encoding de archivos *.csv a "utf-8" automaticamente.

# In[1]:


import os    
import chardet
import pandas as pd
import numpy as np


# read the csv files

# In[2]:


# get file encoding type
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return chardet.detect(rawdata)['encoding']


# In[3]:


# change file encoding function
def change_file_encoding(filename):
    srcfile=filename
    prefix='fixed'
    trgfile=prefix +srcfile
    from_codec = get_encoding_type(srcfile)
    print("Archivo :",filename, "Encoding:", from_codec)
    if from_codec != 'utf-8':
        try: 
            print("Convirtiendo a utf-8")
            with open(srcfile, 'r', encoding=from_codec) as f, open(trgfile, 'w', encoding='utf-8') as e:
                text = f.read() # for small files, for big use chunks
                e.write(text)

            os.remove(srcfile) # remove old encoding file
            os.rename(trgfile, srcfile) # rename new encoding
        except UnicodeDecodeError:
            print('Decode Error')
        except UnicodeEncodeError:
            print('Encode Error')
    else:
        print('encoding is already utf-8. No cambio')
    return


# In[4]:


from os import listdir

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


# In[5]:


filenames = find_csv_filenames("./")
for name in filenames:
  print ("Trabajando con archivo:",name)
  change_file_encoding(name)
print("Terminado")

