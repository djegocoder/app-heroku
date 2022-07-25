import plotly.express as px
import plotly.io as pio
import plotly
import json
import pandas as pd
import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

df = pd.read_csv('static/planilha.csv')

fig1 = pio.read_json("static/grafico2.json")
graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

fig2 = pio.read_json("static/grafico1.json")
graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

fig3 = px.scatter_geo(df,lon='longitude_decimal',lat="latitude_decimal",hover_name="Times", scope="south america",color="Times",symbol="Plataforma de Aposta")
pio.write_json(fig3,file="static/grafico2.json")
graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

fig4 = px.scatter_geo(df,lon='longitude_decimal',lat="latitude_decimal",hover_name="Times", scope="south america",
        color="Times", size=[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15],opacity=0.5,symbol="Estádio",center={"lat":-15,"lon":-50})
graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

fig5 = px.scatter_geo(df,lon='longitude_decimal',lat="latitude_decimal",hover_name="Times", scope="south america",
        color="Times", size=[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15],opacity=0.5,symbol="Estádio",center={"lat":-15,"lon":-50})
graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

fig6 = px.scatter_geo(df,lon='longitude_decimal',lat="latitude_decimal",hover_name="Times", scope="south america",
        color="Times", size=[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15],opacity=0.5,symbol="Estádio",center={"lat":-15,"lon":-50})
graph6JSON = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)


@app.route("/")
def index():
    return render_template("layout.html",graph1JSON=graph1JSON,graph2JSON=graph2JSON,graph3JSON=graph3JSON,graph4JSON=graph4JSON,graph5JSON=graph5JSON,graph6JSON=graph6JSON)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)
