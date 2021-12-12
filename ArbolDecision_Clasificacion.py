#Módulo de árboles de decisión (Pronóstico)
#Importando las bibliotecas
import pandas as pd               
import numpy as np                
import matplotlib.pyplot as plt   
import seaborn as sns  
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import model_selection
from sklearn.tree import plot_tree
from sklearn.tree import export_text

def run (file):
    #Leyendo el archivo
    archivo = pd.read_csv(file)
    st.write ("El archivo seleccionado es el siguiente:")
    st.write(archivo)
    total_columns = len(archivo.axes[1])
    column_names = archivo.columns.values

    #Mostrando el mapa de calor
    plt.figure(figsize=(14,7))
    MatrizInf = np.triu(archivo.corr())
    sns.heatmap(archivo.corr(), cmap='RdBu_r', annot=True, mask=MatrizInf)
    st.write("El mapa de calor de las variables es el siguiente:")
    st.pyplot(plt)

    #Seleccionando las variables predictoras
    st.write ("Elige las variables predictoras.")
    variables_predictoras = st.multiselect("Selecciona las variables predictoras", column_names)
    agree = st.checkbox("Listo")

    #Procedemos a obtener la variable a pronosticar
    if agree:
            variables_restantes = column_names.tolist()
            for i in variables_predictoras:
                for n in variables_restantes:
                    if i == n:
                        variables_restantes.remove(n)
                        break
            #Eligiendo la variable a predecir      
            st.write("Elige la variable a predecir.")
            variable_predecir = st.selectbox("Selecciona la variable a predecir. Recuerda que es una variable que no varíen mucho sus valores.", variables_restantes)
            listo = st.checkbox("Continuar")

            if listo:
                X = np.array(archivo[variables_predictoras])
                Y = np.array(archivo[variable_predecir])
                X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, 
                                                                                test_size = 0.2, 
                                                                                random_state = 0,
                                                                                shuffle = True)
                #Entrenamos a nuestro modelo
                ClasificacionArbol = DecisionTreeClassifier()
                ClasificacionArbol.fit(X_train, Y_train)

                #Generamos el pronóstico
                Y_Clasificacion = ClasificacionArbol.predict(X_validation)

                #Mostrando la gráfica de la predicción contra los valores de prueba
                plt.figure(figsize=(20, 5))
                plt.plot(Y_validation, color='green', marker='o', label='Y_validation')
                plt.plot(Y_Clasificacion, color='red', marker='o', label='Y_Clasificacion')
                plt.xlabel('Paciente')
                plt.ylabel('Tamaño del tumor')
                plt.title('Pacientes con tumores cancerígenos')
                plt.grid(True)
                plt.legend()
                st.write("La gráfica de los datos de prueba contra los pronosticados son:")
                st.pyplot(plt)
                st.write("La exactitud promedio del modelo generado es: " + str(ClasificacionArbol.score(X_validation, Y_validation)))

                #Mostrando la importancia de las Variables
                i = 0
                lista_variables = list(variables_predictoras)
                Prediccion = pd.DataFrame({'Variables' : lista_variables, 'Importancia' : ClasificacionArbol.feature_importances_})
                st.write("La importancia de las variables para la predicción se detalla a continuación:")
                st.write(Prediccion)

                #Creando el árbol y mostrándolo al usuario
                st.write("Selecciona la forma en la que deseas visualziar el árbol")
                tipo  = st.radio("Elige la forma de visualizar el árbol.", ("Texto", "Imagen"))
                st.write("Nota: La imagen puede tardar bastante dependiendo del tamaño del árbol.")
                
                #Si elige imagen
                if tipo == "Imagen":
                    st.write("Imprimiendo la imagen del árbol.")    
                    plt.figure(figsize=(16,16))  
                    plot_tree(ClasificacionArbol, feature_names = variables_predictoras)
                    st.pyplot(plt)

                elif tipo == "Texto":
                    st.write("Para una mejor visualización en texto, deberás descargar el archivo '.txt' que se muestra en el siguiente botón:")
                    Reporte = export_text(ClasificacionArbol, feature_names = lista_variables)
                    st.download_button("Descarga el archivo del árbol", Reporte)
                
                #Hacer un pronóstico
                st.write("Si deseas hacer un pronóstico, indica los siguientes valores:")
                with st.form("Pronósticos"):
                    i = 0
                    var = []

                    #Hacemos que streamlit pida cada una de las variables predictoras seleccionadas
                    while i<len(variables_predictoras):
                        param = st.number_input(variables_predictoras[i])
                        var.insert(i, param)
                        i = i + 1
                    parametros = st.form_submit_button("Calcular")
                    if parametros:
                        i = 0
                        
                        #Creamos el dataframe para la predicción
                        Prediccion = pd.DataFrame({'prueba' : [0]})
                        while i < len(variables_predictoras):
                            Prediccion.insert(i, str(variables_predictoras[i]), var[i])
                            i = i + 1
                        del(Prediccion['prueba'])                        
                        #Imprimimos la predicción
                        st.write("El resultado de la predicción es: " + str(ClasificacionArbol.predict(Prediccion)))