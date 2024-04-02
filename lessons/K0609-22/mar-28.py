from dash import Dash, dcc, html, callback, Input, Output
import plotly.express as px
import pandas as pd
import psutil

df = pd.DataFrame()
for i in range(psutil.cpu_count()):
    df[f"cpu{i+1}"] = [pd.NA] * 250

# print(df.head())

app = Dash()

app.layout = html.Div([
    html.H1(id='h1', children=''),
    dcc.Graph(id='cpu_graph', figure={}),

    dcc.Interval(id='timer', interval=100, n_intervals=1000)
])

@callback(Output('h1', 'children'), 
          Output('cpu_graph', 'figure'),
          Input('timer', 'n_intervals'))
def update(n):
    cpu = psutil.cpu_percent(percpu=True)

    df.iloc[:-1, :] = df.iloc[1:, :]
    df.iloc[-1, :] = cpu

    fig = px.line(df, line_shape='spline')

    return str(cpu), fig


if __name__ == '__main__':
    app.run(debug=True)