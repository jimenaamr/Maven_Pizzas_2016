# INFORME DE CALIDAD Y PREDICCIÓN

En este repositorio se encuentran los archivos necesarios para hacer una predicción sobre los ingredientes que una pizzería deberá comprar semanalmente en función de los datos de dicho negocio de 2016.

## Archivos Adjuntados

- order_details.csv: Detalles sobre los pedidos que se han realizado a lo largo del año. En él encontramos el identificador del pedido, el identificador de la pizza pedida y la cantidad pedida. Deberemos limpiar los datos, ya que no están en el formato correcto.

- orders.csv: Detalles sobre los pedidos que se han realizado a lo largo del año. En él encontramos el identificador del pedido, la fecha en la que se realizó y la hora. Deberemos limpiar los datos, ya que no están en el formato correcto.

- pizza_types.csv: Detalles sobre las pizzas disponibles en la pizzaría. En él encontramos el identificador del tipo de pizza, su nombre completo, la categoría en la que está y los ingredientes necesarios para prepararla.

- pizzas.csv: Detalles sobre las pizzas disponibles en la pizzaría. En él encontramos el identificador del tipo de pizza, su tipo, su tamaño y su precio.

- prediccion_ingredientes16.csv: Dataframe creado tras ejecutar el archivo codigo_prediccion.py. Te ofrece una predicción de los ingredientes que la pizzería debería comprar semanalmente en función de los datos de 2016 analizados.

- requirements.txt: En este archivo encontramos las librerías que se necesitan instalar para poder ejecutar los archivos.

- codigo_prediccion16.py: En este archivo encontramos el código necesario para crear el csv prediccion_ingredientes.csv con la predicción de los ingredientes a comprar semanalmente. Además, este mismo código limpiará los datos de order_details.csv y orders.csv.

- informe_calidad16.py: Código neceario para hacer un informe de calidad sobre los datos encontrados en order_details.csv, orders.csv.

## Modo de Ejecución

1- Instalar el requirements.txt

2- Ejecutar el archivo informe_calidad16.py para realizar el informe de calidad de los datos de cada uno de los csv. La salida mostrará el tipo de datos y la cantidad de NaN y de Null que encontramos.

3- Ejecutar el archivo codigo_prediccion16.py para limpiar los datos de los csv que no son válidos y crear el csv prediccion_ingredientes16.csv con la predicción de ingredientes que deberá comprar la pizzería semanalmente en función de los datos de 2016.