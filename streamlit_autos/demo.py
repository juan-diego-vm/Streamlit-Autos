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
    ["DEF456", "Honda Civic", 2018, "María López", datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "Sin reporte", 7.0],
    ["GHI789", "Ford Focus", 2020, "Carlos Gómez", datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "Accidente leve", 9.0],
]

# Crear un DataFrame con los datos
df = pd.DataFrame(data, columns=columns)

# Función para aplicar colores según la calificación
def highlight_calification(val):
    if val <= 5:
        return "background-color: red; color: white;"
    elif 5 < val <= 7:
        return "background-color: yellow; color: black;"
    elif val > 7:
        return "background-color: green; color: white;"
    return ""

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
            6.5  # Calificación de ejemplo
        ]
        df.loc[len(df)] = new_data
        st.success("Vehículo agregado exitosamente.")

# Aplicar estilos condicionales solo a la columna "Calificación"
styled_df = df.style.applymap(highlight_calification, subset=["Calificación"])

# Mostrar la tabla con estilos
st.write("### Lista de Vehículos")
st.dataframe(df, use_container_width=True)
st.write(styled_df.to_html(), unsafe_allow_html=True)
