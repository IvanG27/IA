#Módulo de clustering particional
#Importando las bibliotecas
import pandas as pd               
import numpy as np                
import matplotlib.pyplot as plt   
import seaborn as sns  
import streamlit as st
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from kneed import KneeLocator

def run (file):
    archivo = pd.read_csv(file)
    st.write ("El archivo seleccionado es el siguiente:")
    st.write(archivo)

    #Obteniendo la variable a analizar
    variable = st.text_input ("Ingresa el nombre de la variable a comparar. Recuerda que es preferible"+
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
        variables = st.multiselect("Selecciona las variables a analizar", column_names)
        agree = st.checkbox("Listo")
        if agree: 
            #Aplicando al algoritmo
            MatrizArchivo = np.array(archivo[variables])
            MArchivo = pd.DataFrame(MatrizArchivo)
            st.write(MArchivo)
            estandarizar = StandardScaler()                            
            MEstandarizada = estandarizar.fit_transform(MatrizArchivo)

            #Definiendo los k clústeres necesarios
            SSE = []
            for i in range(2, 12):
                km = KMeans(n_clusters=i, random_state=0)
                km.fit(MEstandarizada)
                SSE.append(km.inertia_)
            
            st.write("Utilizando el método del codo obtuvimos la siguiente gráfica:")
            plt.figure(figsize=(10, 7))
            plt.plot(range(2, 12), SSE, marker='o')
            plt.xlabel('Cantidad de clusters *k*')
            plt.ylabel('SSE')
            plt.title('Elbow Method')
            st.pyplot (plt)

            kl = KneeLocator(range(2, 12), SSE, curve="convex", direction="decreasing")
            st.write("El codo se localiza en: " + str(kl.elbow))

            #Creando los clusters
            MParticional = KMeans(n_clusters=kl.elbow, random_state=0).fit(MEstandarizada)
            MParticional.predict(MEstandarizada)
            MParticional.labels_
            columnas_innecesarias = column_names.tolist()

            #Obteniendo las columnas que no fueron elegidas por el usuario
            for i in column_names:
                for w in variables:
                    if i == w:
                        columnas_innecesarias.remove(i)
                        break
            
            #Eliminando dichas columnas
            archivo = archivo.drop(columns=columnas_innecesarias)
            archivo['clusterP'] = MParticional.labels_

            #Mostrando los centroides
            CentroidesP = archivo.groupby('clusterP').mean()
            st.write("A continuación, se muestran los clústeres con la media de sus valores para cada variable.")
            st.write(CentroidesP)

            #Mostrando la distribución de los datos de cada centroide
            st.write("Cada clúster se conforma por:")
            st.write(archivo.groupby(['clusterP'])['clusterP'].count())
            st.write("A continuación, se muestran todos los datos del archivo con su clúster respectivo.")
            st.write(archivo)

            #Mostrando un cluster en específico si el usuario lo desea
            st.write("Si deseas ver un clúster en específico, ingresa un número. Por default se muestra el cluster 0.")
            cluster = st.number_input ("Ingresa el cluster", max_value = int(kl.elbow-1), min_value= int(0))
            st.write(archivo[archivo.clusterP == cluster])
    else:
        st.write("La variable indicada no existe en los datos")