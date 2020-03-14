import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
from dash.dependencies import Input, Output

colors = {
    'background': '#87CEFA',
    'text': '#000080'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Привет! Я Даша Добровольская<3',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='И это моя личная страничка.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Markdown('''
                 **Мою страницу в вк можно посмотреть [тут](https://vk.com/smiling_pigeon).**''',style={
        'textAlign': 'center',
        'color': colors['text']
        }),
    html.Div([
            html.Img(src='https://sun9-29.userapi.com/c830408/v830408255/9ffd1/ri9CkANIPtM.jpg',style={
'width':'75%', 'margin-left':150, 'margin-top':30, 'textAlign': 'center'})
            ]),

    html.Label('Еда - любофь'),
    dcc.Slider(
            id='my-slider',
            min=1,
            max=10,
            marks={i: 'Сердечко {}'.format(i) for i in range(11)},
            value=10,
            ),
            html.Div(id='slider-output-container'),
    html.Label('А ты?'),
    dcc.Slider(
            id='your-slider',
            min=1,
            max=10,
            marks={i: 'Сердечко {}'.format(i) for i in range(11)},
            value=1,
            ),
            html.Div(id='slider-output-container2'),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Я люблю', value='Всех животных, особенно собак, особенно больших. Мороженное, мир во всем мире и моих друзей. О, и аниме! И сериальчики хехе'),
        dcc.Tab(label='Мои хобби', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'Я люблю':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'Мои хобби':
        return html.Div([
            html.H3('Tab content 2')
        ])
    
@app.callback(
        dash.dependencies.Output('slider-output-container', 'children'),
        [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return 'Я люблю покушать на: "{}" сердечек из 10'.format(value)
            
@app.callback(
        dash.dependencies.Output('slider-output-container2', 'children'),
        [dash.dependencies.Input('your-slider', 'value')])
def update_output1(value):
    return 'Я люблю покушать на: "{}" сердечек из 10'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
