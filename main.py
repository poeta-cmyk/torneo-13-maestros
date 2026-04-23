import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gala de los 13", layout="wide")

if 'db_resultados' not in st.session_state:
    st.session_state.db_resultados = pd.DataFrame(columns=['Ronda', 'Mesa', 'J_A1', 'J_A2', 'Pts_A', 'J_B1', 'J_B2', 'Pts_B'])

st.title("🏆 Gala de los 13: Sistema de Arbitraje")

st.sidebar.header("Nombres de los Maestros")
nombres = {f"j{i}": st.sidebar.text_input(f"Maestro {i}", f"Jugador {i}") for i in range(1, 14)}

menu = st.tabs(["🎮 Carga de Rondas", "📊 Tabla de Posiciones"])

def obtener_ronda(r):
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
    return rondas.get(r)

with menu[0]:
    r_sel = st.select_slider("Ronda", options=list(range(1, 14)))
    d = obtener_ronda(r_sel)
    st.info(f"Descansa: {nombres[d['desc']]}")
    def mesa_ui(i, lj):
        st.write(f"### MESA {i}")
        c1, c2 = st.columns(2)
        with c1:
            st.write(f"🔵 {nombres[lj[0]]} & {nombres[lj[1]]}")
            pa = st.number_input(f"Pts A - M{i}", 0, 200, key=f"a{r_sel}{i}")
        with c2:
            st.write(f"🔴 {nombres[lj[2]]} & {nombres[lj[3]]}")
            pb = st.number_input(f"Pts B - M{i}", 0, 200, key=f"b{r_sel}{i}")
        return [r_sel, i, lj[0], lj[1], pa, lj[2], lj[3], pb]
    res = [mesa_ui(1, d["m1"]), mesa_ui(2, d["m2"]), mesa_ui(3, d["m3"])]
    if st.button("💾 GUARDAR RESULTADOS"):
        df_n = pd.DataFrame(res, columns=['Ronda', 'Mesa', 'J_A1', 'J_A2', 'Pts_A', 'J_B1', 'J_B2', 'Pts_B'])
        st.session_state.db_resultados = pd.concat([st.session_state.db_resultados, df_n]).drop_duplicates(subset=['Ronda', 'Mesa'], keep='last')
        st.success("¡Resultados guardados!")

with menu[1]:
    df = st.session_state.db_resultados
    if not df.empty:
        st.header("Tabla de Posiciones (JG > DIF > PRO)")
        s = []
        for c, n in nombres.items():
            pa = df[(df['J_A1'] == c) | (df['J_A2'] == c)]
            pb = df[(df['J_B1'] == c) | (df['J_B2'] == c)]
            jj = len(pa) + len(pb)
            jg = len(pa[pa['Pts_A'] > pa['Pts_B']]) + len(pb[pb['Pts_B'] > pb['Pts_A']])
            pf = pa['Pts_A'].sum() + pb['Pts_B'].sum()
            pc = pa['Pts_B'].sum() + pb['Pts_A'].sum()
            s.append([n, jj, jg, jj-jg, pf, pc, pf-pc, round(pf/jj, 2) if jj>0 else 0])
        t = pd.DataFrame(s, columns=['Maestro', 'JJ', 'JG', 'JP', 'PF', 'PC', 'DIF', 'PRO'])
        st.table(t.sort_values(by=['JG', 'DIF', 'PRO'], ascending=False).reset_index(drop=True))
