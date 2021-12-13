#Módulo clasificación (regresión logística)
#Importando las bibliotecas necesarias
import pandas as pd               
import numpy as np                
import matplotlib.pyplot as plt   
import seaborn as sns  
import streamlit as st
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def run(file):
    archivo = pd.read_csv(file)
    st.write ("El archivo seleccionado es el siguiente:")
    st.write(archivo)
    total_columns = len(archivo.axes[1])
    column_names = archivo.columns.values

    #Obteniendo la variable a analizar
    variable3 = st.text_input ("Ingresa el nombre de la variable a comparar. Recuerda que es preferible"+
    " que sus valores sean repetitivos")
    
    #Comprobando si la variable dada existe
    for i in column_names:
        if i == variable3:
            existe = True
            break
        else:
            existe = False

    #Si existe
    if existe == True:
        #Evaluación visual
        st.write("El mostrar la gráfica aumenta mucho el tiempo de ejecución, se recomienda que una vez vista por primera vez, se desactive antes de continuar.")
        st.write("La gráfica comparativa con respecto a las demás variables es:")
        agree = st.checkbox("Ver gráfica")
        if agree:
            sns.pairplot(archivo, hue=variable3) 
            st.pyplot (plt)

        #Matriz de correlaciones
        CorrArchivo = archivo.corr(method='pearson')
        #Mapa de calor
        st.write("A continuación, se muestra el mapa de calor")
        plt.figure(figsize=(14,7))
        MatrizInf = np.triu(CorrArchivo)
        sns.heatmap(CorrArchivo, cmap='RdBu_r', annot=True, mask=MatrizInf)
        st.pyplot(plt)

        #Selección de las variables predictoras
        st.write ("Elige las variables predictoras. Normalmente son variables cuyos valores son dispersos entre sí.")
        variable_predecirRL = st.multiselect("Selecciona las variables predictoras", column_names)
        agree = st.checkbox("Listo")

        if agree:
            variables_restantes = column_names.tolist()
            for i in variable_predecirRL:
                for n in variables_restantes:
                    if i == n:
                        variables_restantes.remove(n)
                        break
            #Eligiendo la variable a predecir      
            st.write("Elige la variable a predecir. Normalmente es una variable cuyos valores son muy repetitivos.")
            variable_predecir1 = st.selectbox("Selecciona la variable a predecir", variables_restantes)
            listo = st.checkbox("Continuar")
            if listo:
                X = np.array(archivo[variable_predecirRL])
                Y = np.array(archivo[variable_predecir1])
                X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, 
                                                                                test_size = 0.2, 
                                                                                random_state = 1234,
                                                                                shuffle = True)
                #Entrenamos a nuestro modelo
                Clasificacion = linear_model.LogisticRegression()
                Clasificacion.fit(X_train, Y_train)

                #Creando la probabilidad
                Probabilidad = Clasificacion.predict_proba(X_validation)

                #Creando las predicciones
                Predicciones = Clasificacion.predict(X_validation)

                #Obteniendo la exactitud de nuestro modelo
                st.write("La exactitud del modelo creado es:")
                st.write(Clasificacion.score(X_validation, Y_validation))

                #Con los datos obtenidos tenemos lo siguiente:
                st.write("Con las predicciones generadas tenemos los siguientes datos:")
                Y_Clasificacion = Clasificacion.predict(X_validation)
                Matriz_Clasificacion = pd.crosstab(Y_validation.ravel(), 
                                   Y_Clasificacion, 
                                   rownames=['Real'], 
                                   colnames=['Clasificación']) 
                st.write(Matriz_Clasificacion)

                #Haciendo la ecuación del modelo
                intercepto = Clasificacion.intercept_
                coeficientes = Clasificacion.coef_
                ecuacion = str(intercepto)
                i = 0
                while i < coeficientes.size:
                    ecuacion = ecuacion + str(coeficientes[0][i]) + " (" + str(variable_predecirRL[i]+")")
                    i = i + 1
                st.write("La ecuación del modelo es:")
                st.write(ecuacion)

                #Hacer un pronóstico
                st.write("Si deseas hacer un pronóstico, indica los siguientes valores:")
                with st.form("Pronósticos"):
                    i = 0
                    var = []

                    #Hacemos que streamlit pida cada una de las variables predictoras seleccionadas
                    while i<len(variable_predecirRL):
                        param = st.number_input(variable_predecirRL[i])
                        var.insert(i, param)
                        i = i + 1
                    parametros = st.form_submit_button("Calcular")
                    if parametros:
                        i = 0
                        
                        #Creamos el dataframe para la predicción
                        Prediccion = pd.DataFrame({'prueba' : [0]})
                        while i < len(variable_predecirRL):
                            Prediccion.insert(i, str(variable_predecirRL[i]), var[i])
                            i = i + 1
                        del(Prediccion['prueba'])                        
                        #Imprimimos la predicción
                        st.write("El resultado de la predicción es: " + str(Clasificacion.predict(Prediccion)))
                

    else:
        st.write("La variable indicada no existe")
