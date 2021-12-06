#Módulo de Clústering Jerárquico
#Importado las bibliotecas
import pandas as pd               
import numpy as np                
import matplotlib.pyplot as plt   
import seaborn as sns  
import streamlit as st
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

def run (file):
    archivo = pd.read_csv(file)
    st.write ("El archivo seleccionado es el siguiente:")
    st.write(archivo)

    #Obteniendo la variable a analizar
    variable = st.text_input ("Ingresa el nombre de la variable a analizar. Recuerda que es preferible"+
    " que sus valores sean repetitivos")
    total_columns = len(archivo.axes[1])
    column_names = archivo.columns.values

    #Comprobando si la variable dada existe
    for i in column_names:
        if i == variable:
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
            sns.pairplot(archivo, hue=variable) 
            st.pyplot (plt)

        #Matriz de correlaciones
        CorrArchivo = archivo.corr(method='pearson')
        #Mapa de calor
        st.write("A continuación, se muestra el mapa de calor")
        plt.figure(figsize=(14,7))
        MatrizInf = np.triu(CorrArchivo)
        sns.heatmap(CorrArchivo, cmap='RdBu_r', annot=True, mask=MatrizInf)
        st.pyplot(plt)

        #Selección de variables
        #with st.form (key = "variables"):
        variables = st.multiselect("Selecciona las variables a analizar", column_names)
        agree = st.checkbox("Listo")
        
        if agree:
            MatrizArchivo = np.array(archivo[variables])
            MArchivo = pd.DataFrame(MatrizArchivo)
            st.write(MArchivo)

            #Aplicando el Algoritmo 
            estandarizar = StandardScaler()              
            MEstandarizada = estandarizar.fit_transform(MatrizArchivo)
            DEstandarizados = pd.DataFrame(MEstandarizada) 

            #Mostrabdo los clústeres formados
            st.write("Los clústeres obtenidos son:")
            plt.figure(figsize=(10, 7))
            plt.title("Casos de hipoteca")
            plt.xlabel('Hipoteca')
            plt.ylabel('Distancia')

            #Dando al usuario la opción de elegir la métrica de distancia
            metrica = st.selectbox ("Selecciona el tipo de métrica con el que deseas trabajar", (
            "Euclidiana", "Chebyshev", "Manhattan"))
            if metrica == "Euclidiana":
                Arbol = shc.dendrogram(shc.linkage(MEstandarizada, method='complete', metric='euclidean'))
                st.pyplot(plt)
            elif metrica == "Chebyshev":
                Arbol = shc.dendrogram(shc.linkage(MEstandarizada, method='complete', metric='chebyshev'))
                st.pyplot(plt)
            elif metrica == "Manhattan":
                Arbol = shc.dendrogram(shc.linkage(MEstandarizada, method='complete', metric='cityblock'))
                st.pyplot(plt)            
            
            #Ingresar el número de clústeres que se obtienen
            num_cluster = st.number_input("Ingresa el valor de clústeres obtenidos en la imagen anterior" +
            " El valor que debes ingresar es el número de colores de cada hoja", min_value=1)
            MJerarquico = AgglomerativeClustering(n_clusters=int(num_cluster), linkage='complete', affinity='euclidean')
            MJerarquico.fit_predict(MEstandarizada)
            columnas_innecesarias = column_names.tolist()

            #Obteniendo las columnas que no fueron elegidas por el usuario
            for i in column_names:
                for w in variables:
                    if i == w:
                        columnas_innecesarias.remove(i)
                        break
            
            #Creando el cluster
            archivo = archivo.drop(columns=columnas_innecesarias)
            archivo['clusterH'] = MJerarquico.labels_
            archivo.groupby(['clusterH'])['clusterH'].count() 
            CentroidesH = archivo.groupby('clusterH').mean()
            st.write("Los centroides con valores medios formados se muestran a continuación:")
            st.write(CentroidesH)

            #Mostrando los elementos de cada clúster
            st.write(archivo.groupby(['clusterH'])['clusterH'].count())
           
    #Si no existe
    else:
        st.write("La variable indicada no existe en los datos")