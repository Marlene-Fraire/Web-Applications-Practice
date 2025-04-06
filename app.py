import scipy.stats
import streamlit as st 
import time

st.header('Lanzar una moneda')

#Gráfico de lineas incial
chart =st.line_chart([0.5])

#Función que emula lanzamiento de moneda y actualiza la media
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no= 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count /outcome_no
        chart.add_rows([mean])
        time.sleep(0.05) #Espera para simular proceso paso a paso

    return mean

#Interfaz de usuario
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

#Acción cuando se presiona el botón
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso...')
    final_mean = toss_coin(number_of_trials)
    st.success(f'Media final: {final_mean:.4f}')