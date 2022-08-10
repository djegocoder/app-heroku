import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import plotly
import json
import pandas as pd
import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

df = pd.read_csv('static/planilha.csv')

fig1 = pio.read_json("static/grafico1.json")
graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

fig2 = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 100,
      line = dict(color = "black", width = 0.5),
      label = ["Palmeiras","Corinthians","Internacional","Atlético MG","Fluminense","Atlético PR","São Paulo","Santos",
                "Flamengo","Botafogo","Red Bull Bragantino","Goiás","Cuiabá","Coritiba","América MG","Avaí","Ceará","Atlétigo GO",
                "Juventude","Fortaleza","Betfair","Galera.bet","Estrelabet","Betano","Sportsbet.io","Pixbet","Blaze.bet","Betpix365",
                "LuckSports.bet","Dafabet","Betcris","Amulerobet"],
      color = "#310c6b"
    ),
    link = dict(
      source = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [20,21,22,23,23,22,24,25,25,26,27,25,28,29,25,25,30,31,25,30],
      value =  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
  ))])

#fig2.update_layout(title_text="Basic Sankey Diagram", font_size=25)
graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

fig3 = px.scatter_geo(df,lon='longitude_decimal',lat="latitude_decimal",hover_name="Times", scope="south america",color="Times",)
#pio.write_json(fig3,file="static/grafico2.json")
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


@app.route("/bets")
def index():
    return render_template("bet.html",graph1JSON=graph1JSON,graph2JSON=graph2JSON,graph3JSON=graph3JSON,graph4JSON=graph4JSON,graph5JSON=graph5JSON,graph6JSON=graph6JSON)

@app.route("/")
def resume():
    return render_template("index.html")

@app.route("/portifolio1")
def portifolio1():
    return render_template("portifolio-1.html")

@app.route("/portifolio2")
def portifolio2():
    return render_template("portifolio-2.html")

@app.route("/portifolio3")
def portifolio3():
    return render_template("portifolio-3.html")

@app.route("/portifolio4")
def portifolio4():
    return render_template("portifolio-4.html")

@app.route("/portifolio5")
def portifolio5():
    return render_template("portifolio-5.html")

@app.route("/portifolio6")
def portifolio6():
    return render_template("portifolio-6.html")

@app.route("/portifolio7")
def portifolio7():
    return render_template("portifolio-7.html")    

@app.route("/portifolio8")
def portifolio8():
    return render_template("portifolio-8.html")

@app.route("/portifolio9")
def portifolio9():
    return render_template("portifolio-9.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)
