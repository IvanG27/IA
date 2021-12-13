#Importando las bibliotecas que vamos a utilizar
import streamlit as st
import Reglas_Asociacion as RA 
import Metricas_Distancia as MD
import Clustering_Jerarquico as CJ
import Clustering_Particional as CP
import Clasificacion_RL as RL
import ArbolDecision_Pronostico as ADP
import ArbolDecision_Clasificacion as ADC

#Datos de la página principal
st.sidebar.header("Menú principal")
opcion = st.sidebar.selectbox ("Selecciona una opción del menú", ("Página inicial", "Algoritmo Reglas de Asociación", "Algoritmo Métricas de distancia",
"Algoritmo Clustering Jerárquico", "Algoritmo Clustering Particional", "Algoritmo Clasificación (Regresión Logística)",
"Algoritmo Árbol de Decisión (Pronóstico)", "Algoritmo Árbol de Decisión (Clasificación)")) #Menú

#En caso de que el usuario elija la página principal
if opcion == "Página inicial":
    st.header("Bienvenido a AlgorithmPRO")
    st.write("Este programa fue diseñado para implementar algunos de los algoritmos vistos durante la clase" +
    " de Inteligencia Artificial. Para su funcionamiento es necesario que se trabaje con archivos 'csv'"+
    " y dar las entradas correspondientes para obtener los resultados correctos. A continuación, se muestran"+
    " las instrucciones de uso: ")
    st.write ("Es muy importante que sigas las instrucciones de cada algoritmo, de no ser así se generarán errores.")
    instrucciones = st.selectbox("Elige el algoritmo del que deseas saber instrucciones", ("Algoritmo Reglas de Asociación", "Algoritmo Métricas de Distancia",
    "Algoritmo Clustering Jerárquico", "Algoritmo Clustering Particional", "Algoritmo Clasificación (Regresión Logística)",
    "Algoritmo Árbol de Decisión (Pronóstico)", "Algoritmo Árbol de Decisión (Clasificación)"))

    #Instrucciones algoritmo relgas de asociación
    if instrucciones == "Algoritmo Reglas de Asociación":
        st.subheader("Instrucciones del Algoritmo Reglas de Asociación: ")
        st.write("1. Deberás seleccionar tu archivo con terminación 'csv' el cual debe tener valores de cadenas. En caso de que hayas subido alguno en otro algoritmo, puede que se haya conservado.")
        st.write("2. Deberás de indicar si la primer fila de tu archivo es parte de los datos o no." + 
        " De ser así, se mostrarán los datos del archivo con la primer fila como parte de ellos.")
        st.write("3. Posteriormente, se mostrarán lista de las frecuencias generada y su gráfica.   ")
        st.write("4. Se deberá de ingresar el soporte mínimo, la confianza mínima y la elevación mínima."
        +" El valor por default para cada uno de estos campos será 0.01 ya que es el valor mínimo, "+
        "mientras que, el valor máximo es de 1 para el soporte y la confianza.")
        st.write("5. Una vez que hayas ingresado los datos, deberás de presionar el botón de 'Calcular'"+
        " para proceder con la obtención de las reglas.")
        st.write("6. Se mostrarán las reglas obtenidas con los valores dados.")
    
    #Algoritmo métricas de distacia
    elif instrucciones == "Algoritmo Métricas de Distancia":
        st.subheader("Instrucciones del Algoritmo Métricas de Distancia: ")
        st.write("1. Deberás seleccionar tu archivo con terminación 'csv' el cual debe tener valores numéricos. En caso de que hayas subido alguno en otro algoritmo, puede que se haya conservado.")
        st.write("2. Selecciona el tipo de métrica de distancia que deseas utilizar.")
        st.write("3. Elige si deseas saber la distancia de dos datos, un rango de datos o todos los datos.")
        st.write("4. En caso de elegir dos datos, deberás de ingresar sus índices correspondietes.")
        st.write("5. En caso de elegir un rango de datos, deberás de indicar los índices de los dos rangos de datos")
        st.write("6. En caso de elegir el rango de datos o todos los datos, los resultados se mostrarán como"+
        " una tabla.")

    #Instrucciones algoritmo Clustering Jerárquico
    elif instrucciones == "Algoritmo Clustering Jerárquico":
        st.subheader("Instrucciones del Algoritmo Clustering Jerárquico: ")
        st.write ("1. Deberás seleccionar tu archivo con terminación 'csv' el cual debe tener valores numéricos. En caso de que hayas subido alguno en otro algoritmo, puede que se haya conservado.")
        st.write ("2. En la evaluación visual deberás de seleccionar una variable con valores repetitivos para mostrar una gráfica que la compare con las demás variables.")
        st.write ("3. Para mostrar la imagen deberás de marcar la casilla de ver gráfica, esto debido a que se aumenta mucho el tiempo de ejecución, se recomienda que una vez vista, se desactive para mayor rapidez.")
        st.write ("4. Se mostrará el mapa de calor de la correlación de las variables que tienes en tu archivo.")
        st.write ("5. Deberás de elegir las variables que se analizarán según tu criterio y marcar la casilla listo cuando hayas terminado.")
        st.write ("6. Se mostrarán todos los datos con cada una de las variables seleccionadas.")
        st.write ("7. Deberás seleccionar el tipo de distancia con la que deseas trabajar. El valor por default es la distancia euclidiana.")
        st.write ("8. Se mostrará una imagen con los clústers formados con los datos seleccionados.")
        st.write ("9. Deberás ingresar los clústeres que se generaron.")
        st.write ("10. Se mostrará una tabla con cada uno de los centroides formados con el valor promedio para cada variable.")
        st.write ("11. Podrás ver la cantidad de datos que conforman a cada clúster.")
        st.write ("Nota: Al elegir las variables a analizar se pondrá oscura la pantalla, pero podrás seguir eligiendo variables.")

    #Instrucciones algoritmo Clustering Particional
    elif instrucciones == "Algoritmo Clustering Particional":
        st.subheader("Instrucciones del Algoritmo Clustering Particional: ")
        st.write ("1. Deberás seleccionar tu archivo con terminación 'csv' el cual debe tener valores numéricos. En caso de que hayas subido alguno en otro algoritmo, puede que se haya conservado.")
        st.write ("2. En la evaluación visual deberás de seleccionar una variable con valores repetitivos para mostrar una gráfica que la compare con las demás variables.")
        st.write ("3. Para mostrar la imagen deberás de marcar la casilla de ver gráfica, esto debido a que se aumenta mucho el tiempo de ejecución, se recomienda que una vez vista, se desactive para mayor rapidez.")
        st.write ("4. Se mostrará el mapa de calor de la correlación de las variables que tienes en tu archivo.")
        st.write ("5. Deberás de elegir las variables que se usarán para pronosticar según tu criterio y marcar la casilla listo cuando hayas terminado.")
        st.write ("6. Se mostrarán todos los datos con cada una de las variables seleccionadas.")
        st.write ("7. Obtendremos el número de clústeres mediante el método del codo.")
        st.write ("8. Se mostrará el número de clústeres a utilizar.")
        st.write ("9. Se mostrarán los centroides con el promedio de sus valores, la cantidad de datos por centroide y una tabla con todos los datos.")
        st.write ("10. Si deseas ver un centroide en particular, podrás seleccionar uno de ellos indicando el número del centroide.")

    #Instrucciones algoritmo Algoritmo Clasificación (Regresión Logística)
    elif instrucciones == "Algoritmo Clasificación (Regresión Logística)":
        st.subheader("Instrucciones del Algoritmo Clasificación (Regresión Logística)")
        st.write ("1. Deberás seleccionar tu archivo con terminación 'csv' el cual debe tener valores numéricos. En caso de que hayas subido alguno en otro algoritmo, puede que se haya conservado.")
        st.write ("2. En la evaluación visual deberás de seleccionar una variable con valores repetitivos para mostrar una gráfica que la compare con las demás variables.")
        st.write ("3. Para mostrar la imagen deberás de marcar la casilla de ver gráfica, esto debido a que se aumenta mucho el tiempo de ejecución, se recomienda que una vez vista, se desactive para mayor rapidez.")
        st.write ("4. Se mostrará el mapa de calor de la correlación de las variables que tienes en tu archivo.")
        st.write ("5. Deberás de elegir las variables que se usarán para pronosticar según tu criterio y marcar la casilla listo cuando hayas terminado.")
        st.write ("6. Deberás seleccionar la variable de clase, es decir, la variable que deseas predecir.")
        st.write ("7. Se mostrará la exactitud del modelo generado.")
        st.write ("8. Se mostrará la matriz de clasificación del modelo.")
        st.write ("9. Se mostrará la ecuación del modelo que se generó.")
        st.write ("10. En caso de querer hacer un pronóstico, deberás de dar el valor a las variables que elegiste para pronosticar.")
        st.write ("11. Deberás de presionar el botón 'Calcular' y se mostrará el resultado de la predicción.")

    #Instrucciones algoritmo Árbol de Decisión (Pronóstico)
    elif instrucciones == "Algoritmo Árbol de Decisión (Pronóstico)":
        st.subheader("Instrucciones del Algoritmo Árbol de Decisión (Pronóstico)")
        st.write ("1. Deberás seleccionar tu archivo con terminación 'csv' el cual debe tener valores numéricos. En caso de que hayas subido alguno en otro algoritmo, puede que se haya conservado.")
        st.write ("2. Se mostrará el mapa de calor de la correlación de las variables que tienes en tu archivo.")
        st.write ("3. Deberás de elegir las variables que se usarán para pronosticar según tu criterio y marcar la casilla listo cuando hayas terminado.")
        st.write ("4. Deberás seleccionar la variable de clase, es decir, la variable que deseas predecir.")
        st.write ("5. Se mostrará la gráfica del modelo obtenido con los datos pronosticados contra los valores de prueba.")
        st.write ("6. Se indicará la exactitud del modelo generado.")
        st.write ("7. Se mostrará la importancias de las variables para el modelo.")
        st.write ("8. Se te dará a aelegir la forma de visualizar el árbol. En texto, se generará un archivo 'txt' que podrás descargar y en imagen se mostrará esta, aunque puede tardar dependiendo del tamaño del árbol.")
        st.write ("9. En caso de que desees hace un pronóstico, deberás de indicar los valores de las variables para pronosticar que indicaste.")
        st.write ("10. Deberás de pulsar el botón 'Calcular' y se mostrará el resultado del pronóstico.")

    #Instrucciones algoritmo Árbol de Decisión (Clasificación)
    elif instrucciones == "Algoritmo Árbol de Decisión (Clasificación)":
        st.subheader("Instrucciones del Algoritmo Árbol de Decisión (Pronóstico)")
        st.write ("1. Deberás seleccionar tu archivo con terminación 'csv' el cual debe tener valores numéricos. En caso de que hayas subido alguno en otro algoritmo, puede que se haya conservado.")
        st.write ("2. Se mostrará el mapa de calor de la correlación de las variables que tienes en tu archivo.")
        st.write ("3. Deberás de elegir las variables que se usarán para pronosticar según tu criterio y marcar la casilla listo cuando hayas terminado.")
        st.write ("4. Deberás seleccionar la variable de clase, es decir, la variable que deseas predecir. Ten en cuenta que esta variable tiene que tener poca variedad en sus valores.")
        st.write ("5. Se mostrará la gráfica del modelo obtenido con los datos pronosticados contra los valores de prueba.")
        st.write ("6. Se indicará la exactitud del modelo generado.")
        st.write ("7. Se mostrará la importancias de las variables para el modelo.")
        st.write ("8. Se te dará a aelegir la forma de visualizar el árbol. En texto, se generará un archivo 'txt' que podrás descargar y en imagen se mostrará esta, aunque puede tardar dependiendo del tamaño del árbol.")
        st.write ("9. En caso de que desees hace un pronóstico, deberás de indicar los valores de las variables para pronosticar que indicaste.")
        st.write ("10. Deberás de pulsar el botón 'Calcular' y se mostrará el resultado del pronóstico.")

#Opción para el algoritmo apriori
elif opcion == "Algoritmo Reglas de Asociación":  
    st.header ("Algoritmo Reglas de Asociación")
    uploaded_fileRA = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores de cadenas.")
    if uploaded_fileRA is not None: ##Si no es nulo el archivo podemos continuar
        RA.run(uploaded_fileRA)

#Opción para el algoritmo métricas de distancia
elif opcion == "Algoritmo Métricas de distancia":
    st.header ("Métricas de Distancia")
    uploaded_fileMD = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores numéricos.")
    if uploaded_fileMD is not None:
        MD.run(uploaded_fileMD)

#Opción para el algoritmo Clustering Jerárquico
elif opcion == "Algoritmo Clustering Jerárquico":
    st.header ("Clustering Jerárquico")
    uploaded_fileCJ = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores numéricos")
    if uploaded_fileCJ is not None:
        CJ.run(uploaded_fileCJ)

#Opción para el algoritmo de clustering particional
elif opcion == "Algoritmo Clustering Particional":
    st.header ("Clustering Particional")
    uploaded_fileCP = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores numéricos.")
    if uploaded_fileCP is not None:
        CP.run(uploaded_fileCP)

#Opción para el algoritmo Regresión Lógistica
elif opcion == "Algoritmo Clasificación (Regresión Logística)":
    st.header ("Regresión Logística")
    uploaded_fileRL = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores numéricos.")
    if uploaded_fileRL is not None:
        RL.run(uploaded_fileRL)

#Opción para el algoritmo árbol de decisión (pronóstico)
elif opcion == "Algoritmo Árbol de Decisión (Pronóstico)":
    st.header ("Árbol de Decisión (Pronóstico)")
    uploaded_fileADP = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores numéricos.")
    if uploaded_fileADP is not None:
        ADP.run(uploaded_fileADP)

#Opción para el algoritmo árbol de decisión (clasificación)
elif opcion == "Algoritmo Árbol de Decisión (Clasificación)":
    st.header ("Árbol de Decisión (Clasificación)")
    uploaded_fileADC = st.file_uploader("Selecciona o arrastra tu archivo con terminación '.csv' que tenga valores numéricos.")
    if uploaded_fileADC is not None:
        ADC.run(uploaded_fileADC)