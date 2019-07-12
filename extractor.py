import pandas as pd

def extract_csv(csv_name):
    """
    Al final no voy a usar esta función. Necesito usar la siguiente con json.
    """
    df = pd.read_csv(csv_name, header=0, encoding = 'utf8')
    return df

def extract_json(json_name):
    """
    Esta función me permite recuperar el tipo de la columna de las canciones que
    tenía el dataframe después del scraping, es decir, una lista de strings, donde cada string es un verso.
    Si lo hiciera con CSV, la letra de la canción pasaría a ser una lista con una única string, por lo que
    perdería la separación entre versos.
    """
    df = pd.read_json(json_name, encoding = 'utf8')
    return df

