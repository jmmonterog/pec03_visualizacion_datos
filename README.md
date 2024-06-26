# Análisis de Nombres de Recién Nacidos en España (2002-2022)

## Autor
**Jesús Manuel Montero Garrido**  
Correo: [jmonterogarr@uoc.edu](mailto:jmonterogarr@uoc.edu)

## Descripción
Esta visualización interactiva analiza la evolución de los nombres más populares en España desde 2002 hasta 2022. La visualización incluye comparaciones nacionales y regionales, mostrando cómo las preferencias de nombres reflejan cambios culturales y sociales. Los gráficos de barras, líneas y pendientes permiten explorar las tendencias de nombres por género, año y comunidad autónoma.

## a) Origen y Licencia de los Datos
### Origen de los Datos
Los datos utilizados en esta visualización provienen de registros oficiales de nombres de recién nacidos en España para los años 2002 y 2022. Estos datos fueron recolectados y proporcionados por el Instituto Nacional de Estadística (INE) y otras fuentes oficiales de las comunidades autónomas.

![image](https://github.com/jmmonterog/pec03_visualizacion_datos/assets/103445965/1472aac1-8abe-4196-96ec-7d4b755888af)

https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177009&menu=resultados&secc=1254736195498&idp=1254734710990#_tabs-1254736195498
![image](https://github.com/jmmonterog/pec03_visualizacion_datos/assets/103445965/f6b1467d-6ac3-49b5-ad57-032e8886c0e9)


### Licencia de los Datos
Los datos están bajo una licencia de uso público, lo que permite su acceso y uso para fines educativos y no comerciales. Es importante consultar la página oficial del INE y las fuentes de datos regionales para obtener detalles específicos sobre las licencias y condiciones de uso.

## b) Herramienta Utilizada y Sus Características
### Herramienta
La visualización fue creada utilizando Dash, una biblioteca de Python para la creación de aplicaciones web analíticas e interactivas.

### Características de Dash
- **Interactividad**: Dash permite crear gráficos interactivos y componentes web que responden a las acciones del usuario, como selecciones y clics.
- **Integración con Plotly**: Utiliza Plotly para generar gráficos ricos y dinámicos, con soporte para una amplia variedad de tipos de gráficos.
- **Desarrollo con Python**: Permite a los desarrolladores usar Python para crear aplicaciones web, integrando perfectamente con bibliotecas de análisis de datos como Pandas y NumPy.
- **Extensibilidad**: Dash es altamente extensible, permitiendo la inclusión de CSS, JavaScript y otros elementos web para mejorar la apariencia y funcionalidad.
- **Facilidad de Uso**: Simplifica la creación de aplicaciones web complejas con un enfoque en la simplicidad y la facilidad de uso, adecuada tanto para desarrolladores experimentados como para principiantes.

## c) Presentación de la Navegación / Animación de la Visualización Creada
La visualización creada está estructurada en varias secciones interactivas, cada una enfocada en un aspecto diferente del análisis de nombres:

1. **Introducción**: Proporciona un contexto sobre la importancia de los nombres y el objetivo de la visualización.

   ![image](https://github.com/jmmonterog/pec03_visualizacion_datos/assets/103445965/d0200a15-0b11-41ff-9b5f-06b985a9572f)

2. **Sección 1: Comparación Nacional**: Incluye gráficos de barras que muestran los 10 nombres más populares en España en 2002 y 2022.

   ![image](https://github.com/jmmonterog/pec03_visualizacion_datos/assets/103445965/365b6ec3-5081-499e-b813-0f9648e39fad)

3. **Sección 2: Análisis Regional**: Presenta gráficos de barras regionales con filtros para seleccionar la comunidad autónoma, género y año. Un dropdown permite explorar cómo varían los nombres entre diferentes regiones.

![image](https://github.com/jmmonterog/pec03_visualizacion_datos/assets/103445965/1cfa1a03-162f-4179-93e5-933ddf5af5dd)

   
4. **Sección 3: Evolución Temporal**: Ofrece un gráfico de pendiente (slope chart) para visualizar la evolución de los nombres a lo largo del tiempo. Un selector permite elegir nombres específicos para un análisis detallado.

![image](https://github.com/jmmonterog/pec03_visualizacion_datos/assets/103445965/26ca149c-215f-4c21-b1d4-5e76d51929e6)

   
5. **Conclusión**: Resume las tendencias principales y reflexiona sobre los cambios culturales observados.

   ![image](https://github.com/jmmonterog/pec03_visualizacion_datos/assets/103445965/aaa25f13-6a32-499c-9eba-3c33054c766a)


## d) Análisis de los Elementos Visuales Usados
### Tipo de Gráficos
- **Gráficos de Barras**: Utilizados para comparar la popularidad de los nombres a nivel nacional y regional. Los gráficos de barras permiten una fácil comparación visual de las cantidades.
- **Gráfico de Pendiente (Slope Chart)**: Muestra la evolución de los nombres más populares entre 2002 y 2022, destacando las tendencias y cambios a lo largo del tiempo.
- **Dropdown y RadioItems**: Proveen una interfaz intuitiva para filtrar y seleccionar datos específicos, mejorando la interactividad de la visualización.

### Interacción
- **Dropdowns**: Permiten seleccionar comunidades autónomas y nombres específicos para un análisis detallado.
- **RadioItems**: Facilitan la selección de género y año, filtrando los datos en los gráficos de barras.
- **Gráficos Interactivos**: Los gráficos generados con Plotly permiten hacer zoom, desplazar y obtener detalles adicionales al pasar el cursor sobre los elementos.

### Colores
- **Colores Vibrantes y Diferenciados**: Utilizados en los gráficos para distinguir claramente entre diferentes categorías (por ejemplo, nombres masculinos y femeninos, diferentes años).
- **Paletas de Colores Temáticas**: Aplicadas para mejorar la coherencia visual y la estética de la visualización.

### Textos
- **Textos Breves y Concisos**: Utilizados en las descripciones y etiquetas para proporcionar contexto sin sobrecargar al usuario con información.
- **Encabezados y Subtítulos**: Empleados para organizar y separar secciones, facilitando la navegación y comprensión de la visualización.

## e) Reflexiones Finales
### Qué Explica y Aporta la Visualización
La visualización muestra cómo las preferencias de nombres en España han cambiado entre 2002 y 2022, reflejando influencias culturales y sociales. Destaca la diversificación y modernización de los nombres, así como la influencia de factores globales y regionales.

### Formas de Captar la Atención del Usuario
- **Interactividad**: Permite a los usuarios explorar los datos de manera dinámica, filtrando y seleccionando diferentes categorías para un análisis personalizado.
- **Elementos Visuales Atractivos**: Uso de colores vibrantes y gráficos interactivos para hacer la visualización visualmente atractiva y fácil de entender.
- **Diseño Intuitivo**: La estructura clara y organizada, con secciones separadas y herramientas de navegación intuitivas, facilita la exploración y comprensión de la información.
- **Resumen y Reflexiones**: Proporciona un análisis conciso y reflexiones finales que ayudan a contextualizar los datos y entender las tendencias observadas.

La combinación de estos elementos asegura que la visualización no solo sea informativa, sino también atractiva y fácil de usar, proporcionando una experiencia enriquecedora para el usuario.



