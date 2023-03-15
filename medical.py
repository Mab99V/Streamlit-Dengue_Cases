import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


# Configuración de la página
st.set_page_config(
    page_title="Proyecto con Streamlit y Plotly",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# Título
st.title("Buscador de información")
st.sidebar.write("Mabel Perez Garibay - S18003216 - zs18003216@estudiantes.uv.mx")

st.sidebar.image("descarga.jpeg")
st.markdown("##")

# Carga de datos
DATA_URL = ('denguecases.csv')

import codecs

@st.cache
# Función para mostrar la tabla
def load_data(nrows):
    doc = codecs.open('denguecases.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data = load_data(1000)

#Filtrar
def filter_data_by_medi(selected_medi):
    filtered_data = data[data['Month'].isin(selected_medi)]
    return filtered_data

def filter_data_by_medic(search_term):
    # search for matches in any column containing the search term
    matches = data[data.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
    return matches



selected_medi = st.sidebar.multiselect("Selecciona el mes", data['Month'].unique())


if not selected_medi:
    st.write("Mostrando la tabla completa")
    st.subheader = ('Todos')
    st.write(data)
else:
    # Filtrar los datos
    filtered_data = filter_data_by_medi(selected_medi)
    
    # Mostrar la tabla filtrada
    st.write("Mostrando los datos filtrados")
    st.write(filtered_data)


# Texto para buscar información
datos = st.sidebar.text_input('Ingresar dato :')
btnBuscar = st.sidebar.button('Buscar')

if (btnBuscar):
   data_medi= filter_data_by_medic(datos.upper())
   count_row = data_medi.shape[0]  # Gives number of rows
   st.write(f"Total de casos : {count_row}")
   st.write(data_medi)

#Histograma
def create_histogram(data, feature):
    fig = px.histogram(data, x=feature, nbins=30)
    return fig

st.subheader = ('Histograma')
feature = st.selectbox("Selecciona la caracteristica para crear el histograma", [ "Dengue_Cases"])
histogram = create_histogram(data, feature)
st.plotly_chart(histogram)

st.markdown("Descripcion: Se muestra la informacion de cuantos casos de dengue hubo por año")

# Función para crear una gráfica de barras
def create_bar_chart(data, x_feature, y_feature):
    fig = px.bar(data, x=x_feature, y=y_feature, color="Month")
    return fig

st.subheader = ('Gráfica de barras')
x_feature = st.sidebar.selectbox("Selecciona una característica para el eje X", ["Month"])
y_feature = st.sidebar.selectbox("Selecciona una característica para el eje Y", ["Dengue_Cases"])
bar_chart = create_bar_chart(data, x_feature, y_feature)
st.plotly_chart(bar_chart)

st.markdown("Descripcion: Se muestra la informacion de cuantos casos hubo por mes")



# Función para crear una gráfica de dispersión
def create_scatter_plot(data, x_feature, y_feature):
    fig = px.scatter(data, x=x_feature, y=y_feature, color="Month")
    return fig

st.subheader = ('Gráfica de dispersión')
ye_feature = st.selectbox("Selecciona una característica para el eje X", ["Year"])
d_feature = st.selectbox("Selecciona una característica para el eje Y", ["Dengue_Cases"], key="dengue_cases")

scatter_plot = create_scatter_plot(data, ye_feature, d_feature)
st.plotly_chart(scatter_plot)

st.markdown("Descripcion: Se muestra la informacion de cuantos casos hubo por mes y año")