#from dash import Dash, html, dcc
import plotly.express as px
import plotly
import json
import pandas as pd
import os
from flask import Flask, render_template

app = Flask(__name__)

df = pd.read_csv('static/planilha.csv')
fig = px.bar(df, x="Times", y="Sigla", color="Bet", barmode="group")
graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

@app.route("/")
def index():
    return render_template("layout.html",graphJSON=graphJSON)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)
