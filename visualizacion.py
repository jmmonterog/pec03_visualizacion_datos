import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Función para crear gráficos de barras combinados para una comunidad autónoma específica
def create_combined_bar_chart(data, comunidad, gender_filter, year_filter):
    df = data[(data['Comunidad'] == comunidad)]
    if gender_filter:
        df = df[df['Sexo'] == gender_filter]
    if year_filter:
        df = df[df['Año'] == year_filter]
    
    top_10 = df.nlargest(10, 'Cantidad')
    fig = px.bar(top_10, x='Nombre', y='Cantidad', color='Sexo', title=f'Top 10 Nombres en {comunidad}', 
                 color_discrete_sequence=px.colors.qualitative.Set3)
    return fig

# Función para crear gráfico de slope
def create_slope_chart(data, selected_name=None):
    df_2002 = data[data['Año'] == 2002]
    df_2022 = data[data['Año'] == 2022]
    
    if selected_name:
        df_2002 = df_2002[df_2002['Nombre'] == selected_name]
        df_2022 = df_2022[df_2022['Nombre'] == selected_name]
    
    combined_df = pd.concat([df_2002, df_2022])
    combined_df['Año'] = combined_df['Año'].astype(str)
    
    fig = px.line(combined_df, x='Año', y='Cantidad', color='Nombre', markers=True,
                  title='Evolución de los Nombres Más Populares en España (2002-2022)',
                  color_discrete_sequence=px.colors.qualitative.Set2)
    return fig

# Cargar los datos nacionales
data_2002 = pd.read_csv('data/nombres_sexo_año_cantidad_2002.csv')
data_2022 = pd.read_csv('data/nombres_sexo_año_cantidad_2022.csv')

# Unir los datos de 2002 y 2022
data_nacional = pd.concat([data_2002, data_2022])

# Cargar datos de comunidades autónomas
data_andalucia = pd.read_csv('data/nombres_sexo_año_cantidad_andalucia.csv')
data_aragon = pd.read_csv('data/nombres_sexo_año_cantidad_aragon.csv')
data_asturias = pd.read_csv('data/nombres_sexo_año_cantidad_asturias.csv')
data_baleares = pd.read_csv('data/nombres_sexo_año_cantidad_baleares.csv')
data_canarias = pd.read_csv('data/nombres_sexo_año_cantidad_canarias.csv')
data_cantabria = pd.read_csv('data/nombres_sexo_año_cantidad_cantabria.csv')
data_castillalamancha = pd.read_csv('data/nombres_sexo_año_cantidad_castillalamancha.csv')
data_castillayleon = pd.read_csv('data/nombres_sexo_año_cantidad_castillayleon.csv')
data_cataluna = pd.read_csv('data/nombres_sexo_año_cantidad_cataluna.csv')
data_ceuta = pd.read_csv('data/nombres_sexo_año_cantidad_ceuta.csv')
data_extremadura = pd.read_csv('data/nombres_sexo_año_cantidad_extremadura.csv')
data_galicia = pd.read_csv('data/nombres_sexo_año_cantidad_galicia.csv')
data_larioja = pd.read_csv('data/nombres_sexo_año_cantidad_la_rioja.csv')
data_madrid = pd.read_csv('data/nombres_sexo_año_cantidad_madrid.csv')
data_melilla = pd.read_csv('data/nombres_sexo_año_cantidad_melilla.csv')
data_murcia = pd.read_csv('data/nombres_sexo_año_cantidad_murcia.csv')
data_paisvasco = pd.read_csv('data/nombres_sexo_año_cantidad_pais_vasco.csv')
data_navarra = pd.read_csv('data/nombres_sexo_año_cantidad_navarra.csv')
data_valencia = pd.read_csv('data/nombres_sexo_año_cantidad_valencia.csv')

# Asegurar que cada DataFrame tenga las columnas necesarias y la columna 'Comunidad'
comunidades_dfs = [
    (data_andalucia, 'Andalucía'), (data_aragon, 'Aragón'), (data_asturias, 'Asturias'), 
    (data_baleares, 'Baleares'), (data_canarias, 'Canarias'), (data_cantabria, 'Cantabria'), 
    (data_castillalamancha, 'Castilla-La Mancha'), (data_castillayleon, 'Castilla y León'), 
    (data_cataluna, 'Cataluña'), (data_ceuta, 'Ceuta'), (data_extremadura, 'Extremadura'), 
    (data_galicia, 'Galicia'), (data_larioja, 'La Rioja'), (data_madrid, 'Madrid'), 
    (data_melilla, 'Melilla'), (data_murcia, 'Murcia'), (data_paisvasco, 'País Vasco'), 
    (data_navarra, 'Navarra'), (data_valencia, 'Valencia')
]

for df, comunidad in comunidades_dfs:
    df['Comunidad'] = comunidad

# Combinar todos los datos en un solo DataFrame
data_comunidades = pd.concat([df for df, _ in comunidades_dfs])

# Gráficos de barras nacionales
top_10_names_2002 = data_2002.nlargest(10, 'Cantidad')
top_10_names_2022 = data_2022.nlargest(10, 'Cantidad')

fig_national_2002 = px.bar(top_10_names_2002, x='Nombre', y='Cantidad', color='Sexo', title='Top 10 Nombres en España (2002)',
                           color_discrete_sequence=px.colors.qualitative.Set1)
fig_national_2022 = px.bar(top_10_names_2022, x='Nombre', y='Cantidad', color='Sexo', title='Top 10 Nombres en España (2022)',
                           color_discrete_sequence=px.colors.qualitative.Set1)

# Crear gráfico de slope inicial
fig_slope = create_slope_chart(data_nacional)

# Crear la aplicación Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Análisis de Nombres de Recién Nacidos en España (2002-2022)', style={'textAlign': 'center', 'color': '#333'}),
    
    html.Div([
        html.Section([
            html.H2('Introducción', style={'backgroundColor': '#d1e7dd', 'padding': '10px', 'borderRadius': '5px'}),
            html.P('La elección de nombres refleja cambios culturales y sociales en la sociedad española. En esta visualización, analizamos la evolución de los nombres más populares entre 2002 y 2022.',
                   style={'padding': '10px'}),
        ], id='introduccion', style={'margin': '20px', 'border': '1px solid #ced4da', 'borderRadius': '5px'}),

        html.Section([
            html.H2('Sección 1: Comparación Nacional', style={'backgroundColor': '#f8d7da', 'padding': '10px', 'borderRadius': '5px'}),
            dcc.Graph(figure=fig_national_2002, id='grafico-barras-nacional-2002'),
            dcc.Graph(figure=fig_national_2022, id='grafico-barras-nacional-2022'),
            html.P('En 2002, los nombres más populares eran tradicionales, mientras que en 2022 hay una mayor diversidad con nombres internacionales ganando popularidad.',
                   style={'padding': '10px'})
        ], id='comparacion-nacional', style={'margin': '20px', 'border': '1px solid #ced4da', 'borderRadius': '5px'}),
        
        html.Section([
            html.H2('Sección 2: Análisis Regional', style={'backgroundColor': '#cfe2ff', 'padding': '10px', 'borderRadius': '5px'}),
            dcc.Dropdown(
                id='dropdown-comunidad',
                options=[{'label': comunidad, 'value': comunidad} for comunidad in data_comunidades['Comunidad'].unique()],
                value='Andalucía',
                clearable=False,
                style={'marginBottom': '10px'}
            ),
            dcc.RadioItems(
                id='radio-genero',
                options=[{'label': 'Todos', 'value': ''},
                         {'label': 'Masculino', 'value': 'H'},
                         {'label': 'Femenino', 'value': 'M'}],
                value='',
                inline=True,
                style={'marginBottom': '10px'}
            ),
            dcc.RadioItems(
                id='radio-ano',
                options=[{'label': 'Todos', 'value': ''},
                         {'label': '2002', 'value': 2002},
                         {'label': '2022', 'value': 2022}],
                value='',
                inline=True,
                style={'marginBottom': '10px'}
            ),
            dcc.Graph(id='grafico-barras-regional'),
            html.P('Comparación de los nombres más populares en diferentes regiones y años.', style={'padding': '10px'})
        ], id='analisis-regional', style={'margin': '20px', 'border': '1px solid #ced4da', 'borderRadius': '5px'}),
        
        html.Section([
            html.H2('Sección 3: Evolución Temporal', style={'backgroundColor': '#e2e3e5', 'padding': '10px', 'borderRadius': '5px'}),
            html.Div([
                dcc.Dropdown(
                    id='dropdown-nombre',
                    options=[{'label': nombre, 'value': nombre} for nombre in data_nacional['Nombre'].unique()],
                    value=None,
                    placeholder='Seleccione un nombre',
                    style={'marginBottom': '10px'}
                ),
                dcc.Graph(id='grafico-slope')
            ], style={'marginBottom': '10px'}),
            html.P('La popularidad de ciertos nombres muestra fluctuaciones significativas a lo largo del tiempo, reflejando cambios en las preferencias culturales.',
                   style={'padding': '10px'})
        ], id='evolucion-temporal', style={'margin': '20px', 'border': '1px solid #ced4da', 'borderRadius': '5px'}),
        
        html.Section([
            html.H2('Conclusión', style={'backgroundColor': '#f8f9fa', 'padding': '10px', 'borderRadius': '5px'}),
            html.H3('Diversificación Cultural', style={'color': '#6c757d'}),
            html.P('La elección de nombres en España entre 2002 y 2022 refleja una sociedad en evolución, marcada por la diversificación cultural, la influencia global y los cambios generacionales en las preferencias.',
                   style={'padding': '10px'})
        ], style={'margin': '20px', 'border': '1px solid #ced4da', 'borderRadius': '5px'})
    ])
])

@app.callback(
    Output('grafico-barras-regional', 'figure'),
    [Input('dropdown-comunidad', 'value'),
     Input('radio-genero', 'value'),
     Input('radio-ano', 'value')]
)
def update_regional_chart(comunidad, gender_filter, year_filter):
    fig = create_combined_bar_chart(data_comunidades, comunidad, gender_filter, year_filter)
    return fig

@app.callback(
    Output('grafico-slope', 'figure'),
    [Input('dropdown-nombre', 'value')]
)
def update_slope_chart(selected_name):
    fig = create_slope_chart(data_nacional, selected_name)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

