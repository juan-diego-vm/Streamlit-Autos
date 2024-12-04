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

# Estado para mostrar el formulario
if "show_form" not in st.session_state:
    st.session_state.show_form = False

# Botón para mostrar el formulario de agregar vehículos
if st.button("➕ Agregar vehículo"):
    st.session_state.show_form = True

# Mostrar el formulario si el botón fue presionado
if st.session_state.show_form:
    with st.form("Agregar vehículo"):
        nueva_placa = st.text_input("Placa")
        nuevo_modelo = st.text_input("Modelo")
        nuevo_anio = st.number_input("Año", min_value=1900, max_value=datetime.now().year, step=1, value=2022)
        nuevo_dueno = st.text_input("Dueño Actual")
        # nuevo_reporte = st.text_input("Reporte")
        # nueva_calificacion = st.slider("Calificación", min_value=0.0, max_value=10.0, step=0.1)
        
        # Botón para guardar los datos
        guardar = st.form_submit_button("Guardar")

        if guardar:
            # Agregar los nuevos datos al DataFrame
            nueva_fecha = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            nuevo_dato = [nueva_placa, nuevo_modelo, nuevo_anio, nuevo_dueno, nueva_fecha, 'En proceso...', 'En proceso...']
            df.loc[len(df)] = nuevo_dato
            st.success("Vehículo agregado exitosamente.")
            st.session_state.show_form = False

# Función para aplicar colores según la calificación
def highlight_calification(val):
    if val <= 5:
        return "background-color: red; color: white;"
    elif 5 < val <= 7:
        return "background-color: yellow; color: black;"
    elif val > 7:
        return "background-color: green; color: white;"
    return ""

# Aplicar estilos condicionales solo a la columna "Calificación"
styled_df = df.style.applymap(highlight_calification, subset=["Calificación"])

# Mostrar la tabla con estilos
st.write("### Lista de Vehículos")
st.dataframe(df, use_container_width=True)
st.write(styled_df.to_html(), unsafe_allow_html=True)
