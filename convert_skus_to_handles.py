import pandas as pd

# CONFIGURACIÓN
INPUT_FILE = 'magexport_simples.csv'   # << Cambia aquí el nombre si tu archivo tiene otro nombre
OUTPUT_FILE = 'magexport_simples_actualizado.csv'

# Cargar el archivo CSV
print(f"Cargando archivo: {INPUT_FILE}")
df = pd.read_csv(INPUT_FILE)

# Crear el diccionario de SKU a URL Key
sku_to_url = dict(zip(df['SKU <sku>'], df['URL Key <url_key> (admin)']))

# Función para convertir lista de SKUs en lista de handles
def convert_skus_to_handles(sku_list):
    if pd.isna(sku_list):
        return ''
    delimiters = ';' if ';' in sku_list else ','
    skus = [sku.strip() for sku in sku_list.split(delimiters)]
    handles = [sku_to_url.get(sku, '') for sku in skus]
    return ','.join(handles)

# Aplicar la conversión
df['Productos relacionados (handles)'] = df['Productos relacionados <relation>'].apply(convert_skus_to_handles)
df['Venta por arriba (handles)'] = df['Venta por arriba <up_sell>'].apply(convert_skus_to_handles)

# Seleccionar columnas importantes
columns_to_export = [
    'SKU <sku>',
    'Name <name> (admin)',
    'Productos relacionados <relation>',
    'Productos relacionados (handles)',
    'Venta por arriba <up_sell>',
    'Venta por arriba (handles)'
]

df_export = df[columns_to_export]

# Guardar el CSV actualizado
df_export.to_csv(OUTPUT_FILE, index=False)
print(f"Archivo guardado como: {OUTPUT_FILE}")
