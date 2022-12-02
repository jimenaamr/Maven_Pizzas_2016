import pandas as pd

df_detalle_pedidos = pd.read_csv('order_details.csv',sep = ";", encoding = "LATIN_1")

tipos_detalle_pedidos = df_detalle_pedidos.dtypes
print(f'El tipo de datos de cada columna en el order_details.csv es:\n{tipos_detalle_pedidos}')
print('\n')
nans_detalle_pedidos = df_detalle_pedidos.isna().sum()
print(f'El número de NaN por cada columna en el order_details.csv es:\n{nans_detalle_pedidos}')
print('\n')
nulls_detalle_pedidos = df_detalle_pedidos.isnull().sum()
print(f'El número de Null por cada columna en el order_details.csv es:\n{nulls_detalle_pedidos}')
print('\n')

df_pedidos = pd.read_csv('orders.csv',sep = ";", encoding = "LATIN_1")

tipos_pedidos = df_pedidos.dtypes
print(f'El tipo de datos de cada columna en el orders.csv es:\n{tipos_pedidos}')
print('\n')
nans_pedidos = df_pedidos.isna().sum()
print(f'El número de NaN por cada columna en el orders.csv es:\n{nans_pedidos}')
print('\n')
nulls_pedidos = df_pedidos.isnull().sum()
print(f'El número de Null por cada columna en el orders.csv es:\n{nulls_pedidos}')
print('\n')