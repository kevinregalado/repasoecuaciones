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


# ===== archivo: utils.py =====
import random

# Genera ecuación ax + b = c con solución entre 1 y 10

def generar_ecuacion():
    x = random.randint(1, 10)
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = a * x + b
    return a, b, c, x

# Formatea la ecuación para mostrar

def formatear_ecuacion(a, b, c):
    if b >= 0:
        return f"{a}x + {b} = {c}"
    else:
        return f"{a}x - {abs(b)} = {c}"
