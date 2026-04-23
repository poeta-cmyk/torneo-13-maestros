# Esta función busca si ya existen puntos guardados para esa mesa y ronda
    def obtener_valor(r, m, equipo):
        busqueda = df[(df['Ronda'] == r) & (df['Mesa'] == m)]
        if not busqueda.empty:
            return int(busqueda.iloc[0][f'Pts_{equipo}'])
        return 0

    def ui_mesa(i, lj):
        st.markdown(f"### MESA {i}")
        c1, c2 = st.columns(2)
        # Aquí el sistema "recuerda" lo anotado anteriormente
        val_a = obtener_valor(r_sel, i, 'A')
        val_b = obtener_valor(r_sel, i, 'B')
        
        with c1:
            st.write(f"🔵 {nombres[lj[0]]} & {nombres[lj[1]]}")
            pa = st.number_input(f"Pts A - M{i}", 0, 200, value=val_a, key=f"a{r_sel}{i}")
        with c2:
            st.write(f"🔴 {nombres[lj[2]]} & {nombres[lj[3]]}")
            pb = st.number_input(f"Pts B - M{i}", 0, 200, value=val_b, key=f"b{r_sel}{i}")
        return [r_sel, i, lj[0], lj[1], pa, lj[2], lj[3], pb]
