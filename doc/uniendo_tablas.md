# Uniendo tablas usando Python/Pandas

```python
casos = pd.read_csv('bonos_covid19.csv', encoding = "ISO-8859-1", delimiter = ';')
ubigeo = pd.read_csv('ubigeos.csv', encoding = "ISO-8859-1", delimiter = ';', na_values=['    NA'])
ubigeo = ubigeo[ubigeo['cod_ubigeo_inei'].notna()]
ubigeo['cod_ubigeo_inei'] = pd.to_numeric(ubigeo['cod_ubigeo_inei'])
resultado =  pd.merge(casos, ubigeo, how='inner', left_on='UBIGEO', right_on='cod_ubigeo_inei')
resultado
```
