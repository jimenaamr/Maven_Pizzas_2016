import pandas as pd

df_detalle_pedidos = pd.read_csv('order_details.csv',sep = ";", encoding = "LATIN_1")
df_pedidos = pd.read_csv('orders.csv',sep = ";", encoding = "LATIN_1")
df_tipos_pizza = pd.read_csv('pizza_types.csv', sep = ",", encoding = "LATIN_1")
df_pizza = pd.read_csv('pizzas.csv', sep = ",", encoding = "LATIN_1")



def limpiar_datos():
    global df_detalle_pedidos
    df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('one','1')
    df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('One','1')
    df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('two','2')
    df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('Two','2')

    
    df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('-','_')
    df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('@','a')
    df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('3','e')
    df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('0','o')
    df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace(' ','_')

    df_detalle_pedidos['quantity'].fillna(1, inplace = True)
    df_detalle_pedidos = df_detalle_pedidos[df_detalle_pedidos['pizza_id'].notna()] 

    for i in range(len(df_pedidos)):
        try: 
            y = pd.to_datetime(float(df_pedidos['date'][i])+3600, unit='s')
        except:
            y = pd.to_datetime(df_pedidos['date'][i])
        df_pedidos['date'][i] = y
    
    lista_cantidades_validas = list(df_detalle_pedidos['quantity'])
    lista_pedidos_validos = list(df_detalle_pedidos['pizza_id'])
    lista_pizzas_validas = []
    lista_tamaños_validos = []

    for pedido in lista_pedidos_validos:
        if pedido[-2:] == '_s' or pedido[-2:] == '_m' or pedido[-2:] == '_l':
            lista_pizzas_validas.append(pedido[:-2])
            lista_tamaños_validos.append(pedido[-1])
        elif pedido[-3:] == '_xl':
            lista_pizzas_validas.append(pedido[:-3])
            lista_tamaños_validos.append(pedido[-2:])
        elif pedido[-4:] == '_xxl':
            lista_pizzas_validas.append(pedido[:-4])
            lista_tamaños_validos.append(pedido[-3:])

    for i in range(len(lista_cantidades_validas)):
        lista_cantidades_validas[i] = int(lista_cantidades_validas[i])
        if lista_cantidades_validas[i] < 0:
            lista_cantidades_validas[i] *= -1

    return lista_pizzas_validas, lista_tamaños_validos, lista_cantidades_validas


def dic_pizza_ingredientes():
    dic_ingredientes = {}
    lista_pizzas = list(df_tipos_pizza['pizza_type_id'])
    lista_ingredientes = list(df_tipos_pizza['ingredients'])

    for i in range(len(lista_pizzas)):
        lista_ingredientes_espacios = lista_ingredientes[i].split(',')
        for j in range(len(lista_ingredientes_espacios)):
            lista_ingredientes_espacios[j] = lista_ingredientes_espacios[j].strip()
        dic_ingredientes[lista_pizzas[i]] = lista_ingredientes_espacios
    return dic_ingredientes


def ingredientes_distintos():
    lista_ingredientes = list(df_tipos_pizza['ingredients'])
    str_ingredientes = ','.join(lista_ingredientes)
    lista_ingredientes_espacios = str_ingredientes.split(',')
    for i in range(len(lista_ingredientes_espacios)):
        lista_ingredientes_espacios[i] = lista_ingredientes_espacios[i].strip()
    lista_ingredientes_juntos = lista_ingredientes_espacios
    ingredientes_unicos = []

    for ingrediente in lista_ingredientes_juntos:
        if ingrediente not in ingredientes_unicos:
            ingredientes_unicos.append(ingrediente)

    dic_ingredientes_unicos = {}
    for i in range(len(ingredientes_unicos)):
        dic_ingredientes_unicos[ingredientes_unicos[i]] = 0
    
    return dic_ingredientes_unicos


def ingredientes_usados(lista_pizzas_pedidas,lista_tamaños,lista_cantidades):
    tamaños = {'s':1,'m':2,'l':3,'xl':4,'xxl':5}
    dic_ingredientes_distintos = ingredientes_distintos()
    dicc_pizza_ingredientes = dic_pizza_ingredientes()

    for i in range(len(lista_pizzas_pedidas)):
        añadir = tamaños[lista_tamaños[i]]*lista_cantidades[i]
        listas_ingredientes_por_pizza = dicc_pizza_ingredientes[lista_pizzas_pedidas[i]]

        for j in range(len(listas_ingredientes_por_pizza)):
            indice = listas_ingredientes_por_pizza[j]
            dic_ingredientes_distintos[indice] += añadir

    return dic_ingredientes_distintos

    
def prediccion():
    datos_listas = limpiar_datos()

    pred = ingredientes_usados(datos_listas[0], datos_listas[1], datos_listas[2])
    claves = list(pred.keys())

    for i in range(len(pred)):
        div = pred[claves[i]]//52
        pred[claves[i]] = div

    return pred


def convertir_dataframe(pred):
    df = pd.DataFrame([[key, pred[key]] for key in pred.keys()], columns=['Ingrediente', 'Cantidad a comprar'])
    return df


def extract():
    df_diccionario_datos = pd.read_csv('data_dictionary.csv',sep = ",", encoding = "LATIN_1")
    df_detalle_pedidos = pd.read_csv('order_details.csv',sep = ",", encoding = "LATIN_1")
    df_pedidos = pd.read_csv('orders.csv',sep = ",", encoding = "LATIN_1")
    df_tipos_pizza = pd.read_csv('pizza_types.csv', sep = ",", encoding = "LATIN_1")
    df_pizza = pd.read_csv('pizzas.csv', sep = ",", encoding = "LATIN_1")
    return df_diccionario_datos, df_detalle_pedidos, df_pedidos, df_tipos_pizza, df_pizza

def transform():
    datos_transformados = prediccion()
    return datos_transformados

def load():
    df = convertir_dataframe(transform())
    df.to_csv('prediccion_ingredientes16.csv')

load()