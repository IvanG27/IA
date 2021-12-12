#Módulo del algoritmo apriori
#Importando bibliotecas 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt;
import seaborn as sns
from apyori import apriori

#Haciendo lo necesario para el algoritmo
def run(file):
    #Leyendo el archivo
    option = st.selectbox('¿La primer fila del archivo es parte de los datos? De ser así los tomaremos en cuenta.', ('Sí', 'No'))
    if option == "Sí": #Verificamos
        archivo = pd.read_csv(file, header=None)
        st.write ("Tu archivo seleccionado es el siguiente:")
        st.write(archivo)
    else:
        archivo = pd.read_csv(file)
        st.write ("Tu archivo seleccionado es el siguiente:")
        st.write(archivo)
    
    #Procesamiento de los datos
    Transacciones = archivo.values.reshape(-1).tolist()
    Lista = pd.DataFrame(Transacciones)
    Lista['Frecuencia'] = 1
    Lista = Lista.groupby(by=[0], as_index=False).count().sort_values(by=['Frecuencia'], ascending=True)
    Lista['Porcentaje'] = (Lista['Frecuencia'] / Lista['Frecuencia'].sum()) 
    Lista = Lista.rename(columns={0 : 'Item'})

    #Mostrando los datos en orden por frecuencia:
    st.write("La lista generada con las frecuencias es la siguiente:\n")
    st.write(Lista)
    plt.figure(figsize=(16,20), dpi=300)
    plt.ylabel('Item')
    plt.xlabel('Frecuencia')
    plt.barh(Lista['Item'], width=Lista['Frecuencia'], color='blue')
    fig = plt
    st.write ("De este modo, la gráfica de frecuencias es:")
    st.pyplot(fig)

    #Preparación de los datos
    DatosLista = archivo.stack().groupby(level=0).apply(list).tolist()

    #Aplicando el algoritmo
    with st.form("Apriori"):
        soporte_min = st.number_input ('Ingresa el soporte mínimo, recuerda que el valor máximo es 1:',
        min_value = float(0.0001), max_value = float(1.0000), format = "%f")
        confianza_min = st.number_input ('Ingresa la confianza mínima, recuerda que el valor máximo es 1:',
        min_value = float(0.0001), max_value = float(1.0000), format = "%f")
        elevacion_min = st.number_input ('Ingresa la elevación mínima:', min_value = float(0.0001), format = "%f")
        agree = st.form_submit_button("Calcular")
        if agree:
            Reglas = apriori(DatosLista, min_support=soporte_min, min_confidence=confianza_min, min_lift=elevacion_min)
            Resultados = list(Reglas)
            #Imprimiendo el número de reglas obtenidas
            st.write ('El número de reglas obtenidas es: ' + str(len(Resultados)))
            if len(Resultados) >= 1:        
                st.write ('Mostrando las reglas obtenidas: \n')
                for item in Resultados:
                    #El primer índice de la lista
                    Emparejar = item[0]
                    items = [x for x in Emparejar]
                    regla = str(item[0]).replace("frozenset", "")
                    st.write('Regla: ' + str(regla))

                    #El segundo índice de la lista
                    st.write('Soporte: ' + str(item[1]))

                    #El tercer índice de la lista
                    st.write('Confianza: ' + str(item[2][0][2]))
                    st.write('Lift: ' + str(item[2][0][3])) 
                    st.write('=====================================') 

    
    
