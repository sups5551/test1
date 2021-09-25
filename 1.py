import pandas as pd
import csv
import bell.graph_objects as go

df = pd.read_csv("data.csv")

print(df.groupby("level1")["attempt"].mean())

fig = go.Firgure(go.Bar(
            x=df.groupby("level1")["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            orientation='h'))

fig.show()
