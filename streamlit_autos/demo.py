import streamlit as st
import pandas as pd
from datetime import datetime

# Título de la app
st.title("Gestión de Vehículos")

# Columnas de la tabla
columns = ["Placa", "Modelo", "Año", "Dueño Actual", "Fecha de Creación", "Reporte", "Calificación"]

# Datos iniciales con fecha y hora actuales
data = [
    ["ABC123", "Toyota Corolla", 2015, "Juan Pérez", datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "Sin reporte", 4.5],
    ["DEF456", "Honda Civic", 2018, "María López", datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "Sin reporte", 4.8],
    ["GHI789", "Ford Focus", 2020, "Carlos Gómez", datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "Accidente leve", 3.9],
]

# Crear un DataFrame con los datos
df = pd.DataFrame(data, columns=columns)

# Mostrar la tabla
st.write("### Lista de Vehículos")
st.dataframe(df)

# Botón para agregar vehículos
col1, col2 = st.columns([3, 1])
with col1:
    pass  # Espacio para el título
with col2:
    if st.button("Agregar vehículo"):
        new_data = [
            "XXX000", 
            "Modelo X", 
            2022, 
            "Nuevo Dueño", 
            datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
            "Sin reporte", 
            5.0
        ]
        df.loc[len(df)] = new_data
        st.success("Vehículo agregado exitosamente.")

# Mostrar la tabla actualizada en Streamlit
# st.dataframe(df)
