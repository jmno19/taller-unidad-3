import pandas as pd

df = pd.read_excel('data1.xlsx', sheet_name='Data')

print("Columnas originales del archivo:")
print(list(df.columns))

df_filtrado = df.drop(columns=['City', 'Country'], errors='ignore')

print("\nColumnas después de anular 'City' y 'Country':")
print(list(df_filtrado.columns))

print(f"\nTotal de registros procesados: {len(df_filtrado)}")