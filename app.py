import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
beers=['Abbot Ale', 'London Pride', 'Websters', 'Tetley', 'Fosters']

bitterness = go.Bar(
    x=beers,
    y=[35, 60, 85, 75, 20],
    name='IBU',
    marker={'color':'purple'}
)
alcohol = go.Bar(
    x=beers,
    y=[5.2, 4.8, 3.8, 3.2, 3],
    name='ABV',
    marker={'color':'blue'}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('something completely different'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )]
)

if __name__ == '__main__':
    app.run_server()
