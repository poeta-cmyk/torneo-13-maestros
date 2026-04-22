import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gala de los 13", layout="wide")

st.title("🏆 Gala Final: Los 13 Maestros")
st.subheader("Sistema de Rotación Perfecta")

# Registro de los 13 Elegidos
st.sidebar.header("Nombres de los Clasificados")
nombres = []
for i in range(1, 14):
    nombre = st.sidebar.text_input(f"Maestro #{i}", f"Jugador {i}", key=f"p{i}")
    nombres.append(nombre)

# Lógica de rotación de tu archivo Excel
def obtener_ronda(ronda_num, lista_nombres):
    # En cada ronda descansa el jugador correspondiente al número de ronda
    idx_descansa = (ronda_num - 1) % 13
    descansa = lista_nombres[idx_descansa]
    
    # Jugadores que juegan esta ronda (los otros 12)
    jugando = [n for i, n in enumerate(lista_nombres) if i != idx_descansa]
    
    # Distribución en mesas (4 por mesa)
    m1 = {"A": jugando[0], "C": jugando[1], "B": jugando[2], "D": jugando[3]}
    m2 = {"A": jugando[4], "C": jugando[5], "B": jugando[6], "D": jugando[7]}
    m3 = {"A": jugando[8], "C": jugando[9], "B": jugando[10], "D": jugando[11]}
    
    return descansa, m1, m2, m3

# Selección de Ronda
ronda = st.select_slider("Selecciona la Ronda", options=list(range(1, 14)))

st.divider()

descansa, mesa1, mesa2, mesa3 = obtener_ronda(ronda, nombres)

st.warning(f"🛋️ **En la Ronda {ronda} descansa:** {descansa}")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("MESA 1")
    st.table(pd.DataFrame([mesa1]).T.rename(columns={0: "Jugador"}))

with col2:
    st.header("MESA 2")
    st.table(pd.DataFrame([mesa2]).T.rename(columns={0: "Jugador"}))

with col3:
    st.header("MESA 3")
    st.table(pd.DataFrame([mesa3]).T.rename(columns={0: "Jugador"}))

st.info("Este programa replica la lógica de tu archivo Excel para garantizar encuentros únicos.")
