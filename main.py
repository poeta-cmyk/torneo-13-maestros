import streamlit as st

st.set_page_config(page_title="Gala de los 13", layout="wide")

st.title("🏆 Gala Final: Los 13 Maestros")
st.subheader("Sistema de Rotación Oficial (Matriz Excel)")

# Registro de Nombres en la barra lateral
st.sidebar.header("Nombres de los Clasificados")
nombres = {}
for i in range(1, 14):
    nombres[f"j{i}"] = st.sidebar.text_input(f"Maestro {i}", f"Jugador {i}")

# MATRIZ EXACTA DE TU EXCEL
def obtener_ronda_oficial(r_num):
    rondas = {
        1:  {"desc": "j13", "m1": ["j1", "j12", "j8", "j5"], "m2": ["j2", "j11", "j3", "j10"], "m3": ["j4", "j9", "j6", "j7"]},
        2:  {"desc": "j1",  "m1": ["j2", "j13", "j9", "j6"], "m2": ["j3", "j12", "j4", "j11"], "m3": ["j5", "j10", "j7", "j8"]},
        3:  {"desc": "j2",  "m1": ["j3", "j1", "j10", "j7"], "m2": ["j4", "j13", "j5", "j12"], "m3": ["j6", "j11", "j8", "j9"]},
        4:  {"desc": "j3",  "m1": ["j4", "j2", "j11", "j8"], "m2": ["j5", "j1", "j6", "j13"], "m3": ["j7", "j12", "j9", "j10"]},
        5:  {"desc": "j4",  "m1": ["j5", "j3", "j12", "j9"], "m2": ["j6", "j2", "j7", "j1"], "m3": ["j8", "j13", "j10", "j11"]},
        6:  {"desc": "j5",  "m1": ["j6", "j4", "j13", "j10"], "m2": ["j7", "j3", "j8", "j2"], "m3": ["j9", "j1", "j11", "j12"]},
        7:  {"desc": "j6",  "m1": ["j7", "j5", "j1", "j11"], "m2": ["j8", "j4", "j9", "j3"], "m3": ["j10", "j2", "j12", "j13"]},
        8:  {"desc": "j7",  "m1": ["j8", "j6", "j2", "j12"], "m2": ["j9", "j5", "j10", "j4"], "m3": ["j11", "j3", "j13", "j1"]},
        9:  {"desc": "j8",  "m1": ["j9", "j7", "j3", "j13"], "m2": ["j10", "j6", "j11", "j5"], "m3": ["j12", "j4", "j1", "j2"]},
        10: {"desc": "j9",  "m1": ["j10", "j8", "j4", "j1"], "m2": ["j11", "j7", "j12", "j6"], "m3": ["j13", "j5", "j2", "j3"]},
        11: {"desc": "j10", "m1": ["j11", "j9", "j5", "j2"], "m2": ["j12", "j8", "j13", "j7"], "m3": ["j1", "j6", "j3", "j4"]},
        12: {"desc": "j11", "m1": ["j12", "j10", "j6", "j3"], "m2": ["j13", "j9", "j1", "j8"], "m3": ["j2", "j7", "j4", "j5"]},
        13: {"desc": "j12", "m1": ["j13", "j11", "j7", "j4"], "m2": ["j1", "j10", "j2", "j9"], "m3": ["j3", "j8", "j5", "j6"]},
    }
    return rondas.get(r_num)

ronda_sel = st.select_slider("Selecciona la Ronda", options=list(range(1, 14)))
datos = obtener_ronda_oficial(ronda_sel)

st.info(f"🛋️ **En la Ronda {ronda_sel} descansa:** {nombres[datos['desc']]}")

def mostrar_mesa(titulo, lista_j):
    st.markdown(f"### {titulo}")
    st.write(f"**Pareja A:** {nombres[lista_j[0]]} y {nombres[lista_j[1]]}")
    st.write(f"**vs**")
    st.write(f"**Pareja B:** {nombres[lista_j[2]]} y {nombres[lista_j[3]]}")

col1, col2, col3 = st.columns(3)
with col1: mostrar_mesa("MESA 1", datos["m1"])
with col2: mostrar_mesa("MESA 2", datos["m2"])
with col3: mostrar_mesa("MESA 3", datos["m3"])
