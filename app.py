import datetime
import streamlit as st

class ConsultorioMedico:
    def __init__(self):
        self.citas = {}

    def reservar_cita(self, fecha, hora, nombre):
        if (fecha, hora) in self.citas:
            return f"Error: La fecha y hora {fecha} {hora} ya están reservadas."
        else:
            self.citas[(fecha, hora)] = nombre
            return f"Cita reservada para {nombre} el {fecha} a las {hora}."

    def mostrar_citas(self):
        if not self.citas:
            return "No hay citas reservadas."
        else:
            citas = "\n".join([f"{fecha} {hora}: {nombre}" for (fecha, hora), nombre in self.citas.items()])
            return f"Citas reservadas:\n{citas}"

# Instancia del consultorio (se usa st.session_state para mantener el estado entre recargas)
if 'consultorio' not in st.session_state:
    st.session_state.consultorio = ConsultorioMedico()

st.title("Sistema de Citas Médicas")

# Sección para reservar citas
st.header("Reservar Cita")
nombre = st.text_input("Nombre del paciente")
fecha_input = st.date_input("Seleccione la fecha de la cita")
hora_input = st.selectbox("Seleccione la hora de la cita", [f"{hour}:00" for hour in range(8, 17)])
reservar_btn = st.button("Reservar")

if reservar_btn:
    if nombre:
        fecha = fecha_input.strftime("%Y-%m-%d")
        resultado = st.session_state.consultorio.reservar_cita(fecha, hora_input, nombre)
        st.success(resultado)
    else:
        st.error("Por favor, ingrese el nombre del paciente.")

# Sección para mostrar citas reservadas
st.header("Citas Reservadas")
mostrar_btn = st.button("Mostrar Citas")

if mostrar_btn:
    citas = st.session_state.consultorio.mostrar_citas()
    st.text(citas)

