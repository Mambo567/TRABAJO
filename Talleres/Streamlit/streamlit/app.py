import pandas as pd
# import matplotlib.pyplot as plt 
import streamlit as st
# from functions import home, map, charts

# Funciones 

def home(df):
    st.image("lobez.png", 
        caption="CARGATRON", width=400)
    
    with st.expander("Description:"):
        st.write("This is an app to visualise charging points.")
        st.dataframe(df)

def map(df,zoom=11):
    st.header("Mapa cargadores madrid")
    st.map(df, latitude="latidtud", longitude="longitud",zoom=zoom)

def charts(df): 

    left, right = st.columns(2)

    with left:
                                     
        df_group_carg = df.groupby("DISTRITO")["Nº CARGADORES"].sum().reset_index()
        st.header("Cargadores por distrito")
        st.bar_chart(data = df_group_carg, 
                    x="DISTRITO", y="Nº CARGADORES")
    with right:
        st.header("Cargadores por Operador")
        df_group_oper = df.groupby("OPERADOR")[["Nº CARGADORES"]].sum().reset_index()
        st.bar_chart(data = df_group_oper, 
                    x="OPERADOR", y="Nº CARGADORES",)


# LO DE FUERA

st.set_page_config(
    page_title="Cargatron",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",
)



# A PARTIR DE AQUI LAS PAGINAS 
option = st.sidebar.selectbox(
    "Page:",
    ("Home", "Map", "Charts"),
)


st.header(f"My Streamlit APP - CARGATRON")


df = pd.read_csv("data/red_recarga_acceso_publico_2021.csv", sep=";")

uploaded_file = st.sidebar.file_uploader("Choose a file (must be ';' separated)", 
                                 type=["csv"]

                                 )
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, sep=";")
        st.balloons()
    except:
        st.write("File format not recognized.")

# Creación de columnas con tamaños distintos
left, right = st.columns([3, 2])

# Filtro de Distrito

mostrar_filtro_D = st.sidebar.checkbox("Utilizar filtro de Distrito")
if mostrar_filtro_D:
    filtro_D = st.sidebar.multiselect(
    "Distrito:",
    df.DISTRITO.unique().tolist(),
    df.DISTRITO.unique().tolist(),
)
    zoom = 13
else:
    filtro_D = df.DISTRITO.unique().tolist()
    zoom = 11
    with right: 
        st.dataframe(df.groupby("DISTRITO")["Nº CARGADORES"].sum().reset_index())




# Filtro de n de estaciones
cargadores = df.loc[:,"Nº CARGADORES"].unique()
minimo_c = cargadores.min()
maximo_c = cargadores.max()
n_estaciones = list(range(minimo_c,maximo_c+1))

mostrar_filtro_c = st.sidebar.checkbox("Utilizar filtro de N de Estaciones")
if mostrar_filtro_c:
    minimo_n, maximo_n = st.sidebar.select_slider(
    "Select a range of color wavelength",
    options= n_estaciones,
    value=(1, 4),
  )
else:
    minimo_n = minimo_c
    maximo_n = maximo_c

# Filtro de Operadores
mostrar_filtro_O = st.sidebar.checkbox("Utilizar filtro de Operador")
if mostrar_filtro_O:
    filtro_O = st.sidebar.multiselect(
    "Operador:",
    df.OPERADOR.unique().tolist(),
    df.OPERADOR.unique().tolist(),
)
else:
    filtro_O = df.OPERADOR.unique().tolist()
    with right:
        st.dataframe(df.groupby("OPERADOR")["Nº CARGADORES"].sum().reset_index())

df = df.loc[(df["DISTRITO"].isin(filtro_D)) & ((df["Nº CARGADORES"] >= minimo_n) & (df["Nº CARGADORES"] <= maximo_n)),:]

# Advertencia

if df.size == 0:
  st.warning('No hay registros que cumplan con esas condiciones')
  st.stop()
# st.success("Gracias por seleccionar elementos válidos :)")



# filtro_D = st.sidebar.selectbox(
#     "Distrito:",
#     df.DISTRITO.unique().tolist(),
    
# )

# if filtro_D == "ALL":
#     pass
# else:
#     df = df.loc[ df["DISTRITO"].isin([filtro_D])    ,  :]





# st.write("You selected:", option)
if option == "Home":
    home(df)
elif option=="Map":
    with left:
        map(df,zoom=zoom)
else: 
    charts(df)

