import pandas as pd

url = "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FArellanoMCarlos%2FEnlace_GitHub%2Frefs%2Fheads%2Fmain%2FData.xlsx&wdOrigin=BROWSELINK"

try:
    df = pd.read_csv(url)
    print("Datos cargados exitosamente en DataFrame de pandas:")

    print(df.head()) 
except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")