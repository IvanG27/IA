#Módulo del algoritmo de métricas de distancia
#importando las bibliotecas
import streamlit as st
import pandas as pd                 
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist    
from scipy.spatial import distance
from sklearn.preprocessing import StandardScaler, MinMaxScaler 

#Haciendo lo necesario para el algoritmo
def run(file):
    #Leyendo los datos
    archivo = pd.read_csv (file)
    st.write("A continuación se muestran los datos seleccionados")
    st.write(archivo)
    #Obteniendo el total de columnas y de renglones
    total_rows = len(archivo.axes[0])
    total_columns = len(archivo.axes[1])

    #Estandarizando los datos
    estandarizar = StandardScaler()                              
    MEstandarizada = estandarizar.fit_transform(archivo)

    #Dejando que el usuario elija el tipo de distancia
    option = st.selectbox ("Selecciona el tipo de distancia con el que deseas trabajar", (
        "Euclidiana", "Chebyshev", "Manhattan", "Minkowski"))
    
    #Seleccionado el caso
    #Si la métrica es euclidiana
    if option == "Euclidiana":
        DstEuclidiana = distance.cdist(MEstandarizada, MEstandarizada, 'euclidean')
        MEuclidiana = pd.DataFrame(DstEuclidiana)
        
        #Obteniendo la distancia
        tipo  = st.radio("Elige el tipo de distancia que quieres calcular.", ("Dos datos", "Un rango de datos",
        "Todos los datos"))  

        #Para dos datos
        if tipo == "Dos datos":
            st.write("Ingresa el valor del renglón de cada dato.")
            col1 = st.number_input ("Primer dato:", min_value = 0, 
            max_value = total_rows)
            col2 = st.number_input ("Segundo dato:", min_value = 0, 
            max_value = total_rows)
            #Obteniendo la distancia
            Objeto1 = MEstandarizada[col1]
            Objeto2 = MEstandarizada[col2]
            dstEuclidiana = distance.euclidean(Objeto1,Objeto2)
            st.write ("La distancia entre el dato " + str(col1) + " y el dato " + str(col2) + " es de: "
            + str(dstEuclidiana))
        
        #Rango de datos
        elif tipo == "Un rango de datos":
            st.write("Ingresa el valor del renglón de cada dato para cada rango de datos.")
            #Primer rango de datos
            st.write("Para el primer rango de datos.")
            col1 = st.number_input ("Dato inicial del primer rango:", min_value = 0, 
            max_value = total_rows)
            col2 = st.number_input ("Dato final del primer rango:", min_value = int(col1 + 1), 
            max_value = total_rows)
            #Segundo rango de datos
            st.write("Para el segundo rango de datos.")
            col3 = st.number_input ("Dato inicial del segundo rango:", min_value = 0, 
            max_value = total_rows)
            col4 = st.number_input ("Dato final del segundo rango:", min_value = int(col3 + 1), 
            max_value = total_rows)
            DstEuclidiana = cdist(MEstandarizada[col1:col2], MEstandarizada[col3:col4], metric='euclidean')
            MEuclidiana = pd.DataFrame(DstEuclidiana)
            st.write ("La matriz distancia entre el rango de datos " + str(col1) + " : " + str(col2) + " y " +
            str(col3) + " : " + str(col4) + " es de: ")
            st.write (MEuclidiana)
        
        #Todos los datos
        elif tipo == "Todos los datos":
            DstEuclidiana = cdist(MEstandarizada, MEstandarizada, metric='euclidean')
            MEuclidiana = pd.DataFrame(DstEuclidiana)
            st.write("La distancia de todos los datos contra todos los datos es:")
            st.write(MEuclidiana)

    #Si la métrica es de Chebyshev
    elif option == "Chebyshev":
        DstChebyshev = distance.cdist(MEstandarizada, MEstandarizada, 'chebyshev')
        MChebyshev = pd.DataFrame(DstChebyshev)
        
        #Obteniendo la distancia
        tipo  = st.radio("Elige el tipo de distancia que quieres calcular.", ("Dos datos", "Un rango de datos",
        "Todos los datos"))  

        #Para dos datos
        if tipo == "Dos datos":
            st.write("Ingresa el valor del renglón de cada dato.")
            col1 = st.number_input ("Primer dato:", min_value = 0, 
            max_value = total_rows)
            col2 = st.number_input ("Segundo dato:", min_value = 0, 
            max_value = total_rows)
            #Obteniendo la distancia
            Objeto1 = MEstandarizada[col1]
            Objeto2 = MEstandarizada[col2]
            dstChebyshev = distance.chebyshev(Objeto1,Objeto2)
            st.write ("La distancia entre el dato " + str(col1) + " y el dato " + str(col2) + " es de: "
            + str(dstChebyshev))
        
        #Rango de datos
        elif tipo == "Un rango de datos":
            st.write("Ingresa el valor del renglón de cada dato para cada rango de datos.")
            #Primer rango de datos
            st.write("Para el primer rango de datos.")
            col1 = st.number_input ("Dato inicial del primer rango:", min_value = 0, 
            max_value = total_rows)
            col2 = st.number_input ("Dato final del primer rango:", min_value = int(col1 + 1), 
            max_value = total_rows)
            #Segundo rango de datos
            st.write("Para el segundo rango de datos.")
            col3 = st.number_input ("Dato inicial del segundo rango:", min_value = 0, 
            max_value = total_rows)
            col4 = st.number_input ("Dato final del segundo rango:", min_value = int(col3 + 1), 
            max_value = total_rows)
            DstChebyshev = cdist(MEstandarizada[col1:col2], MEstandarizada[col3:col4], metric='chebyshev')
            MChebyshev = pd.DataFrame(DstChebyshev)
            st.write ("La matriz distancia entre el rango de datos " + str(col1) + " : " + str(col2) + " y " +
            str(col3) + " : " + str(col4) + " es de: ")
            st.write (MChebyshev)
        
        #Todos los datos
        elif tipo == "Todos los datos":
            DstChebyshev = cdist(MEstandarizada, MEstandarizada, metric='chebyshev')
            MChebyshev = pd.DataFrame(DstChebyshev)
            st.write("La distancia de todos los datos contra todos los datos es:")
            st.write(MChebyshev)

    #Para la métrica de Manhattan
    if option == "Manhattan":
        DstManhattan = distance.cdist(MEstandarizada, MEstandarizada, 'cityblock')
        MManhattan = pd.DataFrame(DstManhattan)
        
        #Obteniendo la distancia
        tipo  = st.radio("Elige el tipo de distancia que quieres calcular.", ("Dos datos", "Un rango de datos",
        "Todos los datos"))  

        #Para dos datos
        if tipo == "Dos datos":
            st.write("Ingresa el valor del renglón de cada dato.")
            col1 = st.number_input ("Primer dato:", min_value = 0, 
            max_value = total_rows)
            col2 = st.number_input ("Segundo dato:", min_value = 0, 
            max_value = total_rows)
            #Obteniendo la distancia
            Objeto1 = MEstandarizada[col1]
            Objeto2 = MEstandarizada[col2]
            dstManhattan = distance.cityblock(Objeto1,Objeto2)
            st.write ("La distancia entre el dato " + str(col1) + " y el dato " + str(col2) + " es de: "
            + str(dstManhattan))
        
        #Rango de datos
        elif tipo == "Un rango de datos":
            st.write("Ingresa el valor del renglón de cada dato para cada rango de datos.")
            #Primer rango de datos
            st.write("Para el primer rango de datos.")
            col1 = st.number_input ("Dato inicial del primer rango:", min_value = 0, 
            max_value = total_rows)
            col2 = st.number_input ("Dato final del primer rango:", min_value = int(col1 + 1), 
            max_value = total_rows)
            #Segundo rango de datos
            st.write("Para el segundo rango de datos.")
            col3 = st.number_input ("Dato inicial del segundo rango:", min_value = 0, 
            max_value = total_rows)
            col4 = st.number_input ("Dato final del segundo rango:", min_value = int(col3 + 1), 
            max_value = total_rows)
            DstManhattan = cdist(MEstandarizada[col1:col2], MEstandarizada[col3:col4], metric='cityblock')
            MManhattan = pd.DataFrame(DstManhattan)
            st.write ("La matriz distancia entre el rango de datos " + str(col1) + " : " + str(col2) + " y " +
            str(col3) + " : " + str(col4) + " es de: ")
            st.write (MManhattan)
            
        #Todos los datos
        elif tipo == "Todos los datos":
            DstManhattan = cdist(MEstandarizada, MEstandarizada, metric='cityblock')
            MManhattan = pd.DataFrame(DstManhattan)
            st.write("La distancia de todos los datos contra todos los datos es:")
            st.write(MManhattan)

    #Para la métrica Minkowski
    if option == "Minkowski":
        DstMinkowski = distance.cdist(MEstandarizada, MEstandarizada, 'minkowski', p=1.5)
        MMinkowski = pd.DataFrame(DstMinkowski)
        
        #Obteniendo la distancia
        tipo  = st.radio("Elige el tipo de distancia que quieres calcular.", ("Dos datos", "Un rango de datos",
        "Todos los datos"))  
        
        #Para dos datos
        if tipo == "Dos datos":
            st.write("Ingresa el valor del renglón de cada dato.")
            col1 = st.number_input ("Primer dato:", min_value = 0, max_value = total_rows)
            col2 = st.number_input ("Segundo dato:", min_value = 0, max_value = total_rows)
            #Obteniendo la distancia
            Objeto1 = MEstandarizada[col1]
            Objeto2 = MEstandarizada[col2]
            dstMinkowski = distance.minkowski(Objeto1,Objeto2)
            st.write ("La distancia entre el dato " + str(col1) + " y el dato " + str(col2) + " es de: "+ str(dstMinkowski))
                
        
        #Rango de datos
        elif tipo == "Un rango de datos":
            st.write("Ingresa el valor del renglón de cada dato para cada rango de datos.")
            #Primer rango de datos
            st.write("Para el primer rango de datos.")
            col1 = st.number_input ("Dato inicial del primer rango:", min_value = 0, max_value = total_rows)
            col2 = st.number_input ("Dato final del primer rango:", min_value = int(col1 + 1), max_value = total_rows)
            #Segundo rango de datos
            st.write("Para el segundo rango de datos.")
            col3 = st.number_input ("Dato inicial del segundo rango:", min_value = 0, max_value = total_rows)
            col4 = st.number_input ("Dato final del segundo rango:", min_value = int(col3 + 1), max_value = total_rows)
            DstMinkowski = cdist(MEstandarizada[col1:col2], MEstandarizada[col3:col4], metric='minkowski', p=1.5)
            MMinkowski = pd.DataFrame(DstMinkowski)
            st.write ("La matriz distancia entre el rango de datos " + str(col1) + " : " + str(col2) + " y " +
            str(col3) + " : " + str(col4) + " es de: ")
            st.write (MMinkowski)
        
        #Todos los datos
        elif tipo == "Todos los datos":
            DstMinkowski = cdist(MEstandarizada, MEstandarizada, metric='minkowski', p=1.5)
            MMinkowski = pd.DataFrame(DstMinkowski)
            st.write("La distancia de todos los datos contra todos los datos es:")
            st.write(MMinkowski)