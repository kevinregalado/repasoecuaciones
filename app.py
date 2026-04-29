# ===== archivo: app.py =====
import streamlit as st
from utils import generar_ecuacion, formatear_ecuacion

st.set_page_config(page_title="Ecuaciones", page_icon="🧮")

st.title("🧮 Practica Ecuaciones de Primer Grado")
st.write("Resuelve la ecuación. La solución siempre es un entero entre 1 y 10.")

# Estado
if "ecuacion" not in st.session_state:
    st.session_state.ecuacion = generar_ecuacion()

# Obtener datos
a, b, c, solucion = st.session_state.ecuacion

# Mostrar ecuación
st.subheader(f"Ecuación: {formatear_ecuacion(a, b, c)}")

# Input usuario
respuesta = st.number_input("Ingresa el valor de x:", step=1, format="%d")

# Verificar
if st.button("Verificar"):
    if respuesta == solucion:
        st.success("✅ Correcto")
        st.snow()
    else:
        st.error(f"❌ Incorrecto. Respuesta correcta: {solucion}")

# Nueva ecuación
if st.button("Nueva ecuación"):
    st.session_state.ecuacion = generar_ecuacion()
    st.rerun()


