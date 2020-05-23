#!/usr/bin/env python
# coding: utf-8

# # Hackaton : gobierno de datos abiertos - corona

# ## colaborador: J Caparo

# ## Convierte el encoding de archivos *.csv a "utf-8" automaticamente.

# In[1]:


import os    
import chardet
import shutil
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
def change_file_encoding(filename,encoded_dir):
    srcfile=filename
    prefix='fixed'
    trgfile=prefix + srcfile
    new_dir= encoded_dir
    from_codec = get_encoding_type(srcfile)
    print("Archivo :",filename, "Encoding:", from_codec)
    if from_codec != 'utf-8':
        try: 
            print("Convirtiendo a utf-8 y copiando al directorio data_limpia")
            with open(srcfile, 'r', encoding=from_codec) as f, open(trgfile, 'w', encoding='utf-8') as e:
                text = f.read() # for small files, for big use chunks
                e.write(text)
                
            shutil.copy2(trgfile, encoded_dir)
            os.chdir(new_dir)
            os.rename(trgfile, srcfile)
#            os.remove(srcfile) # remove old encoding file
#            os.rename(trgfile, srcfile) # rename new encoding
        except UnicodeDecodeError:
            print('Decode Error')
        except UnicodeEncodeError:
            print('Encode Error')
    else:
        print('encoding is already utf-8. No cambio. Se  copio al directorio data_limpia')
        shutil.copy2(srcfile, encoded_dir)
    
    return


# In[4]:


from os import listdir

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


# In[5]:


base_dir = "./"
encoded_dir = "./data_limpia"
filenames = find_csv_filenames(base_dir)
for name in filenames:
  print ("Trabajando con archivo:",name)
  change_file_encoding(name,encoded_dir)
print("Terminado")

