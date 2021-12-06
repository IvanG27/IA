#Importando las bibliotecas que vamos a utilizar
import streamlit as st
import Reglas_Asociacion as RA 
import Metricas_Distancia as MD
import Clustering_Jerarquico as CJ

#Datos de la página principal
st.sidebar.header("Menú principal")
opcion = st.sidebar.selectbox ("Selecciona una opción del menú", ("Página inicial", "Algoritmo Reglas de Asociación", "Algoritmo Métricas de distancia",
"Algoritmo Clústering Jerárquico")) #Menú

#En caso de que el usuario elija la página principal
if opcion == "Página inicial":
    st.header("Bienvenido a AlgorithmPRO")
    st.write("Este programa fue diseñado para implementar algunos de los algoritmos vistos durante la clase" +
    " de Inteligencia Artificial. Para su funcionamiento es necesario que se trabaje con archivos 'csv'"+
    " y dar las entradas correspondientes para obtener los resultados correctos. A continuación, se muestran"+
    " las instrucciones de uso: ")
    st.write ("Es muy importante que sigas las instrucciones de cada algoritmo, de no ser así se generarán errores.")
    instrucciones = st.selectbox("Elige el algoritmo del que deseas saber instrucciones", ("Algoritmo Reglas de Asociación", "Algoritmo Métricas de Distancia",
    "Algoritmo Clústering Jerárquico"))

    #Instrucciones algoritmo relgas de asociación
    if instrucciones == "Algoritmo Reglas de Asociación":
        st.subheader("Instrucciones del Algoritmo Reglas de Asociación: ")
        st.write("1. Deberás de subir tu archivo con terminación '.csv', el cual debe tener valores de cadenas.")
        st.write("2. Deberás de indicar si la primer fila de tu archivo es parte de los datos o no." + 
        " De ser así, se mostrarán los datos del archivo con la primer fila como parte de ellos.")
        st.write("3. Posteriormente, se mostrarán lista de las frecuencias generada y su gráfica.   ")
        st.write("4. Se deberá de ingresar el soporte mínimo, la confianza mínima y la elevación mínima."
        +" El valor por default para cada uno de estos campos será 0.01 ya que es el valor mínimo, "+
        "mientras que, el valor máximo es de 1 para el soporte y la confianza.")
        st.write("5. Una vez que hayas ingresado los datos, deberás de presionar el botón de 'Continuar'"+
        " para proceder con la obtención de las reglas.")
        st.write("6. Se mostrarán las reglas obtenidas con los valores dados.")
    
    #Algoritmo métricas de distacia
    elif instrucciones == "Algoritmo Métricas de Distancia":
        st.subheader("Instrucciones del Algoritmo Métricas de Distancia: ")
        st.write("1. Deberás de subir tu archivo con terminación 'csv', el cual debe tener valores numéricos.")
        st.write("2. Selecciona el tipo de métrica de distancia que deseas utilizar.")
        st.write("3. Elige si deseas saber la distancia de dos datos, un rango de datos o todos los datos.")
        st.write("4. En caso de elegir dos datos, deberás de ingresar sus índices correspondietes.")
        st.write("5. En caso de elegir un rango de datos, deberás de indicar los índices de los dos rangos de datos")
        st.write("6. En caso de elegir el rango de datos o todos los datos, los resultados se mostrarán como"+
        " una tabla.")

    #Instrucciones algoritmo Clustering Jerárquico
    elif instrucciones == "Algoritmo Clústering Jerárquico":
        st.subheader("Instrucciones del Algoritmo Clústering Jerárquico: ")
        st.write ("1. Deberás seleccionar tu archivo con terminación 'csv', el cual debe tener valores numéricos.")
        st.write ("2. Para la evaluación visual deberás de elegir una variable cuyos valores sean repetitivos.")
        st.write ("3. Se mostrará una gráfica comparativa de tu variable de clase contra las demás variables.")
        st.write ("4. Se mostrará el mapa de calor de las variables que tengas en tu archivo.")
        st.write ("5. Deberás de elegir las variables que se analizarán según tu criterio y marcar la casilla listo cuando hayas terminado.")
        st.write ("6. Se mostrarán todos los datos con cada una de las variables seleccionadas.")
        st.write ("7. Deberás seleccionar el tipo de distancia con la que deseas trabajar. El valor por default es la distancia euclidiana.")
        st.write ("8. Se mostrará una imagen con los clústers formados con los datos seleccionados.")
        st.write ("9. Deberás ingresar los clústeres que se generaron.")
        st.write ("10. Se mostrará una tabla con cada uno de los centroides formados con el valor promedio para cada variable.")
        st.write ("11. Podrás ver la cantidad de datos que conforman a cada clúster.")
        st.write ("Nota: Al elegir las variables a analizar se pondrá oscura la pantalla, pero podrás seguir eligiendo variables.")

#Opción para el algoritmo apriori
elif opcion == "Algoritmo Reglas de Asociación":  
    st.header ("Algoritmo Reglas de Asociación")
    uploaded_file = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores de cadenas")
    if uploaded_file is not None: ##Si no es nulo el archivo podemos continuar
        RA.run(uploaded_file)

#Opción para el algoritmo métricas de distancia
elif opcion == "Algoritmo Métricas de distancia":
    st.header ("Métricas de Distancia")
    uploaded_file = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores numéricos")
    if uploaded_file is not None:
        MD.run(uploaded_file)

#Opción para el algoritmo Clústering Jerárquico
elif opcion == "Algoritmo Clústering Jerárquico":
    st.header ("Clústering Jerárquico")
    uploaded_file = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores numéricos")
    if uploaded_file is not None:
        CJ.run(uploaded_file)