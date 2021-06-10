import pandas as xyz
import plotly.express as plotly

data=xyz.read_csv("data.csv")

graph=plotly.scatter(data, x="date", y="cases", color="country", title="Covid Cases Of Different Countries")
graph.show()