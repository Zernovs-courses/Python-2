from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "/home/gleb/Documents/Python/Python-2/Python-2/lessons/K0609-22/world2015.csv"
)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            children="Hello, Sirius",
        ),
        dash_table.DataTable(data=df.to_dict("records"), page_size=10),
        dcc.RadioItems(
            options=["GDP_per_capita", "Life_expectancy", "Population"],
            value="GDP_per_capita",
            id="radio-items",
        ),
        dcc.Graph(
            figure={},
            id ="graph",
        ),
    ]
)

@callback(
    Output("graph", "figure"), 
    Input("radio-items", "value")
)
def update_graph(col_chos):
    fig = px.scatter(
                df,
                x="GDP_per_capita",
                y=col_chos,
                size="Population",
                color="Continent",
                hover_name="Country",
                log_x=True,
                size_max=60,
            )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
